#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict as dd
from collections import Counter
import matplotlib.pyplot as plt
import os
import json
from pprint import pprint
import time
import numpy as np
import math
# from pybrain.supervised.trainers import *
# from pybrain.structure.modules import SoftmaxLayer


class Chronometer():
    def __init__(self):
        self.start = time.time()

    def stop(self):
        return time.time() - self.start


class Data(object):
    def __init__(self, data=dd(str), subject=""):
        self.data = data
        self.text = data["text"].lower().split()
        self.subject = subject
        self.id = data["id"]

    def set_categorie(self, categorie):
        """Set the categorie of the source Tweet or the reply."""
        self.categorie = categorie


class Tweet(Data):
    def __init__(self, data, subject, categorie, structure):
        super(self.__class__, self).__init__(data, subject)
        self.structure = structure
        self.categorie = categorie


class Reply(Data):
    def __init__(self, data, subject, categorie, source_tweet):
        super(self.__class__, self).__init__(data, subject)
        self.categorie = categorie
        self.source = source_tweet


def openJson(path):
    with open(path) as data_file:
        return json.load(data_file)


def dic2Default(d):
    data = dd(str)
    for key in d.keys():
        data[key] = d[key]
    return data


def create_dataset():
    """Create all objects for the datasets."""
    dataset = dd(Data)

    ROOT = "../semeval2017-task8-dataset/rumoureval-data/"
    paths = openJson(
        "../semeval2017-task8-dataset/rumoureval-data/source-reply.json")
    structure_paths = openJson(
        "../semeval2017-task8-dataset/rumoureval-data/structures.json")
    for data_path in paths:
        data = openJson("{}{}".format(ROOT, paths[data_path]))
        subject, source_tweet, type_rt, _ = paths[data_path].split("/")
        categorie = None
        if type_rt == "source-tweet":
            structure = openJson("{}{}".format(
                ROOT, structure_paths[data_path]))
            dataset[data_path] = Tweet(data, subject, categorie, structure)
        if type_rt == "replies":
            dataset[data_path] = Reply(data, subject, categorie, source_tweet)
    return dataset


def get_X_dataset(dataset, X):
    categories = openJson(X)
    x_set = []
    for key in categories:
        dataset[key].set_categorie(categories[key])
        elt = dataset[key]
        x_set.append(elt)
    return x_set


def getInfo(data, nameSet):
    def createPie(dic, sub=""):
        if sub != "":
            sub = "(Classe: " + sub + ")"
        label = []
        partPie = []
        for cat in sorted(dic.keys()):
            label.append(" ".join((cat, str(dic[cat]))))
            partPie.append(dic[cat])
        plt.figure(figsize=(8, 8))
        plt.pie(
            partPie,
            labels=label,
            autopct=lambda partPie: str(round(partPie)) + '%',
            colors=["#B21262", '#FFE519', '#FF007F', "#14B5CC"],
            # explode=[0.2, 0, 0.1, 0]
        )
        plt.legend()
        plt.title("Pie of the " + nameSet + " set.\n" + sub)
        plt.show()

    def createHisto(word_list, cat, color):
        counts = Counter(word_list)
        labels, values = zip(*counts.items())
        indSort = np.argsort(values)[::-1]
        values = np.array(values)[indSort][:30]
        values = np.array([v / len(labels) for v in values])
        labels = np.array(labels)[indSort][:30]

        indexes = np.arange(len(labels))
        bar_width = 0.75

        plt.bar(indexes, values, bar_width, color=color, align='edge')
        plt.xticks(indexes + bar_width / 2, labels)
        plt.title(cat)
        plt.show()

    count = dd(lambda: dd(int))
    countCatWord = dd(list)
    for r in data:
        count[r.subject][r.categorie] += 1
        countCatWord[r.categorie] += r.text
    countCat = dd(int)
    for sub in sorted(count.keys()):
        for cat in count[sub].keys():
            countCat[cat] += count[sub][cat]
        createPie(count[sub], sub)
    createPie(countCat)
    colors = ["#B21262", '#FFE519', '#FF007F', "#14B5CC"]
    for cat, colors in zip(sorted(countCatWord.keys()), colors):
        createHisto(countCatWord[cat], cat, colors)
    return countCat, countCatWord


