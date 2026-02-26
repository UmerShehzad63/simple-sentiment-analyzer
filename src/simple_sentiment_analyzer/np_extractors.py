"""Default noun phrase extractors are for English to maintain backwards
compatibility, so you can still do

>>> from simple_sentiment_analyzer.np_extractors import ConllExtractor

which is equivalent to

>>> from simple_sentiment_analyzer.en.np_extractors import ConllExtractor
"""

from simple_sentiment_analyzer.base import BaseNPExtractor
from simple_sentiment_analyzer.en.np_extractors import ConllExtractor, FastNPExtractor

__all__ = [
    "BaseNPExtractor",
    "ConllExtractor",
    "FastNPExtractor",
]

