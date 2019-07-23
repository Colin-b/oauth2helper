import re

import pytest
import jwt

import oauth2helper


def test_None_token_cannot_be_decoded():
    with pytest.raises(jwt.InvalidTokenError) as exception_info:
        oauth2helper.decode(None)
    assert "JWT Token is mandatory." == str(exception_info.value)


def test_None_token_cannot_be_validated():
    with pytest.raises(jwt.InvalidTokenError) as exception_info:
        oauth2helper.validate(None)
    assert "JWT Token is mandatory." == str(exception_info.value)


def test_empty_token_cannot_be_decoded():
    with pytest.raises(jwt.InvalidTokenError) as exception_info:
        oauth2helper.decode("")
    assert "JWT Token is mandatory." == str(exception_info.value)


def test_empty_token_cannot_be_validated():
    with pytest.raises(jwt.InvalidTokenError) as exception_info:
        oauth2helper.validate("")
    assert "JWT Token is mandatory." == str(exception_info.value)


def test_invalid_token_cannot_be_decoded():
    with pytest.raises(jwt.InvalidTokenError) as exception_info:
        oauth2helper.decode("Invalid token")
    assert (
        "Invalid JWT Token (header, body and signature must be separated by dots)."
        == str(exception_info.value)
    )


def test_invalid_token_cannot_be_validated():
    with pytest.raises(jwt.InvalidTokenError) as exception_info:
        oauth2helper.validate("Invalid token")
    assert (
        "Invalid JWT Token (header, body and signature must be separated by dots)."
        == str(exception_info.value)
    )


def test_missing_upn():
    with pytest.raises(jwt.InvalidTokenError) as exception_info:
        oauth2helper.user_name({})
    assert "No upn (i.e. User ID) in JSON body." == str(exception_info.value)


@pytest.mark.xfail
def test_validation_failure_with_expiry():
    # TODO Launch locally with an up-to-date token
    expired = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlNTUWRoSTFjS3ZoUUVEU0p4RTJnR1lzNDBRMCIsImtpZCI6IlNTUWRoSTFjS3ZoUUVEU0p4RTJnR1lzNDBRMCJ9.eyJhdWQiOiIyYmVmNzMzZC03NWJlLTQxNTktYjI4MC02NzJlMDU0OTM4YzMiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yNDEzOWQxNC1jNjJjLTRjNDctOGJkZC1jZTcxZWExZDUwY2YvIiwiaWF0IjoxNTIwMjcwNTAxLCJuYmYiOjE1MjAyNzA1MDEsImV4cCI6MTUyMDI3NDQwMSwiYWlvIjoiWTJOZ1lFaHlXMjYwVS9kR1RGeWNTMWNPVnczYnpqVXQ0Zk96TkNTekJYaWMyWTVOWFFNQSIsImFtciI6WyJwd2QiXSwiZmFtaWx5X25hbWUiOiJCb3Vub3VhciIsImdpdmVuX25hbWUiOiJDb2xpbiIsImlwYWRkciI6IjE5NC4yOS45OC4xNDQiLCJuYW1lIjoiQm91bm91YXIgQ29saW4gKEVOR0lFIEVuZXJneSBNYW5hZ2VtZW50KSIsIm5vbmNlIjoiW1x1MDAyNzczNjJDQUVBLTlDQTUtNEI0My05QkEzLTM0RDdDMzAzRUJBN1x1MDAyN10iLCJvaWQiOiJkZTZiOGVjYS01ZTEzLTRhZTEtODcyMS1mZGNmNmI0YTljZGQiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTQwOTA4MjIzMy0xNDE3MDAxMzMzLTY4MjAwMzMzMC0zNzY5NTQiLCJzdWIiOiI2eEZSV1FBaElOZ0I4Vy10MnJRVUJzcElGc1VyUXQ0UUZ1V1VkSmRxWFdnIiwidGlkIjoiMjQxMzlkMTQtYzYyYy00YzQ3LThiZGQtY2U3MWVhMWQ1MGNmIiwidW5pcXVlX25hbWUiOiJKUzUzOTFAZW5naWUuY29tIiwidXBuIjoiSlM1MzkxQGVuZ2llLmNvbSIsInV0aSI6InVmM0x0X1Q5aWsyc0hGQ01oNklhQUEiLCJ2ZXIiOiIxLjAifQ.addwLSoO-2t1kXgljqnaU-P1hQGHQBiJMcNCLwELhBZT_vHvkZHFrmgfcTzED_AMdB9mTpvUm_Mk0d3F3RzLtyCeAApOPJaRAwccAc3PB1pKTwjFhdzIXtxib0_MQ6_F1fhb8R8ZcLCbwhMtT8nXoeWJOvH9_71O_vkfOn6E-VwLo17jkvQJOa89KfctGNnHNMcPBBju0oIgp_UVal311SMUw_10i4GZZkjR2I1m7EMg5jMwQgUatYWv2J5HoefAQQDat9jJeEnYNITxsJMN81FHTyuvMnN_ulFzOGtcvlBpmP6jVHfEDoJiqFM4NFh6r4IlOs2U2-jUb_bR5xi2zg"
    with pytest.raises(jwt.InvalidTokenError) as exception_info:
        oauth2helper.validate(expired)
    assert "Signature has expired" == str(exception_info.value)


