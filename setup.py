from distutils.core import setup

setup(
    name = 'lbry',
    packages = ['lbry'],
    version = '1.0.2',  # Ideally should be same as your GitHub release tag varsion
    description = 'A client wrapper for the LBRY API, using requests module',
    author = 'Simon Stead',
    author_email = 'simonstead@me.com',
    url = 'https://github.com/simonstead/lbry-python',
    download_url = 'https://github.com/simonstead/lbry-python/archive/v1.0.2.tar.gz',
    keywords = ['lbry', 'crypto'],
    classifiers = [],
)
