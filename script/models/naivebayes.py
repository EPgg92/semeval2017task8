#!/usr/bin/env python3
"""
"""
from sklearn.naive_bayes import MultinomialNB


def create_nb_model(vecs_train, labels_train):
    return MultinomialNB().fit(vecs_train, labels_train)


def nb_predict(nb_model, vecs_test, labels_test):
    return [(nb_model.predict([x])[0], y) for x, y in zip(
        vecs_test, labels_test)]
