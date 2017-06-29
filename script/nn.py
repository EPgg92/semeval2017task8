#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.classes.chronometer import Chronometer
import utils.function as futils
import numpy as np
import json
import models.neuralnetwork as nn
import utils.mesure as ms
import utils.vectorise as vc


def main():
    print("Extraction")
    train_vecs = np.array(futils.open_json(
        "../dataset/my_datasets/hyp2_train_vecs.json"))
    train_labels = np.array(futils.open_json(
        "../dataset/my_datasets/train_label.json"))
    test_vecs = np.array(futils.open_json(
        "../dataset/my_datasets/hyp2_dev_vecs.json"))
    test_labels = np.array(futils.open_json(
        "../dataset/my_datasets/dev_label.json"))
    print("Training")
    model = nn.create_trained_nn(train_vecs, train_labels, epochs=1)
    loss, acc = model.evaluate(test_vecs, test_labels)
    pred_label = nn.predict_nn(model, test_vecs, test_labels)
    pred_label = [(vc.convert_map_to_label(p), vc.convert_map_to_label(l))
                  for p, l in pred_label]
    print(ms.all_mesure(pred_label))


if __name__ == '__main__':
    main()
