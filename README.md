<h2 align="center">OAuth2 helper</h2>

<p align="center">
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href='https://pse.tools.digital.engie.com/drm-all.gem/job/team/view/Python%20modules/job/oauth2helper/job/master/'><img src='https://pse.tools.digital.engie.com/drm-all.gem/buildStatus/icon?job=team/oauth2helper/master'></a>
</p>

Provides:

 * Validation of OAuth2 token
 * Extraction of data from validated (or decoded) token.

## Validating an OAuth2 token ##

```python
from oauth2helper.token import validate

headers = {}  # Header containing the OAuth2 Token
my_token = headers.get('Bearer')

validate(my_token)  # Will raise InvalidTokenError or InvalidKeyError in case validation failed
```

## Extracting user from a OAuth2 token ##

```python
from oauth2helper.token import validate
from oauth2helper.content import user_name

headers = {}  # Header containing the OAuth2 Token
my_token = headers.get('Bearer')

json_header, json_body = validate(my_token)
username = user_name(json_body)
```

Contributing
------------

Everyone is free to contribute on this project.

Before creating an issue please make sure that it was not already reported.

Project follow "Black" code formatting: https://black.readthedocs.io/en/stable/

To integrate it within Pycharm: https://black.readthedocs.io/en/stable/editor_integration.html#pycharm

To add the pre-commit hook, after the installation run: **pre-commit install**
