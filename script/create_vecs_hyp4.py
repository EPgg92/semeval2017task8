#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.vectorise as vutils
import utils.function as futils
import utils.preprocess as putils


def hyp1_pp(str0):
    return putils.convert_to_ngrams_char(putils.convert_to_lowercase(str0), 3)


def get_label_col(index, var):
    return [hyp1_pp(v[index]) for v in var]


def main():
    print("Extraction")
    lTrain = futils.open_json("../dataset/my_datasets/train.json")
    lDev = futils.open_json("../dataset/my_datasets/dev.json")
    print("Preprocessing")
    lTrain = get_label_col(3, lTrain)
    lDdev = get_label_col(3, lDev)
    print("Vectorisation")
    lTrain, all_words = vutils.vectorise_train(lTrain)
    lDdev = vutils.vectorise_test(lDev, all_words)
    print("Saving")
    futils.create_json("../dataset/my_datasets/hyp1_train_vecs.json",
                       lTrain)
    futils.create_json("../dataset/my_datasets/hyp1_dev_vecs.json",
                       lDdev)


if __name__ == '__main__':
    main()
