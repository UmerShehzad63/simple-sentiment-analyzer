"""Default taggers to the English taggers for backwards incompatibility, so you
can still do

>>> from simple_sentiment_analyzer.taggers import NLTKTagger

which is equivalent to

>>> from simple_sentiment_analyzer.en.taggers import NLTKTagger
"""

from simple_sentiment_analyzer.base import BaseTagger
from simple_sentiment_analyzer.en.taggers import NLTKTagger, PatternTagger

__all__ = [
    "BaseTagger",
    "PatternTagger",
    "NLTKTagger",
]

