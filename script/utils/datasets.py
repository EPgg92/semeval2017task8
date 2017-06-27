#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict as dd
from utils.classes.data import Data
from utils.classes.reply import Reply
from utils.classes.tweet import Tweet
import utils.function as f


def create_dataset():
    """Create all objects for the datasets."""
    dataset = dd(Data)
    ROOT = "../dataset/rumoureval-data/"
    paths = f.open_json("../dataset/traindev/source-reply.json")
    structure_paths = f.open_json("../dataset/traindev/structures.json")
    for data_path in paths:
        data = f.open_json("{}{}".format(ROOT, paths[data_path]))
        subject, source_tweet, type_rt, _ = paths[data_path].split("/")
        categorie = None
        if type_rt == "source-tweet":
            structure = f.open_json("{}{}".format(
                ROOT, structure_paths[data_path]))
            dataset[data_path] = Tweet(data, subject, categorie, structure)
        if type_rt == "replies":
            dataset[data_path] = Reply(data, subject, categorie, source_tweet)
    return dataset


def get_X_dataset(dataset, X):
    categories = f.open_json(X)
    x_set = []
    for key in categories:
        dataset[key].set_categorie(categories[key])
        elt = dataset[key]
        x_set.append(elt)
    return x_set
