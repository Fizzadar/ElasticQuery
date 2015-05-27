# ElasticQuery
# File: setup.py
# Desc: needed

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    version='2.0.1',
    name='ElasticQuery',
    description='A simple query builder for Elasticsearch',
    author='Nick Barrett',
    author_email='pointlessrambler@gmail.com',
    url='http://github.com/Fizzadar/ElasticQuery',
    package_dir={
        'ElasticQuery': 'elasticquery'
    },
    packages=[
        'elasticquery'
    ]
)
