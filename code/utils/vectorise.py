#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from collections import defaultdict as dd
from collections import Counter as ct


def get_vec_label(x_list):
    vecs = []
    labels = []
    for rep_twe in x_list:
        vecs.append(rep_twe.get_vector())
        labels.append(rep_twe.get_categorie())
    return np.array(vecs), labels


def vectorise_train(train):
    all_words = set()
    for rep_twe in train:
        all_words.update(rep_twe.get_text())
    all_words = sorted(list(all_words))
    for rep_twe in train:
        vector = np.zeros(len(all_words))
        for word in rep_twe.get_text():
            vector[all_words.index(word)] += 1
        rep_twe.set_vector(vector)
    return train, all_words


def vectorise_freq_train(train):
    train, all_words = vectorise_train(train)
    _UNK_ = 0.003
    list_cat = dd(list)
    set_cat = dd(set)
    freq = dd(lambda: dd(float))
    for rep_twe in train:
        list_cat[rep_twe.get_categorie()].extend(rep_twe.get_text())
        set_cat[rep_twe.get_categorie()].update(rep_twe.get_text())
    for cat in list_cat:
        count_cat = ct(list_cat[cat])
        deno = len(set_cat[cat])
        for word in all_words:
            if word in list_cat[cat]:
                freq[cat][word] = count_cat[word] / deno
            else:
                freq[cat][word] = _UNK_ / deno
    for rep_twe in train:
        vector = []
        for cat in freq:
            vectorcat = np.zeros(len(all_words))
            for word in rep_twe.get_text():
                vectorcat[all_words.index(word)] = freq[cat][word]
            vector.extend(list(vectorcat))
        rep_twe.set_vector(np.array(vector))
    return train, all_words,  freq


def vectorise_test(test, all_words):
    for rep_twe in test:
        vector = np.zeros(len(all_words))
        for word in rep_twe.get_text():
            if word in all_words:
                vector[all_words.index(word)] += 1
        rep_twe.set_vector(np.append(vector))
    return test


def vectorise_freq_test(test, all_words, freq):
    for rep_twe in test:
        vector = []
        for cat in freq:
            vectorcat = np.zeros(len(all_words))
            for word in rep_twe.get_text():
                if word in all_words:
                    vectorcat[all_words.index(word)] = freq[cat][word]
            vector.extend(list(vectorcat))
        rep_twe.set_vector(np.array(vector))
    return test
