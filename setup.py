try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup_keywords

config= {
    'description': 'TTS_proyect',
    'author': 'Brizuela, Nelson Damian',
    'url': '',
    'author_email': 'nelson83mdq@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'package': ['TTS_'],
    'script': [],
    'name': 'TTS_'
}

setup(**config)