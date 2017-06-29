#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.classes.chronometer import Chronometer
import utils.function as futils
import numpy as np
import json
import models.neuralnetwork as nn
import utils.mesure as ms
import utils.vectorise as vc
import sys


def test_it(hyp):
    for_graph = []
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
    model = nn.create_trained_nn(train_vecs, train_labels, 1)
    epochs = 1
    loss, acc = model.evaluate(train_vecs, train_labels)
    while acc < 0.95 or epochs < 300:
        for_graph.append((epochs, loss, acc))
        epochs += 1
        nn.retrain_model(model, vecs_train, labels_train, 1)
    pred_label = nn.predict_nn(model, test_vecs, test_labels)
    pred_label = [(vc.convert_map_to_label(p), vc.convert_map_to_label(l))
                  for p, l in pred_label]
    print(ms.all_mesure(pred_label))
    print("Epochs: {}".format(epochs))
    futils.create_json("../tests/for_graph/{}.json".format(hyp), for_graph)


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
