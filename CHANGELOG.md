# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.2.0] - 2019-10-28
### Changed
- Do not use fixed first level dependencies.

### Added
- Allow to provide algorithms, a list of authorized algorithms. Default to `["RS256"]`

## [3.1.0] - 2019-10-21
### Changed
- Update [cryptography](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst) to version 2.8

## [3.0.1] - 2019-08-06
### Fixed
- pytest-responses version is now fixed to 0.4.0.

## [3.0.0] - 2019-08-02
### Changed
- Token validation now requires to supply the identity provider URL. Relying on the one in the token was a security issue.
- A proper error is now raised in case identity provider URL cannot be reached.

## [2.0.0] - 2019-07-23
### Changed
- Update requests to version 2.22.0.
- Add a contributing documentation
- Add License
- Rely on latest version of pytest instead of pytest-cov
- All available functions are exposed via oauth2helper instead of a submodule

## [1.6.0] - 2019-04-11
### Added
- version is now in a public file.

### Changed
- Update [cryptography](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst) to version 2.6.1
- Remove coverage and nose

## [1.5.0] - 2019-02-22
### Added
- Update [cryptography](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst) to version 2.5

## [1.4.0] - 2018-12-14
### Added
- Update requests to version 2.21.0
- Update [cryptography](https://github.com/pyca/cryptography/blob/master/CHANGELOG.rst) to version 2.4.2

## [1.3.0] - 2018-11-16
### Added
- Update requests to version 2.20.1

## [1.2.0] - 2018-09-04
### Added
- Add content.get function to retrieve any value from JSON body.

## [1.1.1] - 2018-08-09
### Fixed
- Update dependencies to latest version.

## [1.1.0] - 2018-05-03
### Fixed
- Handle _ in base64 encoded token.

## [1.0.0] - 2018-03-05
### Changed
- Drop compatibility with python < 3.6.
- validate optional parameter verify_expiry renamed into verify_exp.
- jwt errors are now thrown instead of ValueError in order for client to catch it easily.

### Added
- Every JWT validation option can now be provided as kwargs to validate.

### Fixed
- Return a user friendly exception in case it is not possible to split token.
- Update dependencies to latest version.

[Unreleased]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v3.2.0...HEAD
[3.2.0]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v3.1.0...v3.2.0
[3.1.0]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v3.0.1...v3.1.0
[3.0.1]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v3.0.0...v3.0.1
[3.0.0]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v2.0.0...v3.0.0
[2.0.0]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v1.6.0...v2.0.0
[1.6.0]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v1.1.1...v1.2.0
[1.1.1]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.tools.digital.engie.com/gempy/oauth2helper/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.tools.digital.engie.com/gempy/oauth2helper/releases/tag/v1.0.0