@pytest.mark.xfail
def test_validation_sucess_without_expiry():
    # TODO Launch locally with an up-to-date token
    expired = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlNTUWRoSTFjS3ZoUUVEU0p4RTJnR1lzNDBRMCIsImtpZCI6IlNTUWRoSTFjS3ZoUUVEU0p4RTJnR1lzNDBRMCJ9.eyJhdWQiOiIyYmVmNzMzZC03NWJlLTQxNTktYjI4MC02NzJlMDU0OTM4YzMiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yNDEzOWQxNC1jNjJjLTRjNDctOGJkZC1jZTcxZWExZDUwY2YvIiwiaWF0IjoxNTIwMjcwNTAxLCJuYmYiOjE1MjAyNzA1MDEsImV4cCI6MTUyMDI3NDQwMSwiYWlvIjoiWTJOZ1lFaHlXMjYwVS9kR1RGeWNTMWNPVnczYnpqVXQ0Zk96TkNTekJYaWMyWTVOWFFNQSIsImFtciI6WyJwd2QiXSwiZmFtaWx5X25hbWUiOiJCb3Vub3VhciIsImdpdmVuX25hbWUiOiJDb2xpbiIsImlwYWRkciI6IjE5NC4yOS45OC4xNDQiLCJuYW1lIjoiQm91bm91YXIgQ29saW4gKEVOR0lFIEVuZXJneSBNYW5hZ2VtZW50KSIsIm5vbmNlIjoiW1x1MDAyNzczNjJDQUVBLTlDQTUtNEI0My05QkEzLTM0RDdDMzAzRUJBN1x1MDAyN10iLCJvaWQiOiJkZTZiOGVjYS01ZTEzLTRhZTEtODcyMS1mZGNmNmI0YTljZGQiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTQwOTA4MjIzMy0xNDE3MDAxMzMzLTY4MjAwMzMzMC0zNzY5NTQiLCJzdWIiOiI2eEZSV1FBaElOZ0I4Vy10MnJRVUJzcElGc1VyUXQ0UUZ1V1VkSmRxWFdnIiwidGlkIjoiMjQxMzlkMTQtYzYyYy00YzQ3LThiZGQtY2U3MWVhMWQ1MGNmIiwidW5pcXVlX25hbWUiOiJKUzUzOTFAZW5naWUuY29tIiwidXBuIjoiSlM1MzkxQGVuZ2llLmNvbSIsInV0aSI6InVmM0x0X1Q5aWsyc0hGQ01oNklhQUEiLCJ2ZXIiOiIxLjAifQ.addwLSoO-2t1kXgljqnaU-P1hQGHQBiJMcNCLwELhBZT_vHvkZHFrmgfcTzED_AMdB9mTpvUm_Mk0d3F3RzLtyCeAApOPJaRAwccAc3PB1pKTwjFhdzIXtxib0_MQ6_F1fhb8R8ZcLCbwhMtT8nXoeWJOvH9_71O_vkfOn6E-VwLo17jkvQJOa89KfctGNnHNMcPBBju0oIgp_UVal311SMUw_10i4GZZkjR2I1m7EMg5jMwQgUatYWv2J5HoefAQQDat9jJeEnYNITxsJMN81FHTyuvMnN_ulFzOGtcvlBpmP6jVHfEDoJiqFM4NFh6r4IlOs2U2-jUb_bR5xi2zg"
    json_header, json_body = oauth2helper.validate(expired, verify_exp=False)
    assert {
        "alg": "RS256",
        "kid": "SSQdhI1cKvhQEDSJxE2gGYs40Q0",
        "typ": "JWT",
        "x5t": "SSQdhI1cKvhQEDSJxE2gGYs40Q0",
    } == json_header
    assert {
        "aio": "Y2NgYEhyW260U/dGTFycS1cOVw3bzjUt4fOzNCSzBXic2Y5NXQMA",
        "amr": ["pwd"],
        "aud": "2bef733d-75be-4159-b280-672e054938c3",
        "exp": 1520274401,
        "family_name": "Bounouar",
        "given_name": "Colin",
        "iat": 1520270501,
        "ipaddr": "194.29.98.144",
        "iss": "https://sts.windows.net/24139d14-c62c-4c47-8bdd-ce71ea1d50cf/",
        "name": "Bounouar Colin (ENGIE Energy Management)",
        "nbf": 1520270501,
        "nonce": "['7362CAEA-9CA5-4B43-9BA3-34D7C303EBA7']",
        "oid": "de6b8eca-5e13-4ae1-8721-fdcf6b4a9cdd",
        "onprem_sid": "S-1-5-21-1409082233-1417001333-682003330-376954",
        "sub": "6xFRWQAhINgB8W-t2rQUBspIFsUrQt4QFuWUdJdqXWg",
        "tid": "24139d14-c62c-4c47-8bdd-ce71ea1d50cf",
        "unique_name": "JS5391@engie.com",
        "upn": "JS5391@engie.com",
        "uti": "uf3Lt_T9ik2sHFCMh6IaAA",
        "ver": "1.0",
    } == json_body


