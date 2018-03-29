from setuptools import setup

setup(
    name='lambda_cli',
    version='0.0.1',
    packages=['lambda_cli'],
    #url='https://bitbucket.org/simonasya/lambda-interpreter',
    license='GNU General Public License v3.0',
    author='Patrik Valkovic',
    author_email='patrik.valkovic@hotmail.cz',
    description='Application parse and evaluate lambda expressions',
    install_requires=[
        'grammpy',
        'pyparsers',
        'grammpy-transforms',
        'lambda_interpreter',
        'ply',
    ]
)
