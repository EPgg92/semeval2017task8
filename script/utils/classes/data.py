#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict as dd
import numpy as np


class Data(object):
    """Superclass Data."""

    def __init__(self, data, subject, categorie):
        """Initialisation."""
        # self.data = data
        self.text = " ".join(data["text"].split())
        self.subject = subject
        self.data_id = data["id"]
        self.categorie = categorie
        self.vector = np.array([])

    def __str__(self):
        """Return a good string presentation."""
        return "\t".join(
            [str(self.data_id),
             self.categorie,
             self.subject,
             self.text])

    def get_text(self):
        """Return the text of the source Tweet or the reply."""
        return self.text

    def get_subject(self):
        """Return the subject of the source Tweet or the reply."""
        return self.subject

    def get_id(self):
        """Return the id of the source Tweet or the reply."""
        return self.data_id

    def set_categorie(self, categorie):
        """Set the categorie of the source Tweet or the reply."""
        self.categorie = categorie

    def get_categorie(self):
        """Return the categorie of the source Tweet or the reply."""
        return self.categorie

    def set_vector(self, vector):
        """Set the vector of the source Tweet or the reply."""
        self.vector = vector

    def get_vector(self):
        """Return the vector of the source Tweet or the reply."""
        return self.vector
