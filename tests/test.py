import unittest
import jwt
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
import base64
import json
import os

import oauth2helper.token
import oauth2helper.content


class TestJwtMethods(unittest.TestCase):

    def test_rsa(self):
        cer_in = b"MIIDBTCCAe2gAwIBAgIQY4RNIR0dX6dBZggnkhCRoDANBgkqhkiG9w0BAQsFADAtMSswKQYDVQQDEyJhY2NvdW50cy5hY2Nlc3Njb250cm9sLndpbmRvd3MubmV0MB4XDTE3MDIxMzAwMDAwMFoXDTE5MDIxNDAwMDAwMFowLTErMCkGA1UEAxMiYWNjb3VudHMuYWNjZXNzY29udHJvbC53aW5kb3dzLm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMBEizU1OJms31S/ry7iav/IICYVtQ2MRPhHhYknHImtU03sgVk1Xxub4GD7R15i9UWIGbzYSGKaUtGU9lP55wrfLpDjQjEgaXi4fE6mcZBwa9qc22is23B6R67KMcVyxyDWei+IP3sKmCcMX7Ibsg+ubZUpvKGxXZ27YgqFTPqCT2znD7K81YKfy+SVg3uW6epW114yZzClTQlarptYuE2mujxjZtx7ZUlwc9AhVi8CeiLwGO1wzTmpd/uctpner6oc335rvdJikNmc1cFKCK+2irew1bgUJHuN+LJA0y5iVXKvojiKZ2Ii7QKXn19Ssg1FoJ3x2NWA06wc0CnruLsCAwEAAaMhMB8wHQYDVR0OBBYEFDAr/HCMaGqmcDJa5oualVdWAEBEMA0GCSqGSIb3DQEBCwUAA4IBAQAiUke5mA86R/X4visjceUlv5jVzCn/SIq6Gm9/wCqtSxYvifRXxwNpQTOyvHhrY/IJLRUp2g9/fDELYd65t9Dp+N8SznhfB6/Cl7P7FRo99rIlj/q7JXa8UB/vLJPDlr+NREvAkMwUs1sDhL3kSuNBoxrbLC5Jo4es+juQLXd9HcRraE4U3UZVhUS2xqjFOfaGsCbJEqqkjihssruofaxdKT1CPzPMANfREFJznNzkpJt4H0aMDgVzq69NxZ7t1JiIuc43xRjeiixQMRGMi1mAB75fTyfFJ/rWQ5J/9kh0HMZVtHsqICBF1tHMTMIK5rwoweY0cuCIpN7A/zMOQtoD"
        certificate_text = b"-----BEGIN CERTIFICATE-----\n" + cer_in + b"\n-----END CERTIFICATE-----"
        certificate = load_pem_x509_certificate(certificate_text, default_backend())
        public_key = certificate.public_key()

        options = {
            'verify_signature': True,
            'verify_exp': False,
            'verify_nbf': False,
            'verify_iat': False,
            'verify_aud': False,
            'require_exp': False,
            'require_iat': False,
            'require_nbf': False
        }

        encoded = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImEzUU4wQlpTN3M0bk4tQmRyamJGMFlfTGRNTSIsImtpZCI6ImEzUU4wQlpTN3M0bk4tQmRyamJGMFlfTGRNTSJ9.eyJhdWQiOiIyYmVmNzMzZC03NWJlLTQxNTktYjI4MC02NzJlMDU0OTM4YzMiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yNDEzOWQxNC1jNjJjLTRjNDctOGJkZC1jZTcxZWExZDUwY2YvIiwiaWF0IjoxNDkwNzc5NzEyLCJuYmYiOjE0OTA3Nzk3MTIsImV4cCI6MTQ5MDc4MzYxMiwiYW1yIjpbInB3ZCJdLCJmYW1pbHlfbmFtZSI6IkRlIE1hZXllciIsImdpdmVuX25hbWUiOiJGYWJyaWNlIiwiaXBhZGRyIjoiMTA0LjQ2LjU4LjE0OSIsIm5hbWUiOiJEZSBNYWV5ZXIgRmFicmljZSAoZXh0ZXJuYWwpIiwibm9uY2UiOiI3MzYyQ0FFQS05Q0E1LTRCNDMtOUJBMy0zNEQ3QzMwM0VCQTciLCJvaWQiOiI1YTJmOGQyYS0xNzQ1LTRmNTctOTcwYS03YjIwMzU5YWUyZGMiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTQwOTA4MjIzMy0xNDE3MDAxMzMzLTY4MjAwMzMzMC0yODUxNjAiLCJwbGF0ZiI6IjMiLCJzdWIiOiJRcjhNZlAwQk9oRld3WlNoNFZSVEpYeGd3Z19XTFBId193TnBnS1lMQTJVIiwidGlkIjoiMjQxMzlkMTQtYzYyYy00YzQ3LThiZGQtY2U3MWVhMWQ1MGNmIiwidW5pcXVlX25hbWUiOiJCSUY1OTBAZW5naWUuY29tIiwidXBuIjoiQklGNTkwQGVuZ2llLmNvbSIsInZlciI6IjEuMCJ9.vZO7a5Vs0G_g92Bb00BPKcLuF9WmrqfLjwbLhz8xEe3OfqfthWHqh_jzf_Md88INc4ZuMqOMPhWZTZjQMgCACIpTiHDpFRkokZ-jqC09BaQSSjwV_27b-zy-m6CZcFtdUe10LIBQEqiL9JnZlVIrBgFqr49bKBvZKr3uuaoeiuR2XcC0U2klYkDr3CYIexX0w57lvD5Ow0xKkdWKYVswcJipenU9PP63R0wNXr-8cb-6PGIUzaQDREo-EuR2e3uShF9u5cagG7emt9fDmJr8eGxBJU9ppRoffJpuaYeJiIg1F_n0iK7hENnIjZVnHjFn46DZO-RPse8YZjd4YBuKsg"
        jwt.decode(encoded, public_key, options=options)

        with self.assertRaises(jwt.ExpiredSignatureError):
            jwt.decode(encoded, public_key)

    def test_rsa_discovery(self):
        encoded = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImEzUU4wQlpTN3M0bk4tQmRyamJGMFlfTGRNTSIsImtpZCI6ImEzUU4wQlpTN3M0bk4tQmRyamJGMFlfTGRNTSJ9.eyJhdWQiOiIyYmVmNzMzZC03NWJlLTQxNTktYjI4MC02NzJlMDU0OTM4YzMiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yNDEzOWQxNC1jNjJjLTRjNDctOGJkZC1jZTcxZWExZDUwY2YvIiwiaWF0IjoxNDkwNzc5NzEyLCJuYmYiOjE0OTA3Nzk3MTIsImV4cCI6MTQ5MDc4MzYxMiwiYW1yIjpbInB3ZCJdLCJmYW1pbHlfbmFtZSI6IkRlIE1hZXllciIsImdpdmVuX25hbWUiOiJGYWJyaWNlIiwiaXBhZGRyIjoiMTA0LjQ2LjU4LjE0OSIsIm5hbWUiOiJEZSBNYWV5ZXIgRmFicmljZSAoZXh0ZXJuYWwpIiwibm9uY2UiOiI3MzYyQ0FFQS05Q0E1LTRCNDMtOUJBMy0zNEQ3QzMwM0VCQTciLCJvaWQiOiI1YTJmOGQyYS0xNzQ1LTRmNTctOTcwYS03YjIwMzU5YWUyZGMiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTQwOTA4MjIzMy0xNDE3MDAxMzMzLTY4MjAwMzMzMC0yODUxNjAiLCJwbGF0ZiI6IjMiLCJzdWIiOiJRcjhNZlAwQk9oRld3WlNoNFZSVEpYeGd3Z19XTFBId193TnBnS1lMQTJVIiwidGlkIjoiMjQxMzlkMTQtYzYyYy00YzQ3LThiZGQtY2U3MWVhMWQ1MGNmIiwidW5pcXVlX25hbWUiOiJCSUY1OTBAZW5naWUuY29tIiwidXBuIjoiQklGNTkwQGVuZ2llLmNvbSIsInZlciI6IjEuMCJ9.vZO7a5Vs0G_g92Bb00BPKcLuF9WmrqfLjwbLhz8xEe3OfqfthWHqh_jzf_Md88INc4ZuMqOMPhWZTZjQMgCACIpTiHDpFRkokZ-jqC09BaQSSjwV_27b-zy-m6CZcFtdUe10LIBQEqiL9JnZlVIrBgFqr49bKBvZKr3uuaoeiuR2XcC0U2klYkDr3CYIexX0w57lvD5Ow0xKkdWKYVswcJipenU9PP63R0wNXr-8cb-6PGIUzaQDREo-EuR2e3uShF9u5cagG7emt9fDmJr8eGxBJU9ppRoffJpuaYeJiIg1F_n0iK7hENnIjZVnHjFn46DZO-RPse8YZjd4YBuKsg"
        (jwt_header, jwt_body, jwt_sign) = encoded.split('.')
        json_str_header = base64.b64decode(jwt_header).decode('unicode_escape')
        json_header = json.loads(json_str_header)
        kid = json_header['kid']
        body_str_json = base64.b64decode(jwt_body).decode('unicode_escape')
        body_json = json.loads(body_str_json)
        self.assertEqual(body_json['upn'].split('@')[0], 'BIF590')

        keys_str_json = open(os.path.join(os.path.dirname(__file__), 'discovery.json'), 'r').read()
        keys_json = json.loads(keys_str_json)

        expected_cer_in = "MIIDBTCCAe2gAwIBAgIQY4RNIR0dX6dBZggnkhCRoDANBgkqhkiG9w0BAQsFADAtMSswKQYDVQQDEyJhY2NvdW50cy5hY2Nlc3Njb250cm9sLndpbmRvd3MubmV0MB4XDTE3MDIxMzAwMDAwMFoXDTE5MDIxNDAwMDAwMFowLTErMCkGA1UEAxMiYWNjb3VudHMuYWNjZXNzY29udHJvbC53aW5kb3dzLm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMBEizU1OJms31S/ry7iav/IICYVtQ2MRPhHhYknHImtU03sgVk1Xxub4GD7R15i9UWIGbzYSGKaUtGU9lP55wrfLpDjQjEgaXi4fE6mcZBwa9qc22is23B6R67KMcVyxyDWei+IP3sKmCcMX7Ibsg+ubZUpvKGxXZ27YgqFTPqCT2znD7K81YKfy+SVg3uW6epW114yZzClTQlarptYuE2mujxjZtx7ZUlwc9AhVi8CeiLwGO1wzTmpd/uctpner6oc335rvdJikNmc1cFKCK+2irew1bgUJHuN+LJA0y5iVXKvojiKZ2Ii7QKXn19Ssg1FoJ3x2NWA06wc0CnruLsCAwEAAaMhMB8wHQYDVR0OBBYEFDAr/HCMaGqmcDJa5oualVdWAEBEMA0GCSqGSIb3DQEBCwUAA4IBAQAiUke5mA86R/X4visjceUlv5jVzCn/SIq6Gm9/wCqtSxYvifRXxwNpQTOyvHhrY/IJLRUp2g9/fDELYd65t9Dp+N8SznhfB6/Cl7P7FRo99rIlj/q7JXa8UB/vLJPDlr+NREvAkMwUs1sDhL3kSuNBoxrbLC5Jo4es+juQLXd9HcRraE4U3UZVhUS2xqjFOfaGsCbJEqqkjihssruofaxdKT1CPzPMANfREFJznNzkpJt4H0aMDgVzq69NxZ7t1JiIuc43xRjeiixQMRGMi1mAB75fTyfFJ/rWQ5J/9kh0HMZVtHsqICBF1tHMTMIK5rwoweY0cuCIpN7A/zMOQtoD"
        for key in keys_json['keys']:
            if key['kid'] == kid:
                self.assertEqual(key['x5c'][0], expected_cer_in)
                return

        self.fail()

    def test_None_token_cannot_be_decoded(self):
        with self.assertRaises(ValueError) as cm:
            oauth2helper.token.decode(None)
        self.assertEqual('JWT Token is mandatory.', cm.exception.args[0])

    def test_None_token_cannot_be_validated(self):
        with self.assertRaises(ValueError) as cm:
            oauth2helper.token.validate(None)
        self.assertEqual('JWT Token is mandatory.', cm.exception.args[0])

    def test_empty_token_cannot_be_decoded(self):
        with self.assertRaises(ValueError) as cm:
            oauth2helper.token.decode('')
        self.assertEqual('JWT Token is mandatory.', cm.exception.args[0])

    def test_empty_token_cannot_be_validated(self):
        with self.assertRaises(ValueError) as cm:
            oauth2helper.token.validate('')
        self.assertEqual('JWT Token is mandatory.', cm.exception.args[0])

    def test_invalid_token_cannot_be_decoded(self):
        with self.assertRaises(ValueError) as cm:
            oauth2helper.token.decode('Invalid token')
        self.assertEqual('Invalid JWT Token (header, body and sign must be separated by dots).', cm.exception.args[0])

    def test_invalid_token_cannot_be_validated(self):
        with self.assertRaises(ValueError) as cm:
            oauth2helper.token.validate('Invalid token')
        self.assertEqual('Invalid JWT Token (header, body and sign must be separated by dots).', cm.exception.args[0])

    @unittest.skip('Should be manually executed with a valid token at the time of the execution.')
    def test_rsa_online_auth_no_expiry(self):
        encoded = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImEzUU4wQlpTN3M0bk4tQmRyamJGMFlfTGRNTSIsImtpZCI6ImEzUU4wQlpTN3M0bk4tQmRyamJGMFlfTGRNTSJ9.eyJhdWQiOiIyYmVmNzMzZC03NWJlLTQxNTktYjI4MC02NzJlMDU0OTM4YzMiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yNDEzOWQxNC1jNjJjLTRjNDctOGJkZC1jZTcxZWExZDUwY2YvIiwiaWF0IjoxNDkwNzc5NzEyLCJuYmYiOjE0OTA3Nzk3MTIsImV4cCI6MTQ5MDc4MzYxMiwiYW1yIjpbInB3ZCJdLCJmYW1pbHlfbmFtZSI6IkRlIE1hZXllciIsImdpdmVuX25hbWUiOiJGYWJyaWNlIiwiaXBhZGRyIjoiMTA0LjQ2LjU4LjE0OSIsIm5hbWUiOiJEZSBNYWV5ZXIgRmFicmljZSAoZXh0ZXJuYWwpIiwibm9uY2UiOiI3MzYyQ0FFQS05Q0E1LTRCNDMtOUJBMy0zNEQ3QzMwM0VCQTciLCJvaWQiOiI1YTJmOGQyYS0xNzQ1LTRmNTctOTcwYS03YjIwMzU5YWUyZGMiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTQwOTA4MjIzMy0xNDE3MDAxMzMzLTY4MjAwMzMzMC0yODUxNjAiLCJwbGF0ZiI6IjMiLCJzdWIiOiJRcjhNZlAwQk9oRld3WlNoNFZSVEpYeGd3Z19XTFBId193TnBnS1lMQTJVIiwidGlkIjoiMjQxMzlkMTQtYzYyYy00YzQ3LThiZGQtY2U3MWVhMWQ1MGNmIiwidW5pcXVlX25hbWUiOiJCSUY1OTBAZW5naWUuY29tIiwidXBuIjoiQklGNTkwQGVuZ2llLmNvbSIsInZlciI6IjEuMCJ9.vZO7a5Vs0G_g92Bb00BPKcLuF9WmrqfLjwbLhz8xEe3OfqfthWHqh_jzf_Md88INc4ZuMqOMPhWZTZjQMgCACIpTiHDpFRkokZ-jqC09BaQSSjwV_27b-zy-m6CZcFtdUe10LIBQEqiL9JnZlVIrBgFqr49bKBvZKr3uuaoeiuR2XcC0U2klYkDr3CYIexX0w57lvD5Ow0xKkdWKYVswcJipenU9PP63R0wNXr-8cb-6PGIUzaQDREo-EuR2e3uShF9u5cagG7emt9fDmJr8eGxBJU9ppRoffJpuaYeJiIg1F_n0iK7hENnIjZVnHjFn46DZO-RPse8YZjd4YBuKsg"
        json_body, json_header = oauth2helper.token.validate(encoded, verify_expiry=False)
        self.assertEqual('BIF590', oauth2helper.content.user_name(json_body))

    @unittest.skip('Should be manually executed with a valid token at the time of the execution.')
    def test_rsa_online_auth_with_expiry_check(self):
        encoded = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImEzUU4wQlpTN3M0bk4tQmRyamJGMFlfTGRNTSIsImtpZCI6ImEzUU4wQlpTN3M0bk4tQmRyamJGMFlfTGRNTSJ9.eyJhdWQiOiIyYmVmNzMzZC03NWJlLTQxNTktYjI4MC02NzJlMDU0OTM4YzMiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yNDEzOWQxNC1jNjJjLTRjNDctOGJkZC1jZTcxZWExZDUwY2YvIiwiaWF0IjoxNDkwNzc5NzEyLCJuYmYiOjE0OTA3Nzk3MTIsImV4cCI6MTQ5MDc4MzYxMiwiYW1yIjpbInB3ZCJdLCJmYW1pbHlfbmFtZSI6IkRlIE1hZXllciIsImdpdmVuX25hbWUiOiJGYWJyaWNlIiwiaXBhZGRyIjoiMTA0LjQ2LjU4LjE0OSIsIm5hbWUiOiJEZSBNYWV5ZXIgRmFicmljZSAoZXh0ZXJuYWwpIiwibm9uY2UiOiI3MzYyQ0FFQS05Q0E1LTRCNDMtOUJBMy0zNEQ3QzMwM0VCQTciLCJvaWQiOiI1YTJmOGQyYS0xNzQ1LTRmNTctOTcwYS03YjIwMzU5YWUyZGMiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTQwOTA4MjIzMy0xNDE3MDAxMzMzLTY4MjAwMzMzMC0yODUxNjAiLCJwbGF0ZiI6IjMiLCJzdWIiOiJRcjhNZlAwQk9oRld3WlNoNFZSVEpYeGd3Z19XTFBId193TnBnS1lMQTJVIiwidGlkIjoiMjQxMzlkMTQtYzYyYy00YzQ3LThiZGQtY2U3MWVhMWQ1MGNmIiwidW5pcXVlX25hbWUiOiJCSUY1OTBAZW5naWUuY29tIiwidXBuIjoiQklGNTkwQGVuZ2llLmNvbSIsInZlciI6IjEuMCJ9.vZO7a5Vs0G_g92Bb00BPKcLuF9WmrqfLjwbLhz8xEe3OfqfthWHqh_jzf_Md88INc4ZuMqOMPhWZTZjQMgCACIpTiHDpFRkokZ-jqC09BaQSSjwV_27b-zy-m6CZcFtdUe10LIBQEqiL9JnZlVIrBgFqr49bKBvZKr3uuaoeiuR2XcC0U2klYkDr3CYIexX0w57lvD5Ow0xKkdWKYVswcJipenU9PP63R0wNXr-8cb-6PGIUzaQDREo-EuR2e3uShF9u5cagG7emt9fDmJr8eGxBJU9ppRoffJpuaYeJiIg1F_n0iK7hENnIjZVnHjFn46DZO-RPse8YZjd4YBuKsg"
        with self.assertRaises(jwt.ExpiredSignatureError):
            oauth2helper.token.validate(encoded, verify_expiry=True)


if __name__ == '__main__':
    unittest.main()
