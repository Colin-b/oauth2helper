import datetime

import pytest
from starlette.applications import Starlette
from starlette.authentication import requires
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import PlainTextResponse
from starlette.testclient import TestClient
import jwt


from oauth2helper.starlette import OAuth2IdTokenBackend, unauthorized


def create_client(**backend_options):
    backend = OAuth2IdTokenBackend(
        identity_provider_url="https://test_identity_provider",
        scopes_retrieval=lambda json_body: ["authenticated"],
        algorithms=["HS256"],
        # Avoid having to generate a private and public key
        verify_signature=False,
        **backend_options,
    )
    app = Starlette(
        middleware=[
            Middleware(AuthenticationMiddleware, backend=backend, on_error=unauthorized)
        ]
    )

    @app.route("/test")
    @requires(scopes=["authenticated"])
    def endpoint(request):
        return PlainTextResponse(request.user.display_name)

    return TestClient(app)


def create_token(
    responses, response_kid: str = "SSQdhI1cKvhQEDSJxE2gGYs40Q1", **body
) -> str:
    add_identity_provider_response(responses, kid=response_kid)
    expiry_in_1_hour = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    return jwt.encode(
        {"exp": expiry_in_1_hour, "iat": 1520270501, "nbf": 1520270501, **body},
        "secret",
        algorithm="HS256",
        headers={"kid": "SSQdhI1cKvhQEDSJxE2gGYs40Q1"},
    ).decode("unicode_escape")


def add_identity_provider_response(responses, kid):
    responses.add(
        responses.GET,
        "https://test_identity_provider",
        json={
            "keys": [
                {
                    "kid": kid,
                    "x5c": [
                        "MIIDBTCCAe2gAwIBAgIQdEMOjSqDVbdN3mzb2IumCzANBgkqhkiG9w0BAQsFADAtMSswKQYDVQQDEyJhY2NvdW50cy5hY2Nlc3Njb250cm9sLndpbmRvd3MubmV0MB4XDTE5MDYwNDAwMDAwMFoXDTIxMDYwNDAwMDAwMFowLTErMCkGA1UEAxMiYWNjb3VudHMuYWNjZXNzY29udHJvbC53aW5kb3dzLm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKEUUBvom99MdPXlrQ6S9MFmoQPoYI3NJVqEFOJcARY11dj3zyJogL8MTsTRt+DIJ8NyvYbgWC7K7zkAGzHQZhPJcM/AxSjFqh6qB98UqgxoSGBaG0A4lUZJHnKW3qx+YaiWrkg+z4sAwUkP0QgyI29Ejpkk6WUfe1rOJNc/defFUX+AVGxo81beLVAM/8tnCOSbF0H3IADwd76D/Hrp8RsGf4jPHr8N4VDsO/p7oj8rbOx0pL1ehjMK13zspmP8NO5mMcP9i5yiJ37FgbXESAxvja7I9t+y4LQYSu05M7la4Lqv//m5A8MBd6k0VxgF/Sq8GOIbkcQ0bJTCIN9B6oMCAwEAAaMhMB8wHQYDVR0OBBYEFNRP0Lf6MDeL11RDH0uL7H+/JqtLMA0GCSqGSIb3DQEBCwUAA4IBAQCJKR1nxp9Ij/yisCmDG7bdN1yHj/2HdVvyLfCCyReRfkB3cnTZVaIOBy5occGkdmsYJ+q8uqczkoCMAz3gvvq1c0msKEiNpqWNeU2aRXqyL3QZJ/GBmUK1I0tINPVv8j7znm0DcvHHXFvhzS8E4s8ai8vQkcpyac/7Z4PN43HtjDnkZo9Zxm7JahHshrhA8sSPvsuC4dQAcHbOrLbHG+HIo3Tq2pNl7mfQ9fVJ2FxbqlzPYr/rK8H2GTA6N55SuP3KTNvyL3RnMa3hXmGTdG1dpMFzD/IE623h/BqY6j29PyQC/+MUD4UCZ6KW9oIzpi27pKQagH1i1jpBU/ceH6AW"
                    ],
                }
            ]
        },
    )


def test_without_token():
    client = create_client()
    response = client.get("/test")
    assert response.status_code == 403
    assert response.text == "Forbidden"


def test_with_token_containing_upn(responses):
    client = create_client()
    response = client.get(
        "/test",
        headers={
            "Authorization": f"Bearer {create_token(responses, upn='test@test.com')}"
        },
    )
    assert response.status_code == 200
    assert response.text == "test@test.com"


def test_with_token_containing_field_name(responses):
    client = create_client(username_field="test_field")
    response = client.get(
        "/test",
        headers={
            "Authorization": f"Bearer {create_token(responses, test_field='test value')}"
        },
    )
    assert response.status_code == 200
    assert response.text == "test value"


def test_without_upn_in_token(responses):
    client = create_client()
    response = client.get(
        "/test", headers={"Authorization": f"Bearer {create_token(responses)}"}
    )
    assert response.status_code == 401
    assert response.text == "No upn in JSON body."


def test_without_field_name_in_token(responses):
    client = create_client(username_field="test_field")
    response = client.get(
        "/test", headers={"Authorization": f"Bearer {create_token(responses)}"}
    )
    assert response.status_code == 401
    assert response.text == "No test_field in JSON body."


def test_with_invalid_token(responses):
    client = create_client()
    response = client.get(
        "/test",
        headers={
            "Authorization": f"Bearer {create_token(responses, response_kid='SSQdhI1cKvhQEDSJxE2gGYs40Q2', upn='test@test.com')}"
        },
    )
    assert response.status_code == 401
    assert (
        response.text
        == "SSQdhI1cKvhQEDSJxE2gGYs40Q1 is not a valid key identifier. Valid ones are ['SSQdhI1cKvhQEDSJxE2gGYs40Q2']."
    )


def test_with_token_not_in_authorization_header():
    client = create_client()
    response = client.get("/test", headers={"Bearer": f"Bearer token"})
    assert response.status_code == 403
    assert response.text == "Forbidden"


def test_with_token_not_prefixed_with_bearer():
    client = create_client()
    response = client.get("/test", headers={"Authorization": "token"})
    assert response.status_code == 403
    assert response.text == "Forbidden"
