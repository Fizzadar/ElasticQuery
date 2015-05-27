# Moving from ElasticQuery v1 to v2

ElasticQuery v2 tries to stick close to the v1 API, however there area a couple of breaking changes to be aware of:

### No kwargs on "field" related values

Example: a term query would change from:

    `Filter.term(field_name='term_value')`

to:

    `Filter.term('field_name', 'term_value')`

This change was made because passing in multiple kwargs will generate an invalid query, and it avoids having to unpack dict objects when field names contain Python reserved characters.

### Renamed methods

These keep ElasticQuery true to the Elasticsearch DSL format.

+ `ElasticQuery.offset` is now `ElasticQuery.from_`
+ `Filter.or_filter` is now `Filter.or_`

### Query string default operator

Is now the same as Elasticsearch, `OR`. Was previousl defaulted to `AND`.

### Queries

+ No more `Filter.string` or `Query.string`
+ No more `Filter.query_string`, wrap `Query.query_string` inside a `Filter.query`
+ The `cache=True` must be included in the `Filter.query` context, not inside `Query.query_string`.
