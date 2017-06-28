#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.function as futils


def recurs_struc(dic_input, dic_output={}):
    for key in dic_input:
        branch = dic_input[key]
        recurs_struc(branch, dic_output)
        for sKey in dic_input[key]:
            dic_output[sKey] = key
    return dic_output


def direct_struc():
    dic_output = {}
    structures = futils.open_json("../dataset/traindev/structures.json")
    for id_tweet in structures:
        dic_input = futils.open_json("{}{}".format(
            "../dataset/rumoureval-data/", structures[id_tweet]))
        dic_output = recurs_struc(dic_input, dic_output)
    return dic_output


def main():
    # aa = futils.open_json(
    #    "../dataset/rumoureval-data/charliehebdo/552783667052167168/structure.json")
    # a = {1: {3: {5: [], 7: []}, 2: {4: {6: {8: []}}}}}
    # b = {}
    # recurs_struc(a, b)
    # print(b)
    futils.create_json(
        "../dataset/traindev/direct_structures.json", direct_struc())


if __name__ == '__main__':
    main()
