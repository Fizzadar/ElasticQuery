# Elastic Query
# File: docs/conf.py
# Desc: minimal Sphinx config

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

source_suffix = '.rst'
master_doc = 'index'

project = 'ElasticQuery'
copyright = '2015, Nick Barrett (Fizzadar)'
author = 'Nick Barrett (Fizzadar)'

version = 'latest'
release = 'latest'

html_theme = 'sphinx_rtd_theme'
