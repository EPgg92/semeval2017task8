#!/usr/bin/env python3

"""Function to do mesure."""

from collections import defaultdict as dd
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import fbeta_score


def create_dic(pred_label):
    """Return a dictionnary of the count of pred and label."""
    dic = dd(lambda: dd(int))
    for pred, label in pred_label:
        dic[pred][label] += 1
    return dic


def conf_tab(pred_label):
    """Return a string of the confusion table."""
    y_label = pd.Series([y for _, y in pred_label], name='Actual')
    y_pred = pd.Series([y for y, _ in pred_label], name='Predicted')
    df_confusion = pd.crosstab(y_label, y_pred, rownames=['R:Actual'],
                               colnames=['C:Predicted'], margins=True)
    return str(df_confusion)


def accuracy(pred_label):
    """Return a string of the accuracy."""
    y_label = [y for _, y in pred_label]
    y_pred = [y for y, _ in pred_label]
    return "Accuracy:\t{}".format(accuracy_score(y_label, y_pred))


def precision(pred_label):
    """Return a string of the precision."""
    y_label = [y for _, y in pred_label]
    y_pred = [y for y, _ in pred_label]
    return "Precision:\t{:.0%}".format(
        precision_score(y_label, y_pred, average='weighted'))


def recall(pred_label):
    """Return a string of the recall."""
    y_label = [y for _, y in pred_label]
    y_pred = [y for y, _ in pred_label]
    return "Recall:\t\t{:.0%}".format(
        recall_score(y_label, y_pred, average='weighted'))


def fscore(pred_label):
    """Return a string of the f-score."""
    y_label = [y for _, y in pred_label]
    y_pred = [y for y, _ in pred_label]
    return "Fscore:\t\t{:.0%}".format(
        fbeta_score(y_label, y_pred, average='weighted', beta=1))


def all_mesure(pred_label):
    """Return a string of all the precedente mesures."""
    return "\n".join([
        conf_tab(pred_label),
        accuracy(pred_label),
        fscore(pred_label),
        precision(pred_label),
        recall(pred_label),
        ""])
