<h2 align="center">Validate and extract information from OAuth2 token</h2>

<p align="center">
<a href='https://github.tools.digital.engie.com/gempy/oauth2helper/releases/latest'><img src='https://pse.tools.digital.engie.com/all/buildStatus/icon?job=team/oauth2helper/master&config=version'></a>
<a href='https://pse.tools.digital.engie.com/all/job/team/view/Python%20modules/job/oauth2helper/job/master/'><img src='https://pse.tools.digital.engie.com/all/buildStatus/icon?job=team/oauth2helper/master'></a>
<a href='https://pse.tools.digital.engie.com/all/job/team/view/Python%20modules/job/oauth2helper/job/master/cobertura/'><img src='https://pse.tools.digital.engie.com/all/buildStatus/icon?job=team/oauth2helper/master&config=testCoverage'></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href='https://pse.tools.digital.engie.com/all/job/team/view/Python%20modules/job/oauth2helper/job/master/lastSuccessfulBuild/testReport/'><img src='https://pse.tools.digital.engie.com/all/buildStatus/icon?job=team/oauth2helper/master&config=testCount'></a>
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
python -m pip install oauth2helper -i https://all-team-remote:tBa%40W%29tvB%5E%3C%3B2Jm3@artifactory.tools.digital.engie.com/artifactory/api/pypi/all-team-pypi-prod/simple
```
