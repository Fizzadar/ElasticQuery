# ElasticQuery
# File: elasticquery/suggesters.py
# Desc: internal ElasticQuery definitions mapping to Elasticsearch suggester objects

from .dsl import BaseSuggester, MetaSuggester
from .exceptions import NoSuggesterError

SUGGESTERS = {
    'term': {
        'args': ('field',),
        'kwargs': ('analyzer', 'size', 'sort', 'suggest_mode')
    },
    'phrase': {
        'args': ('field',),
        'kwargs': (
            'gram_size', 'real_word_error_likelihood', 'confidence', 'max_errors',
            'separator', 'size', 'analyzer', 'shard_size', 'collate'
        )
    },
    'completion': {
        'args': ('field',),
        'kwargs': ('size',)
    },
}


class Suggester(BaseSuggester):
    __metaclass__ = MetaSuggester

    _eq_type = 'suggester'
    _definitions = SUGGESTERS
    _exception = NoSuggesterError
