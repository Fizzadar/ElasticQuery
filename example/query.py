# ElasticQuery
# File: example/query.py
# Desc: an ElasticQuery example

from elasticsearch import Elasticsearch
from elasticquery import ElasticQuery, Filter, Query, Aggregate


q = ElasticQuery(
    es=Elasticsearch(),
    index='mapping_test',
    doc_type='doc_mapping'
)

# Filters & queries
q.must(
    Filter.range('field', 0, 500),
    Filter.terms(my_field=['list', 'of', 'terms']),
    Filter.or_filter(
        Filter.string(field='matching string'),
        Filter.raw_string('field: another matching string')
    )
)

# Nested filter/query
q.should(
    Query.nested('nested_document', must=[
        Query.term(field='match')
    ])
)

# Aggregates
q.aggregate('aggregate_name', Aggregate.sum('field_name'))
q.aggregates(
    ('another_aggregate', Aggregate.terms('field_name')),
    ('yet_another_agg', Aggregate.avg('field_name'))
)

if __name__ == '__main__':
    # Print out JSON ready for ES
    print 'JSON', q.json(indent=4)

    # Get the results with provided __es__ client
    # requires mapping_test index setup as with ElasticMapping's example (github.com/Fizzadar/ElasticMapping)
    # print 'GET', q.get()
