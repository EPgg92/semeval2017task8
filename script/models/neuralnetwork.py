#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Neural network propulsed by Keras and tensorflow."""

from keras.models import Sequential
from keras.layers import Dense, Activation
import keras
import numpy as np
import tensorflow as tf


def create_trained_nn(vecs_train, labels_train, epochs=50):
    """Create a trained neural network model."""
    input_dim = vecs_train.shape[1]
    model = Sequential()
    model.add(Dense(units=100, input_dim=input_dim))
    model.add(Activation('relu'))
    model.add(Dense(units=100))
    model.add(Activation('relu'))
    model.add(Dense(units=4))
    model.add(Activation('softmax'))
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='sgd',
                  metrics=['accuracy'])
    model.fit(vecs_train, labels_train, epochs=epochs, batch_size=32)
    return model


def retrain_model(model, vecs_train, labels_train, epochs=50):
    """Retrain a neural network model."""
    model.fit(vecs_train, labels_train, epochs=epochs, batch_size=32)
    return model


def predict_nn(model, vecs_test, labels_test):
    """Permit to do prediction with neural network model."""
    return [(pred, label) for pred, label in zip(
        model.predict_classes(vecs_test), labels_test)]
