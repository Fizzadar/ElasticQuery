# ElasticQuery

A _simple_ query builder for Elasticsearch.


## Synopsis

```py
from elasticquery import ElasticQuery, Filter, Query, Aggregate

q = ElasticQuery()

# Filters & queries
q.must(
    Filter.range('field', 0, 500),
    Filter.terms(my_field=['list', 'of', 'terms']),
    Filter.or_filter(
        Query.string(field='matching string'),
        Query.raw_string('field: another matching string')
    )
)

# Nested filter/query
q.should(
    Query.nested('path', must=[
        Query.term(field='match')
    ])
)

# Aggregates
q.aggregate('aggregate_name', Aggregate.sum('field_name'))
q.aggregates(
    ('another_aggregate', Aggregate.terms('field_name')),
    ('yet_another_agg', Aggregate.avg('field_name'))
)

# Print out JSON ready for ES
print q.json(indent=4)
```


## API: ElasticQuery

`q = ElasticQuery()`

### q.json()

Return a json string ready to send to Elasticsearch.

### q.fields(fields)

**fields**: list of fields to return

### q.sort(field, order=False)

Sort the result set by a field, order optional.

### q.must(*Query/Filter)

Search where the `Query`/`Filter` object matches.

### q.should(*Query/Filter)

Search where the `Query`/`Filter` object might matches.

### q.must_not(*Query/Filter)

Search where the `Query`/`Filter` object does not match.

### q.aggregate(name, Aggregate)

Add an `Aggregate` to our search query.

### q.aggregates(*(name, Aggregate))

Shortcut to add multiple of the above.


## Filter

### Filter.nested(path, must=None, should=None, must_not=None)

Adds a nested query.

**musts, shoulds & must_nots**: all lists containing `Query` or `Filter` objects.

### Filter.range(field, gt=None, gte=None, lt=None, lte=None)

### Filter.prefix(**kwargs)

Prefix multiple keys.

### Filter.term(**kwargs)

Search multiple key=>value terms.

### Filter.terms(**kwargs)

Search multiple key=>[values] terms.

### Filter.missing(field)

Filter for missing/null fields.

### Filter.raw_string(string, default_operator='AND')

Adds a raw query string to match against.

### Filter.string(default_operator='AND', **kwargs)

This builds a query string based on `kwargs`. Values can be simple (ints/strings) or lists, in which case they are `OR`'d together.

### Filter.or_filter(*args)

Or the arg filters/queries together.


## Query

The `Query` class inherits from `Filter`, see above for API details.

### Query.mlt(field, match, min_term_frequency=1, max_query_terms=False)

Searches objects where field is similar to the match.


## Aggregate

### Aggregate.sub(aggregate, **aggregates)

Puts **aggregates as sub-aggregats under aggregate.

### Aggregate.sum(field)

Get sum of a field.

### Aggregate.avg(field)

Get the average value across a field.

### Aggregate.min(field)

Get the lowest value of a field.

### Aggregate.max(field)

Get the highest value of a field.

### Aggregate.stats(field)

Get stats on a field.

### Aggregate.extended_stats(field)

Get extended stats on a field.

### Aggregate.missing(field)

Count how many documents are missing a given field.

### Aggregate.value_count(field)

Count how many documents contain a given field.

### Aggregate.histogram(field, interval)

Generate a histogram.

### Aggregate.date_histogram(field, interval='day')

Generate a date histogram.

### Aggregate.terms(field)

Count number of terms on a field.

### Aggregate.nested(path)

Create a nested aggregation (for use with sub aggregates, see Aggregate.sub).

### Aggregate.filter(musts=None, shoulds=None, must_nots=None)

Creates a filtered aggregate (for use with sub aggregates, see Aggregate.sub).
