"""Make word inflection default to English. This allows for backwards
compatibility so you can still import text.inflect.

    >>> from simple_sentiment_analyzer.inflect import singularize

is equivalent to

    >>> from simple_sentiment_analyzer.en.inflect import singularize
"""

from simple_sentiment_analyzer.en.inflect import pluralize, singularize

__all__ = [
    "singularize",
    "pluralize",
]

