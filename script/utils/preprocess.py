"""Usefull function to preprocess sentences."""

# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import TweetTokenizer
from nltk import ngrams

STOP_WORDS = "~/SE8-2017/script/utils/stop_words.txt"


def __get_stopwords(path_stopwords):
    with open(path_stopwords, 'r') as stream:
        stop_words = stream.read().split("\n")
        return set(stop_words)


def remove_stopwords(sentence,
                     file_stopwords=STOP_WORDS):
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


def convert_to_ngrams_word(sentence, n, sep=" "):
    return [sep.join(ng) for ng in ngrams(sentence, n)]


def convert_to_ngrams_char(sentence, n, sep=""):
    return convert_to_ngrams_word(
        list(sentence), n, sep)


def main():
    sentence = "This is my sentence, it's a bit short; but I still like it"
    print(convert_to_lowercase(sentence))
    print(tokenise(sentence))
    print(remove_stopwords(tokenise(sentence), "utils/stop_words.txt"))
    print(lemmatize(tokenise(sentence)))
    print(convert_to_ngrams_word(lemmatize(tokenise(sentence)), 3))
    print(convert_to_ngrams_char(sentence, 4))


if __name__ == '__main__':
    main()
