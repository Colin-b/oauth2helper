import requests
import base64
import json
import jwt
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
import logging

_default_options = {
    'verify_signature': True,
    'verify_exp': True,
    'verify_nbf': True,
    'verify_iat': True,
    'verify_aud': False,
    'require_exp': True,
    'require_iat': True,
    'require_nbf': True
}


def validate(jwt_token: str, **options) -> (dict, dict):
    """
    Validate token and return JSON header and body as a tuple.

    :param jwt_token: JWT Token as provided in Bearer header.

    :param verify_signature: Default to True
    :param verify_exp: Check token expiry. Default to True
    :param verify_nbf: Default to True
    :param verify_iat: Default to True
    :param verify_aud: Default to False
    :param require_exp: Default to True
    :param require_iat: Default to True
    :param require_nbf: Default to True
    """
    json_header, json_body = decode(jwt_token)
    _validate_json_token(jwt_token, json_header, json_body, options)
    return json_header, json_body


def decode(jwt_token: str) -> (dict, dict):
    """
    Decode base64 encoded token and return JSON decoded header and body as a tuple.
    """
    if not jwt_token:
        raise ValueError('JWT Token is mandatory.')

    if jwt_token.count('.') < 2:
        raise ValueError('Invalid JWT Token (header, body and signature must be separated by dots).')

    (jwt_header, jwt_body, jwt_signature) = jwt_token.split('.', maxsplit=2)

    return _to_json(jwt_header), _to_json(jwt_body)


def _validate_json_token(jwt_token: str, json_header: dict, json_body: dict, options: dict):
    public_key = _get_public_key(json_body, json_header)
    logging.debug(f'Public key: {public_key}')
    jwt.decode(jwt_token, public_key, options={**_default_options, **options})


def _get_public_key(json_body: dict, json_header: dict):
    kid = json_header.get('kid')
    if not kid:
        raise ValueError('No kid in JSON header.')

    # TODO cache this
    x5c = _request_x5c(json_body, kid)

    certificate_text = b"-----BEGIN CERTIFICATE-----\n" + x5c.encode('utf-8') + b"\n-----END CERTIFICATE-----"
    certificate = load_pem_x509_certificate(certificate_text, default_backend())
    return certificate.public_key()


def _request_x5c(json_body: dict, kid: str) -> str:
    iss = json_body.get('iss')
    if iss is None:
        raise ValueError('No iss (i.e. identity provider) in JSON body.')

    tid = json_body.get('tid')
    if tid is None:
        raise ValueError('No tid in JSON body.')

    idp = iss.split(tid)[0]

    keys_response = requests.get(f'{idp}common/discovery/keys')
    keys_json = keys_response.json()

    for key in keys_json.get('keys', []):
        if key['kid'] == kid:
            return key['x5c'][0]
    raise ValueError(f'{kid} cannot be found in kid within {keys_json}.')


def _to_json(base_64_json: str) -> dict:
    decoded_json = decode_base64(base_64_json)
    return json.loads(decoded_json.decode('unicode_escape'))


def decode_base64(base64_encoded_string: str) -> bytes:
    """
    Decode base64, padding being optional.

    :param base64_encoded_string: Base64 data as an ASCII byte string
    :returns: The decoded byte string.
    """
    missing_padding = len(base64_encoded_string) % 4
    if missing_padding != 0:
        base64_encoded_string += '=' * (4 - missing_padding)
    return base64.b64decode(base64_encoded_string)
