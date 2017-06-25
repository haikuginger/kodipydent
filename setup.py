from setuptools import setup, find_packages

with open('README.rst') as readme:
    readme = readme.read()

with open('requirements.txt') as req_file:
    requirements = req_file.read().splitlines()

setup(
    name = "kodipydent",
    version = "0.3.1",
    packages = ['kodipydent'],
    author = "Jesse Shapiro",
    author_email = "jesse@jesseshapiro.net",
    long_description = readme,
    keywords = "Kodi JSON-RPC JSONRPC RPC JSON client XBMC",
    url = "https://github.com/haikuginger/kodipydent",
    install_requires = requirements,
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