def test_content_extraction():
    json_body = {
        "aio": "Y2NgYEhyW260U/dGTFycS1cOVw3bzjUt4fOzNCSzBXic2Y5NXQMA",
        "amr": ["pwd"],
        "aud": "2bef733d-75be-4159-b280-672e054938c3",
        "exp": 1520274401,
        "family_name": "Bounouar",
        "given_name": "Colin",
        "iat": 1520270501,
        "ipaddr": "194.29.98.144",
        "iss": "https://sts.windows.net/24139d14-c62c-4c47-8bdd-ce71ea1d50cf/",
        "name": "Bounouar Colin (ENGIE Energy Management)",
        "nbf": 1520270501,
        "nonce": "['7362CAEA-9CA5-4B43-9BA3-34D7C303EBA7']",
        "oid": "de6b8eca-5e13-4ae1-8721-fdcf6b4a9cdd",
        "onprem_sid": "S-1-5-21-1409082233-1417001333-682003330-376954",
        "sub": "6xFRWQAhINgB8W-t2rQUBspIFsUrQt4QFuWUdJdqXWg",
        "tid": "24139d14-c62c-4c47-8bdd-ce71ea1d50cf",
        "unique_name": "JS5391@engie.com",
        "upn": "JS5391@engie.com",
        "uti": "uf3Lt_T9ik2sHFCMh6IaAA",
        "ver": "1.0",
    }
    assert "JS5391" == oauth2helper.user_name(json_body)
    assert "Bounouar Colin (ENGIE Energy Management)" == oauth2helper.get(
        json_body, "name"
    )


