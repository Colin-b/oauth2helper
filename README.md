<h2 align="center">Validate and extract information from OAuth2 token</h2>

<p align="center">
<a href="https://pypi.org/project/oauth2helper/"><img alt="pypi version" src="https://img.shields.io/pypi/v/oauth2helper"></a>
<a href="https://travis-ci.org/Colin-b/oauth2helper"><img alt="Build status" src="https://api.travis-ci.org/Colin-b/oauth2helper.svg?branch=develop"></a>
<a href="https://travis-ci.org/Colin-b/oauth2helper"><img alt="Coverage" src="https://img.shields.io/badge/coverage-100%25-brightgreen"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://travis-ci.org/Colin-b/oauth2helper"><img alt="Number of tests" src="https://img.shields.io/badge/tests-13 passed-blue"></a>
<a href="https://pypi.org/project/oauth2helper/"><img alt="Number of downloads" src="https://img.shields.io/pypi/dm/oauth2helper"></a>
</p>

Provides:

 * Validation of OAuth2 token
 * Extraction of data from validated (or decoded) token.

## Validating an OAuth2 token

```python
import oauth2helper

headers = {"Authorization": "Bearer YOUR_OAUTH2_TOKEN"}
my_token = headers.get('Authorization')[7:]

# Will raise InvalidTokenError or InvalidKeyError in case validation failed
oauth2helper.validate(my_token, "https://provider_url/common/discovery/keys")
```

## Extracting user from a OAuth2 token

```python
import oauth2helper

headers = {"Authorization": "Bearer YOUR_OAUTH2_TOKEN"}
my_token = headers.get('Authorization')[7:]

json_header, json_body = oauth2helper.validate(my_token, "https://provider_url/common/discovery/keys")
username = oauth2helper.user_name(json_body)
```

## How to install
1. [python 3.6+](https://www.python.org/downloads/) must be installed
2. Use pip to install module:
```sh
python -m pip install oauth2helper
```
