try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Nmap Query Utility',
    'author': 'John Bielich',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'jbielich@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['nmapquery'],
    'scripts': [],
    'name': 'nmapquery'
}

setup(**config)
