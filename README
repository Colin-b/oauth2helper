# Provide information on OAuth2 #

## Validating a OAuth2 token ##

```python
from oauth2helper.token import validate

headers = {}  # Header containing the OAuth2 Token
my_token = headers.get('Bearer')

validate(my_token)
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
