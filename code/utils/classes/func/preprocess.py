"""Usefull function to preprocess sentences."""

# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import TweetTokenizer


def __get_stopwords(path_stopwords):
    with open(path_stopwords, 'r') as stream:
        stop_words = stream.read().split("\n")
        return set(stop_words)


def remove_stopwords(sentence,
                     file_stopwords="~/SE8-2017/code/classes/func/stop_words.txt"):
    """Remove stop_words from a sentence."""
    stopwords = __get_stopwords(file_stopwords)
    return [w for w in sentence if w not in stopwords]


def lemmatize(sentence):
    """Lemmatize a sentence."""
    lancaster_stemmer = LancasterStemmer()
    return [lancaster_stemmer.stem(word) for word in sentence]


def tokenise(sentence):
    """Tokenise a sentence."""
    tknzr = TweetTokenizer()
    return tknzr.tokenize(sentence)


def convert_to_lowercase(sentence):
    """Convert to lowercase a sentence."""
    return sentence.lower()
