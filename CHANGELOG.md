# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
- Update cryptography to version 2.6.1
- Remove coverage and nose

## [1.5.0] - 2019-02-22
### Added
- Update dependencies to latest version (cryptography 2.5)

## [1.4.0] - 2018-12-14
### Added
- Update dependencies to latest version (requests 2.21.0, cryptography 2.4.2)

## [1.3.0] - 2018-11-16
### Added
- Update dependencies to latest version (requests 2.20.1)

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

[Unreleased]: https://github.tools.digital.engie.com/GEM-Py/oauth2helper/compare/v1.7.0...HEAD
[1.7.0]: https://github.tools.digital.engie.com/GEM-Py/oauth2helper/compare/v1.6.0...v1.7.0
[1.6.0]: https://github.tools.digital.engie.com/GEM-Py/oauth2helper/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.tools.digital.engie.com/GEM-Py/oauth2helper/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.tools.digital.engie.com/GEM-Py/oauth2helper/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.tools.digital.engie.com/GEM-Py/oauth2helper/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.tools.digital.engie.com/GEM-Py/oauth2helper/compare/v1.1.1...v1.2.0
[1.1.1]: https://github.tools.digital.engie.com/GEM-Py/oauth2helper/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.tools.digital.engie.com/GEM-Py/oauth2helper/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.tools.digital.engie.com/GEM-Py/oauth2helper/releases/tag/v1.0.0
