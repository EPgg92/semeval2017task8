#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.classes.data import Data


class Tweet(Data):
    """Sub-class of Data"""

    def __init__(self, data, subject, categorie, structure):
        """Initialisation using super class Data."""
        super(Tweet, self).__init__(data, subject, categorie)
        self.structure = structure
        self.source = self.get_id()

    def get_structure(self):
        """Return ID of the source Tweet."""
        return self.structure

    def get_source(self):
        """Return ID of the source Tweet. Here the same ID"""
        return self.source
