# ElasticQuery
# File: setup.py
# Desc: needed

from setuptools import setup


if __name__ == '__main__':
    setup(
        version='3.2',
        name='ElasticQuery',
        description='A simple query builder for Elasticsearch 2',
        author='Nick Barrett',
        author_email='pointlessrambler@gmail.com',
        url='http://github.com/Fizzadar/ElasticQuery',
        package_dir={
            'ElasticQuery': 'elasticquery',
        },
        packages=[
            'elasticquery',
        ],
        install_requires=['six>=1.4.0'],
    )
