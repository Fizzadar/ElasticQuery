# ElasticQuery
# File: exception.py
# Desc: ES query builder exceptions


# A base exception
class ElasticQueryException(Exception):
    pass

class NoESClient(ElasticQueryException):
    pass

class NoDocType(ElasticQueryException):
    pass

class NoIndexName(ElasticQueryException):
    pass

class InvalidField(ElasticQueryException):
    pass

class NoQuery(ElasticQueryException):
    pass

class NoFilter(ElasticQueryException):
    pass

class InvalidArg(ElasticQueryException):
    pass
