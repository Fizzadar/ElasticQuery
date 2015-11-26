# ElasticQuery
# File: exception.py
# Desc: ES query builder exceptions


# A base exception
class ElasticQueryException(Exception):
    pass


# ES querying exceptions
class NoESClient(ElasticQueryException):
    pass

class NoDocType(ElasticQueryException):
    pass

class NoIndexName(ElasticQueryException):
    pass


# Missing DSL object exceptions
class DslException(ElasticQueryException):
    pass

class NoQuery(DslException):
    pass

class NoFilter(DslException):
    pass

class NoAggregate(DslException):
    pass

class NoSuggester(DslException):
    pass


# Invalid DSL argument exceptions
class InvalidArg(DslException):
    pass

class MissingArg(DslException):
    pass
