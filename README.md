<h2 align="center">OAuth2 helper</h2>

<p align="center">
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href='https://pse.tools.digital.engie.com/drm-all.gem/job/team/view/Python%20modules/job/oauth2helper/job/master/'><img src='https://pse.tools.digital.engie.com/drm-all.gem/buildStatus/icon?job=team/oauth2helper/master'></a>
</p>

Provides:

 * Validation of OAuth2 token
 * Extraction of data from validated (or decoded) token.

## Validating an OAuth2 token

```python
import oauth2helper

headers = {}  # Header containing the OAuth2 Token
my_token = headers.get('Bearer')

oauth2helper.validate(my_token)  # Will raise InvalidTokenError or InvalidKeyError in case validation failed
```

## Extracting user from a OAuth2 token

```python
import oauth2helper

headers = {}  # Header containing the OAuth2 Token
my_token = headers.get('Bearer')

json_header, json_body = oauth2helper.validate(my_token)
username = oauth2helper.user_name(json_body)
```

## How to install
1. [python 3.7+](https://www.python.org/downloads/) must be installed
2. Use pip to install module:
```sh
python -m pip install oauth2helper -i https://all-team-remote:tBa%40W%29tvB%5E%3C%3B2Jm3@artifactory.tools.digital.engie.com/artifactory/api/pypi/all-team-pypi-prod/simple
```
