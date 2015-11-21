# ElasticQuery Suggesters API

Note that all Suggester calls can also be passed additional keyword arguments not specified here, but no validation of inputs is done on them.

+ [completion](#method-suggestercompletion)
+ [phrase](#method-suggesterphrase)
+ [term](#method-suggesterterm)

### class: Suggester

##### method: Suggester.completion

```py
Suggester.completion(
    field,
    s=None,
    i=None,
    z=None,
    e=None
)
```

##### method: Suggester.phrase

```py
Suggester.phrase(
    field,
    gram_size=None,
    real_word_error_likelihood=None,
    confidence=None,
    max_errors=None,
    separator=None,
    size=None,
    analyzer=None,
    shard_size=None,
    collate=None
)
```

##### method: Suggester.term

```py
Suggester.term(
    field,
    analyzer=None,
    size=None,
    sort=None,
    suggest_mode=None
)
```