def transformVar(countCat, countCatWord, i=0.3):
    deno = sum([countCat[cat] for cat in countCat.keys()])
    probAp = dd(float)
    pW = dd(lambda: dd(float))
    for cat in countCat.keys():
        probAp[cat] = countCat[cat] / deno
        c = Counter(countCatWord[cat])
        denoW = len(countCatWord[cat])
        pW[cat]["_UNK_"] = i / denoW
        for w in c.keys():
            pW[cat][w] = c[w] / denoW

    return probAp, pW


def testing0(test, probAp, pW):
    tConf = dd(lambda: dd(int))
    forScore = {}
    for t in test:
        listposs = list()
        for cat in sorted(probAp.keys()):
            probCat = math.log(probAp[cat])
            for w in t.text:
                probW = pW[cat]["_UNK_"]
                if w in pW[cat]:
                    probW = pW[cat][w]
                probCat += math.log(probW)
            listposs.append((probCat, cat))
        maxCat = sorted(listposs)[-1]
        tConf[t.categorie][maxCat[1]] += 1
        forScore[t.id] = maxCat[1]
        # print(t.categorie, maxCat[1])
    # pprint(tConf)
    return tConf, forScore


def printTConf(tConf):
    def pr(dic0, name):
        str1 = "## " + name + "\n\n|"
        for key in sorted(dic0.keys()):
            str1 += "{:^7}".format(key) + "|"
        str1 += "\n|:-----:|:-----:|:-----:|:-----:|:-----:|\n|"
        for key in sorted(dic0.keys()):
            str1 += "{:^7}".format(str(round(dic0[key] * 100, 2)) + "%") + "|"
        str1 += "\n"
        return str1

    str0 = "## Truth \ Prediction" + "\n\n|"
    for key in ["P \\ T"] + sorted(tConf.keys()):
        str0 += "{:^7}".format(key) + "|"
    str0 += "\n|:-----:|:-----:|:-----:|:-----:|:-----:|\n"
    for truth in sorted(tConf.keys()):
        str0 += "|" + "{:^7}".format(truth) + "|"
        for key in sorted(tConf.keys()):
            str0 += "{:^7}".format(tConf[truth][key]) + "|"
        str0 += "\n"
    str0 += "\n"
    acc = sum([tConf[k1][k2] for k1 in tConf.keys(
    ) for k2 in tConf.keys() if k1 == k2]) / sum(
        [tConf[k1][k2] for k1 in tConf.keys() for k2 in tConf.keys()])
    pre = dd(lambda: 0.1)
    rec = dd(lambda: 0.1)
    fsc = dd(lambda: 0.1)
    for key in tConf.keys():
        rec[key] += tConf[key][key] / sum(
            [tConf[key][k1] for k1 in tConf.keys()])
        pre[key] += tConf[key][key] / sum(
            [tConf[k1][key] for k1 in tConf.keys()])
        fsc[key] = (2 * pre[key] * rec[key]) / (pre[key] + rec[key])
    str0 += pr(pre, "Precision")
    str0 += "\n" + pr(rec, "Recall")
    str0 += "\n" + pr(fsc, "F-score")
    # str0 = ""
    str0 += "\n" + "### Accuracy:\t" + str(round(acc * 100, 2)) + "%"
    return str0


def main():
    chrono = Chronometer()
    dataset = create_dataset()
    test = get_X_dataset(
        dataset, "../semeval2017-task8-dataset/traindev/rumoureval-subtaskA-dev.json")
    train = get_X_dataset(
        dataset, "../semeval2017-task8-dataset/traindev/rumoureval-subtaskA-train.json")
    countCat, countCatWord = getInfo(train, "train")
    probAp, pW = transformVar(countCat, countCatWord, i=0.3)
    tConf, forScore = testing0(test, probAp, pW)
    print(printTConf(tConf))
    print("\nChronometer: " + str(round(chrono.stop(), 2)) + "s")


if __name__ == '__main__':
    main()
