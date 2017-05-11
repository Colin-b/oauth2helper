import requests
import base64
import json
import jwt
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
import logging


def validate(jwt_token, verify_expiry=True):
    """
    Validate token and return JSON header and body as a tuple.
    """
    json_header, json_body = decode(jwt_token)
    _validate_json_token(jwt_token, verify_expiry, json_header, json_body)
    return json_header, json_body


def decode(jwt_token):
    """
    Decode base64 encoded token and return JSON decoded header and body as a tuple.
    """
    if not jwt_token:
        raise ValueError('JWT Token is mandatory.')

    (jwt_header, jwt_body, jwt_sign) = jwt_token.split('.')

    return _to_json(jwt_header), _to_json(jwt_body)


def _validate_json_token(jwt_token, verify_expiry, json_header, json_body):
    public_key = _get_public_key(json_body, json_header)
    logging.debug('Public key: {0}'.format(public_key))

    jwt.decode(jwt_token, public_key, options={
        'verify_signature': True,
        'verify_exp': verify_expiry,
        'verify_nbf': True,
        'verify_iat': True,
        'verify_aud': False,
        'require_exp': True,
        'require_iat': True,
        'require_nbf': True
    })


def _get_public_key(json_body, json_header):
    kid = json_header.get('kid')
    if not kid:
        raise ValueError('No kid in JSON header.')

    # TODO cache this
    x5c = _request_x5c(json_body, kid)

    certificate_text = b"-----BEGIN CERTIFICATE-----\n" + x5c.encode('utf-8') + b"\n-----END CERTIFICATE-----"
    certificate = load_pem_x509_certificate(certificate_text, default_backend())
    return certificate.public_key()


def _request_x5c(json_body, kid):
    iss = json_body.get('iss')
    if iss is None:
        raise ValueError('No iss (i.e. identity provider) in JSON body.')

    tid = json_body.get('tid')
    if tid is None:
        raise ValueError('No tid in JSON body.')

    idp = iss.split(tid)[0]

    keys_response = requests.get(idp + 'common/discovery/keys')
    keys_json = keys_response.json()

    for key in keys_json.get('keys', []):
        if key['kid'] == kid:
            return key['x5c'][0]
    raise ValueError('{0} cannot be found in {1}.'.format(kid, keys_json))


def _to_json(base_64_json):
    decoded_json = decode_base64(base_64_json)
    return json.loads(decoded_json.decode('unicode_escape'))


def decode_base64(base64_encoded_string):
    """
    Decode base64, padding being optional.

    :param base64_encoded_string: Base64 data as an ASCII byte string
    :returns: The decoded byte string.
    """
    missing_padding = len(base64_encoded_string) % 4
    if missing_padding != 0:
        base64_encoded_string += '=' * (4 - missing_padding)
    return base64.b64decode(base64_encoded_string)
