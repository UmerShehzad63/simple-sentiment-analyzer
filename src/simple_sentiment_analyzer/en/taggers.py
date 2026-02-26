"""Parts-of-speech tagger implementations."""

import nltk

import simple_sentiment_analyzer as tb
from simple_sentiment_analyzer.base import BaseTagger
from simple_sentiment_analyzer.decorators import requires_nltk_corpus
from simple_sentiment_analyzer.en import tag as pattern_tag


class PatternTagger(BaseTagger):
    """Tagger that uses the implementation in
    Tom de Smedt's pattern library
    (http://www.clips.ua.ac.be/pattern).
    """

    def tag(self, text, tokenize=True):
        """Tag a string or BaseBlob."""
        if not isinstance(text, str):
            text = text.raw
        return pattern_tag(text, tokenize)


class NLTKTagger(BaseTagger):
    """Tagger that uses NLTK's standard TreeBank tagger.
    NOTE: Requires numpy. Not yet supported with PyPy.
    """

    @requires_nltk_corpus
    def tag(self, text):
        """Tag a string or BaseBlob."""
        if isinstance(text, str):
            text = tb.SimpleSentimentAnalyzer(text)

        return nltk.tag.pos_tag(text.tokens)

