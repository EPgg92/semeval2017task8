#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.classes.chronometer import Chronometer
import utils.datasets as ds
import utils.vectorise as vc
import utils.mesure as ms
import models.naivebayes as nb
import models.neuralnetwork as nn


def main():
    str0 = ""
    chrono = Chronometer()
    datasets = ds.create_dataset()
    test = ds.get_X_dataset(
        datasets, "../dataset/traindev/rumoureval-subtaskA-dev.json")
    train = ds.get_X_dataset(
        datasets, "../dataset/traindev/rumoureval-subtaskA-train.json")
    train, all_words, freq = vc.vectorise_freq_train(train)
    test = vc.vectorise_freq_test(test, all_words, freq)
    train_vecs, train_labels = vc.get_vec_label(train)
    test_vecs, test_labels = vc.get_vec_label(test)

    nb_model = nb.create_nb_model(train_vecs, train_labels)
    pred_label = nb.nb_predict(nb_model, test_vecs, test_labels)

    str0 += ms.all_mesure(pred_label)

    list_label = sorted(list(set(train_labels)))
    train_labels = nn.convert_label_in_number(train_labels, list_label)
    nn_model = nn.create_trained_nn(train_vecs, train_labels, epochs=40)
    test_labels = nn.convert_label_in_number(test_labels, list_label)

    pred_label = nn.convert_number_to_label(
        nn.predict_nn(nn_model, test_vecs, test_labels), list_label)
    str0 += ms.all_mesure(pred_label)
    print(str0)
    print(chrono.str_flow_out())


if __name__ == '__main__':
    main()
