import os
from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_dir, 'README'), 'r') as f:
    long_description = f.read()

# More information on properties: https://packaging.python.org/distributing
setup(name='oauth2helper',
      version=open("oauth2helper/_version.py").readlines()[-1].split()[-1].strip("\"'"),
      author='Engie',
      # TODO Provide a support mailbox for our products
      author_email='colin.bounouar@external.engie.com',
      maintainer='Engie',
      # TODO Provide a support mailbox for our products
      maintainer_email='colin.bounouar@external.engie.com',
      url="http://guru.trading.gdfsuez.net/bitbucket/projects/AUT/repos/oauth2",
      description="Provide information on OAuth2",
      long_description=long_description,
      # TODO Package to artifactory and assert that bamboo will keep it up to date
      download_url='http://www.engie.com',
      classifiers=[
          "Development Status :: 3 - Beta",
          "Intended Audience :: Developers"
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Operating System :: Microsoft :: Windows :: Windows 7"
      ],
      keywords=[
          'security',
          'oauth2',
          'jwt'
      ],
      packages=find_packages(exclude=['tests']),
      tests_require=[
          # Used to run tests
          'nose'
      ],
      install_requires=[
          # Used to retrieve keys
          'requests==2.6.0',
          # Used to decode tokens
          'pyjwt',
          # Used to handle certificate
          'cryptography==1.8.1'
      ],
      platforms=[
          'Windows'
      ]
      )
