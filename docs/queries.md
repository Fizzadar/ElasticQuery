# ElasticQuery Queries API

### `Query.span_or([Query])`

### `Query.terms(field, [])`

### `Query.has_child(type, filter=Filter, query=Query)`

### `Query.span_first(Query)`

### `Query.prefix(field, value, boost=None)`

### `Query.term(field, value, boost=None)`

### `Query.nested(path, Query)`

### `Query.dis_max([Query])`

### `Query.query_string(query, fields=[])`

### `Query.fuzzy_like_this([], like_text)`

### `Query.has_parent(parent_type, filter=Filter, query=Query)`

### `Query.fuzzy(field, value, boost=None, fuzziness=None, prefix_length=None, max_expansions=None)`

### `Query.geo_shape(type=None, coordinates=[])`

### `Query.fuzzy_like_this_field(field, like_text, max_query_terms=None, ignore_tf=None, fuzziness=None, prefix_length=None, boost=None, analyzer=None)`

### `Query.span_multi(Query)`

### `Query.match_all(boost=None)`

### `Query.span_near([Query])`

### `Query.simple_query_string(query, fields=[])`

### `Query.multi_match([], query)`

### `Query.span_term(field, value, boost=None)`

### `Query.regexp(field, value, boost=None, flags=None)`

### `Query.ids([], type=None)`

### `Query.more_like_this([], like_text)`

### `Query.range(gte=None, gt=None, lte=None, lt=None)`

### `Query.bool(must=[Query], must_not=[Query], should=[Query])`

### `Query.common(query)`

### `Query.wildcard(field, value, boost=None)`

### `Query.indices([], query=Query, no_match_query=Query)`

### `Query.filtered(filter=Filter, query=Query)`

### `Query.span_not(include=Query, exclude=Query)`

### `Query.boost(positive=None, negative=None)`

### `Query.constant_score(filter=Filter, query=Query)`

### `Query.match(field, query, operator=None, zero_terms_query=None, cutoff_frequency=None, boost=None)`

### `Query.top_children(type, query=Query)`
