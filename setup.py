from setuptools import setup
import textwrap

setup(
    name='salesforce-oauth2',
    version='0.1',
    author='Nick Catalano',
    packages=['salesforce_oauth2',],
    url='https://github.com/neworganizing/salesforce-oauth2',
    license='APACHE',
    description="A simple implementation of Salesforce's OAuth2 authentication interface.",
    long_description=textwrap.dedent(open('README.rst', 'r').read()),
    install_requires=[
        'requests',
    ],
    keywords = "python salesforce salesforce.com oauth2",
    classifiers=['Development Status :: 4 - Beta', 'Environment :: Console', 'Intended Audience :: Developers', 'Natural Language :: English', 'Operating System :: OS Independent', 'Topic :: Internet :: WWW/HTTP'],
)