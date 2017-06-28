#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.classes.data import Data


class Reply(Data):
    """Sub-class of Data"""

    def __init__(self, data, subject, categorie, source_tweet):
        """Initialisation using super class Data."""
        super(Reply, self).__init__(data, subject, categorie)
        self.source = source_tweet
        self.rp = -10

    def get_source(self):
        """Return ID of the source Tweet."""
        return self.source
