from jwt.exceptions import InvalidTokenError


def user_name(json_body: dict) -> str:
    """
    Return user name stored in JSON body.
    :raises InvalidTokenError
    """
    upn = json_body.get('upn')
    if upn is None:
        raise InvalidTokenError('No upn (i.e. User ID) in JSON body.')
    return upn.split('@')[0]
