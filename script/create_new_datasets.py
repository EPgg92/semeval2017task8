#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import utils.function as futils


def get_train_and_test():
    import utils.datasets as ds
    datasets = ds.create_dataset()
    dev = ds.get_X_dataset(
        datasets, "../dataset/traindev/rumoureval-subtaskA-dev.json")
    train = ds.get_X_dataset(
        datasets, "../dataset/traindev/rumoureval-subtaskA-train.json")
    return train, dev


def create_ds_json(path, ds):
    dic_ds = {rp.get_id(): [rp.get_id(), rp.get_source(),
                            rp. get_categorie(), rp.get_text()] for rp in ds}
    list_it = [dic_ds[rp_id] for rp_id in sorted(dic_ds)]
    futils.create_json(path, list_it)


def main():
    train, dev = get_train_and_test()
    create_ds_json("../dataset/my_datasets/train.json", train)
    create_ds_json("../dataset/my_datasets/dev.json", dev)


if __name__ == '__main__':
    main()
