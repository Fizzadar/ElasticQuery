# ElasticQuery

A simple query builder for Elasticsearch. Install with `pip install elasticquery`. Uses metod calls and their args/kwargs to generate query/filter/aggregate objects. Outputs dict/json represntation to be passed directly to ES.

### API

+ [Filters]()
+ [Queries]()
+ [Aggregates]()
+ [ElasticQuery]()


## Synopsis

```py
from elasticsearch import Elasticsearch
from elasticquery import ElasticQuery, Filter, Query


q = ElasticQuery(
    es=Elasticsearch(),
    index='mapping_test',
    doc_type='doc_mapping'
)

# -> q.timeout
q.timeout(10)

# -> q.size
q.size(1)

# -> q.from
q.offset(1)

# -> q.filtered_query.filter
q.filter(
    # -> q.filtered_query.filter.bool
    Filter.bool(must=[
        # -> q.filtered_query.filter.bool.must.nested
        Filter.nest('parent_field',
            # -> q.filtered_query.filter.bool.must.nested.term
            Filter.term('field', 'this')
        )
    ], must_not=[
        # -> q.filtered_query.filter.bool.must_not.or_filter
        Filter.any(
            # -> q.filtered_query.filter.bool.must_not.or_filter.term
            Filter.term('another_field', 'trololol'),
            # -> q.filtered_query.filter.bool.must_not.or_filter.query.query_string
            Filter.string('a query string')
        )
    ])
)

# -> q.filtered_query.query
q.query(
    # -> q.filtered_query.query.prefix_match
    Query.prefix_match('prefixed_field', 'matching string')
)

# Print the query
print q.json(indent=4)

# Run & print the result
print q.get()
```


## Naming Differences

ElasticQuery attempts to keep all names and arguments in-line with their ES coutnerparts. Unfortunately a number of key terms are reserved by Python, so ElasticQuery implements the following alternatives:

+ `from` -> `from_` (eg setting query['from'])
+ `or` -> `or_` (eg or_filters)
+ `and` -> `and_` (eg and_filters)


## Testing

+ Create virtualenv
+ `pip install requirements.pip`
+ Run `nosetests`
