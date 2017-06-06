#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Activation
import keras
import numpy as np
import tensorflow as tf


def create_trained_nn(vecs_train, labels_train, epochs=50):
    input_dim = vecs_train.shape[1]
    model = Sequential()
    model.add(Dense(units=100, input_dim=input_dim))
    model.add(Activation('relu'))
    model.add(Dense(units=100))
    model.add(Activation('relu'))
    model.add(Dense(units=20))
    model.add(Activation('softmax'))
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='sgd',
                  metrics=['accuracy'])
    model.fit(vecs_train, labels_train, epochs=epochs, batch_size=32)
    return model


def retrain_model(model, vecs_train, labels_train, epochs=50):
    model.fit(vecs_train, labels_train, epochs=epochs, batch_size=32)
    return model


def convert_label_in_number(labels, list_label):
    return np.array([list_label.index(lab) for lab in labels])


def convert_number_to_label(pred, list_label):
    return [(list_label[x], list_label[y]) for x, y in pred]


def predict_nn(model, vecs_test, labels_test):
    return [(pred, label) for pred, label in zip(
        model.predict_classes(vecs_test), labels_test)]


def main():
    train_vecs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    train_label = np.array([0, 1, 1, 1])
    test_vecs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    test_label = np.array([0, 1, 1, 1])
    model = create_trained_nn(train_vecs, train_label, 100)

    model = retrain_model(model, train_vecs, train_label, 100)
    loss, acc = model.evaluate(test_vecs, test_label)
    print(loss, acc)


if __name__ == '__main__':
    main()
