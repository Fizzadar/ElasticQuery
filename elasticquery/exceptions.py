# ElasticQuery
# File: exception.py
# Desc: ES query builder exceptions


class QueryError(ValueError):
    pass


class NoQueryError(QueryError):
    pass


class NoAggregateError(QueryError):
    pass


class NoSuggesterError(QueryError):
    pass


class MissingArgError(ValueError):
    pass
