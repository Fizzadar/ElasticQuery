# ElasticQuery Queries API

Note that all Query calls can also be passed additional keyword arguments not specified here, but no validation of inputs is done on them.

+ [span_or](#method-queryspan_or)
+ [terms](#method-queryterms)
+ [has_child](#method-queryhas_child)
+ [span_first](#method-queryspan_first)
+ [prefix](#method-queryprefix)
+ [term](#method-queryterm)
+ [fuzzy](#method-queryfuzzy)
+ [nested](#method-querynested)
+ [dis_max](#method-querydis_max)
+ [query_string](#method-queryquery_string)
+ [fuzzy_like_this](#method-queryfuzzy_like_this)
+ [has_parent](#method-queryhas_parent)
+ [function_score](#method-queryfunction_score)
+ [geo_shape](#method-querygeo_shape)
+ [fuzzy_like_this_field](#method-queryfuzzy_like_this_field)
+ [span_multi](#method-queryspan_multi)
+ [match_all](#method-querymatch_all)
+ [span_near](#method-queryspan_near)
+ [simple_query_string](#method-querysimple_query_string)
+ [multi_match](#method-querymulti_match)
+ [span_term](#method-queryspan_term)
+ [regexp](#method-queryregexp)
+ [ids](#method-queryids)
+ [more_like_this](#method-querymore_like_this)
+ [range](#method-queryrange)
+ [bool](#method-querybool)
+ [common](#method-querycommon)
+ [wildcard](#method-querywildcard)
+ [indices](#method-queryindices)
+ [filtered](#method-queryfiltered)
+ [span_not](#method-queryspan_not)
+ [boost](#method-queryboost)
+ [constant_score](#method-queryconstant_score)
+ [match](#method-querymatch)
+ [top_children](#method-querytop_children)

### class: Query

##### method: Query.span_or

```py
Query.span_or(
    [Query]
)
```

##### method: Query.terms

```py
Query.terms(
    field,
    [value]
)
```

##### method: Query.has_child

```py
Query.has_child(
    type,
    filter=Filter,
    query=Query
)
```

##### method: Query.span_first

```py
Query.span_first(
    Query
)
```

##### method: Query.prefix

```py
Query.prefix(
    field,
    value,
    boost=None
)
```

##### method: Query.term

```py
Query.term(
    field,
    value,
    boost=None
)
```

##### method: Query.fuzzy

```py
Query.fuzzy(
    field,
    value,
    boost=None,
    fuzziness=None,
    prefix_length=None,
    max_expansions=None
)
```

##### method: Query.nested

```py
Query.nested(
    path,
    Query
)
```

##### method: Query.dis_max

```py
Query.dis_max(
    [Query]
)
```

##### method: Query.query_string

```py
Query.query_string(
    query,
    fields=[]
)
```

##### method: Query.fuzzy_like_this

```py
Query.fuzzy_like_this(
    [fields],
    like_text
)
```

##### method: Query.has_parent

```py
Query.has_parent(
    parent_type,
    filter=Filter,
    query=Query
)
```

##### method: Query.function_score

```py
Query.function_score(
    [functions],
    filter=Filter,
    query=Query
)
```

##### method: Query.geo_shape

```py
Query.geo_shape(
    field,
    type=None,
    coordinates=[]
)
```

##### method: Query.fuzzy_like_this_field

```py
Query.fuzzy_like_this_field(
    field,
    like_text,
    max_query_terms=None,
    ignore_tf=None,
    fuzziness=None,
    prefix_length=None,
    boost=None,
    analyzer=None
)
```

##### method: Query.span_multi

```py
Query.span_multi(
    Query
)
```

##### method: Query.match_all

```py
Query.match_all(
    boost=None
)
```

##### method: Query.span_near

```py
Query.span_near(
    [Query]
)
```

##### method: Query.simple_query_string

```py
Query.simple_query_string(
    query,
    fields=[]
)
```

##### method: Query.multi_match

```py
Query.multi_match(
    [fields],
    query
)
```

##### method: Query.span_term

```py
Query.span_term(
    field,
    value,
    boost=None
)
```

##### method: Query.regexp

```py
Query.regexp(
    field,
    value,
    boost=None,
    flags=None
)
```

##### method: Query.ids

```py
Query.ids(
    [values],
    type=None
)
```

##### method: Query.more_like_this

```py
Query.more_like_this(
    [fields],
    like_text
)
```

##### method: Query.range

```py
Query.range(
    field,
    gte=None,
    gt=None,
    lte=None,
    lt=None
)
```

##### method: Query.bool

```py
Query.bool(
    must=[Query],
    must_not=[Query],
    should=[Query]
)
```

##### method: Query.common

```py
Query.common(
    query
)
```

##### method: Query.wildcard

```py
Query.wildcard(
    field,
    value,
    boost=None
)
```

##### method: Query.indices

```py
Query.indices(
    [indices],
    query=Query,
    no_match_query=Query
)
```

##### method: Query.filtered

```py
Query.filtered(
    filter=Filter,
    query=Query
)
```

##### method: Query.span_not

```py
Query.span_not(
    include=Query,
    exclude=Query
)
```

##### method: Query.boost

```py
Query.boost(
    positive=None,
    negative=None
)
```

##### method: Query.constant_score

```py
Query.constant_score(
    filter=Filter,
    query=Query
)
```

##### method: Query.match

```py
Query.match(
    field,
    query,
    operator=None,
    zero_terms_query=None,
    cutoff_frequency=None,
    boost=None
)
```

##### method: Query.top_children

```py
Query.top_children(
    type,
    query=Query
)
```
