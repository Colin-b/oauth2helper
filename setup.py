import os
from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_dir, "README.md"), "r") as f:
    long_description = f.read()

setup(
    name="oauth2helper",
    version=open("oauth2helper/version.py").readlines()[-1].split()[-1].strip("\"'"),
    description="Validate and extract information from OAuth2 token.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        # Used to retrieve keys
        "requests==2.22.0",
        # Used to decode tokens
        "pyjwt==1.7.1",
        # Used to handle certificate
        "cryptography==2.7",
    ],
    extras_require={
        "testing": [
            # Used to mock requests
            "pytest-responses==0.4.0"
        ]
    },
    python_requires=">=3.6",
    project_urls={
        "Changelog": "https://github.tools.digital.engie.com/GEM-Py/oauth2helper/blob/master/CHANGELOG.md",
        "Issues": "https://github.tools.digital.engie.com/GEM-Py/oauth2helper/issues",
    },
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Build Tools",
        "Operating System :: Microsoft :: Windows :: Windows 7",
    ],
    keywords=["security", "oauth2", "jwt"],
    platforms=["Windows", "Linux"],
)