def test_content_extraction_missing_key():
    with pytest.raises(jwt.InvalidTokenError) as exception_info:
        oauth2helper.get({}, "qsdfqsdfqsdf")
    assert "No qsdfqsdfqsdf in JSON body." == str(exception_info.value)


def test_invalid_kid():
    expired = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImEzUU4wQlpTN3M0bk4tQmRyamJGMFlfTGRNTSIsImtpZCI6ImEzUU4wQlpTN3M0bk4tQmRyamJGMFlfTGRNTSJ9.eyJhdWQiOiIyYmVmNzMzZC03NWJlLTQxNTktYjI4MC02NzJlMDU0OTM4YzMiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yNDEzOWQxNC1jNjJjLTRjNDctOGJkZC1jZTcxZWExZDUwY2YvIiwiaWF0IjoxNDkwNzc5NzEyLCJuYmYiOjE0OTA3Nzk3MTIsImV4cCI6MTQ5MDc4MzYxMiwiYW1yIjpbInB3ZCJdLCJmYW1pbHlfbmFtZSI6IkRlIE1hZXllciIsImdpdmVuX25hbWUiOiJGYWJyaWNlIiwiaXBhZGRyIjoiMTA0LjQ2LjU4LjE0OSIsIm5hbWUiOiJEZSBNYWV5ZXIgRmFicmljZSAoZXh0ZXJuYWwpIiwibm9uY2UiOiI3MzYyQ0FFQS05Q0E1LTRCNDMtOUJBMy0zNEQ3QzMwM0VCQTciLCJvaWQiOiI1YTJmOGQyYS0xNzQ1LTRmNTctOTcwYS03YjIwMzU5YWUyZGMiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTQwOTA4MjIzMy0xNDE3MDAxMzMzLTY4MjAwMzMzMC0yODUxNjAiLCJwbGF0ZiI6IjMiLCJzdWIiOiJRcjhNZlAwQk9oRld3WlNoNFZSVEpYeGd3Z19XTFBId193TnBnS1lMQTJVIiwidGlkIjoiMjQxMzlkMTQtYzYyYy00YzQ3LThiZGQtY2U3MWVhMWQ1MGNmIiwidW5pcXVlX25hbWUiOiJCSUY1OTBAZW5naWUuY29tIiwidXBuIjoiQklGNTkwQGVuZ2llLmNvbSIsInZlciI6IjEuMCJ9.vZO7a5Vs0G_g92Bb00BPKcLuF9WmrqfLjwbLhz8xEe3OfqfthWHqh_jzf_Md88INc4ZuMqOMPhWZTZjQMgCACIpTiHDpFRkokZ-jqC09BaQSSjwV_27b-zy-m6CZcFtdUe10LIBQEqiL9JnZlVIrBgFqr49bKBvZKr3uuaoeiuR2XcC0U2klYkDr3CYIexX0w57lvD5Ow0xKkdWKYVswcJipenU9PP63R0wNXr-8cb-6PGIUzaQDREo-EuR2e3uShF9u5cagG7emt9fDmJr8eGxBJU9ppRoffJpuaYeJiIg1F_n0iK7hENnIjZVnHjFn46DZO-RPse8YZjd4YBuKsg"
    with pytest.raises(jwt.InvalidTokenError) as exception_info:
        oauth2helper.validate(expired)
    assert re.match(
        "a3QN0BZS7s4nN-BdrjbF0Y_LdMM is not a valid key identifier. Valid ones are .*",
        str(exception_info.value),
    )
