from jwt.exceptions import InvalidTokenError


def user_name(json_body: dict) -> str:
    """
    Return user name stored in JSON body.
    :raises InvalidTokenError
    """
    try:
        upn = get(json_body=json_body, key="upn")
    except InvalidTokenError as e:
        raise InvalidTokenError('No upn (i.e. User ID) in JSON body.')
    return upn.split('@')[0]

def get(json_body: dict, key) -> str:
    """
    Return value for a given key stored in JSON body
    :raises InvalidTokenError
    """
    value = json_body.get(key)
    if value is None:
        raise InvalidTokenError(f'No {key} in JSON body.')
    return value
