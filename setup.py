from setuptools import setup

v='0.0.2'

setup(
    name='pyparsers',
    version=v,
    packages=['pyparsers', 'pyparsers.CYK'],
    url='https://github.com/PatrikValkovic/pyparsers',
    license='GNU General Public License v3.0',
    download_url='https://github.com/PatrikValkovic/pyparsers/archive/v' + v + '.tar.gz',
    author='Patrik Valkovic',
    author_email='patrik.valkovic@hotmail.cz',
    description='Parsers for grammpy library',
    install_requires=[
        'grammpy'
    ]
)
