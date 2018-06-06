# ElasticQuery
# File: elasticquery/suggesters.py
# Desc: internal ElasticQuery definitions mapping to Elasticsearch suggester objects

import six

from .dsl import BaseSuggester, MetaSuggester
from .exception import NoSuggester

SUGGESTERS = {
    'term': {
        'args': ('field', ),
        'kwargs': ('analyzer', 'size', 'sort', 'suggest_mode')
    },
    'phrase': {
        'args': ('field', ),
        'kwargs': (
            'gram_size', 'real_word_error_likelihood', 'confidence', 'max_errors',
            'separator', 'size', 'analyzer', 'shard_size', 'collate'
        )
    },
    'completion': {
        'args': ('field', ),
        'kwargs': ('size', )
    }
}


@six.add_metaclass(MetaSuggester)
class Suggester(BaseSuggester):
    _eq_type = 'suggester'
    _definitions = SUGGESTERS
    _exception = NoSuggester
