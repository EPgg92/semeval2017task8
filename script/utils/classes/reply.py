#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.classes.data import Data


class Reply(Data):
    """Sub-class of Data"""

    def __init__(self, data, subject, categorie, source_tweet):
        """Initialisation using super class Data."""
        super(Reply, self).__init__(data, subject, categorie)
        self.source = int(source_tweet)

    def __str__(self):
        """Return a good string presentation."""
        return "{}\t{}".format(super(Reply, self).__str__(), str(self.source))

    def get_source(self):
        """Return ID of the source Tweet."""
        return self.source
