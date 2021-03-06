#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.classes.chronometer import Chronometer
import utils.function as futils
import numpy as np
import json
import models.naivebayes as nb
import utils.mesure as ms
import utils.vectorise as vc
import sys


def test_it(hyp):
    print(hyp)
    print("Extraction")
    train_vecs = np.array(futils.open_json(
        "../dataset/my_datasets/{}_train_vecs.json".format(hyp)))
    train_labels = np.array(futils.open_json(
        "../dataset/my_datasets/train_label.json"))
    test_vecs = np.array(futils.open_json(
        "../dataset/my_datasets/{}_dev_vecs.json".format(hyp)))
    test_labels = np.array(futils.open_json(
        "../dataset/my_datasets/dev_label.json"))
    print("Training")
    nb_model = nb.create_nb_model(train_vecs, train_labels)
    pred_label = nb.nb_predict(nb_model, test_vecs, test_labels)
    pred_label = [(vc.convert_map_to_label(p), vc.convert_map_to_label(l))
                  for p, l in pred_label]
    print("\nModel Naive bayes:\n")
    print(ms.all_mesure(pred_label))


def error(hyp):
    print("Please choose one of this corpus:")
    print(hyp)


def main():
    hyp = ["hyp1", "hyp2", "hyp3", "hyp3bis",
           "hyp4", "hyp5", "hyp6", "hyp6bis"]
    if len(sys.argv) > 1:
        if str(sys.argv[1]) not in hyp:
            error(hyp)
        else:
            test_it(sys.argv[1])
    else:
        error(hyp)


if __name__ == '__main__':
    main()
