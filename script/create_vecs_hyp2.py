#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.vectorise as vutils
import utils.function as futils
import utils.preprocess as putils


def pp(str0):
    return putils.tokenise(putils.convert_to_lowercase(str0))


def get_label_col(index, var):
    return [v[index] for v in var]


def hyp2_pp(ds):
    return[pp(rp) for rp in get_label_col(3, ds)]


def create_objType(ds):
    return [int(x[0] == x[1]) for x in ds]


def add_objType_to_vec(vecs, objType):
    return [vec + [x] for vec, x in zip(vecs, objType)]


def main():
    print("Extraction")
    lTrain = futils.open_json("../dataset/my_datasets/train.json")
    lDev = futils.open_json("../dataset/my_datasets/dev.json")
    objType_train = create_objType(lTrain)
    objType_Dev = create_objType(lDev)
    print("Preprocessing")
    lTrain = hyp2_pp(lTrain)
    lDev = hyp2_pp(lDev)
    print("Vectorisation")
    lTrain, all_words = vutils.vectorise_train(lTrain)
    lDev = vutils.vectorise_test(lDev, all_words)
    lTrain = add_objType_to_vec(lTrain, objType_train)
    lDev = add_objType_to_vec(lDev, objType_Dev)
    print("Saving")
    futils.create_json("../dataset/my_datasets/hyp2_train_vecs.json",
                       lTrain)
    futils.create_json("../dataset/my_datasets/hyp2_dev_vecs.json",
                       lDev)


if __name__ == '__main__':
    main()
