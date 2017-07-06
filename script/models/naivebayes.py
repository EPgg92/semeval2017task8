#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Naive bayes model propulsed by sklearn."""

from sklearn.naive_bayes import MultinomialNB


def create_nb_model(vecs_train, labels_train):
    """Create a trained naive bayes model."""
    return MultinomialNB().fit(vecs_train, labels_train)


def nb_predict(nb_model, vecs_test, labels_test):
    """Permit to do prediction with naive bayes model."""
    return [(nb_model.predict([x])[0], y) for x, y in zip(
        vecs_test, labels_test)]
