"""Default parsers to English for backwards compatibility so you can still do

>>> from simple_sentiment_analyzer.parsers import PatternParser

which is equivalent to

>>> from simple_sentiment_analyzer.en.parsers import PatternParser
"""

from simple_sentiment_analyzer.base import BaseParser
from simple_sentiment_analyzer.en.parsers import PatternParser

__all__ = [
    "BaseParser",
    "PatternParser",
]

