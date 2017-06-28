#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.vectorise as vutils
import utils.function as futils


def get_label_col(index, var):
    return [vutils.convert_label_to_map(v[index]) for v in var]


def main():
    lTrain = futils.open_json("../dataset/my_datasets/train.json")
    lDev = futils.open_json("../dataset/my_datasets/dev.json")

    futils.create_json("../dataset/my_datasets/train_label.json",
                       get_label_col(2, lTrain))
    futils.create_json("../dataset/my_datasets/dev_label.json",
                       get_label_col(2, lDev))


if __name__ == '__main__':
    main()
