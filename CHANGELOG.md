# OAuth2 Helper Changelog #

List all changes in various categories:
* Release notes: Contains all worth noting changes (breaking changes mainly)
* Enhancements
* Bug fixes
* Known issues

## Version 1.1.0 (2018-05-03) ##

### Bug fixes ###

- Handle _ in base64 encoded token.

## Version 1.0.0 (2018-03-05) ##

### Release notes ###

- Drop compatibility with python < 3.6.
- validate optional parameter verify_expiry renamed into verify_exp.
- jwt errors are now thrown instead of ValueError in order for client to catch it easily.

### Enhancements ###

- Every JWT validation option can now be provided as kwargs to validate.

### Bug fixes ###

- Return a user friendly exception in case it is not possible to split token.
- Update dependencies to latest version.
