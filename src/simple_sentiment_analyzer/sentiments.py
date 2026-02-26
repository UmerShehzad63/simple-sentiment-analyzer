"""Default sentiment analyzers are English for backwards compatibility, so
you can still do

>>> from simple_sentiment_analyzer.sentiments import PatternAnalyzer

which is equivalent to

>>> from simple_sentiment_analyzer.en.sentiments import PatternAnalyzer
"""

from simple_sentiment_analyzer.base import BaseSentimentAnalyzer
from simple_sentiment_analyzer.en.sentiments import (
    CONTINUOUS,
    DISCRETE,
    NaiveBayesAnalyzer,
    PatternAnalyzer,
)

__all__ = [
    "BaseSentimentAnalyzer",
    "DISCRETE",
    "CONTINUOUS",
    "PatternAnalyzer",
    "NaiveBayesAnalyzer",
]

