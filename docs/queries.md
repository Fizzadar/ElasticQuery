# ElasticQuery Queries API

### span_or

`Query.span_or([Query])`

### terms

`Query.terms(field, [])`

### has_child

`Query.has_child(type, filter=Filter, query=Query)`

### span_first

`Query.span_first(Query)`

### prefix

`Query.prefix(field, value, boost=None)`

### term

`Query.term(field, value, boost=None)`

### nested

`Query.nested(path, Query)`

### dis_max

`Query.dis_max([Query])`

### query_string

`Query.query_string(query, fields=[])`

### fuzzy_like_this

`Query.fuzzy_like_this([], like_text)`

### has_parent

`Query.has_parent(parent_type, filter=Filter, query=Query)`

### fuzzy

`Query.fuzzy(field, value, boost=None, fuzziness=None, prefix_length=None, max_expansions=None)`

### geo_shape

`Query.geo_shape(field, type=None, coordinates=[])`

### fuzzy_like_this_field

`Query.fuzzy_like_this_field(field, like_text, max_query_terms=None, ignore_tf=None, fuzziness=None, prefix_length=None, boost=None, analyzer=None)`

### span_multi

`Query.span_multi(Query)`

### match_all

`Query.match_all(boost=None)`

### span_near

`Query.span_near([Query])`

### simple_query_string

`Query.simple_query_string(query, fields=[])`

### multi_match

`Query.multi_match([], query)`

### span_term

`Query.span_term(field, value, boost=None)`

### regexp

`Query.regexp(field, value, boost=None, flags=None)`

### ids

`Query.ids([], type=None)`

### more_like_this

`Query.more_like_this([], like_text)`

### range

`Query.range(field, gte=None, gt=None, lte=None, lt=None)`

### bool

`Query.bool(must=[Query], must_not=[Query], should=[Query])`

### common

`Query.common(query)`

### wildcard

`Query.wildcard(field, value, boost=None)`

### indices

`Query.indices([], query=Query, no_match_query=Query)`

### filtered

`Query.filtered(filter=Filter, query=Query)`

### span_not

`Query.span_not(include=Query, exclude=Query)`

### boost

`Query.boost(positive=None, negative=None)`

### constant_score

`Query.constant_score(filter=Filter, query=Query)`

### match

`Query.match(field, query, operator=None, zero_terms_query=None, cutoff_frequency=None, boost=None)`

### top_children

`Query.top_children(type, query=Query)`
