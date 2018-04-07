# ElasticQuery v3 [![PyPI version](https://badge.fury.io/py/ElasticQuery.svg)](https://pypi.python.org/pypi/ElasticQuery)

A simple query builder for Elasticsearch. Install with `pip install elasticquery`. Uses metod calls and their args/kwargs to generate query/filter/aggregate objects. Outputs dict/json represntation to be passed directly to ES.

+ [Documentation](https://elasticquery.readthedocs.org/en/latest/)
+ [Queries API](https://elasticquery.readthedocs.org/en/latest/queries.html)
+ [Aggregates API](https://elasticquery.readthedocs.org/en/latest/aggregates.html)
+ [Suggesters API](https://elasticquery.readthedocs.org/en/latest/suggesters.html)


## Synopsis

```py
from elasticsearch import Elasticsearch
from elasticquery import ElasticQuery, Filter, Aggregate


# Create a query with our ES index details
q = ElasticQuery(
    es=Elasticsearch(),
    index='mapping_test',
    doc_type='doc_mapping'
)

# Query it!
q.query(
    Query.terms('my_field', ['my', 'terms'])
)

# Aggregate it!
q.aggregate(
    Aggregate.sum('my_agg', 'my_field')
)

# Print the query, then run on ES and print it's output
print q.json(indent=4)
print q.get()
```


## Development/Testing

+ Create virtualenv
+ `pip install -r requirements.pip`
+ Run `nosetests`
