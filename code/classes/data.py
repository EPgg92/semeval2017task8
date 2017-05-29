#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict as dd


class Data(object):
    """Superclass Data."""

    def __init__(self, data=dd(str), subject="", categorie=""):
        """Initialisation."""
        self.data = data
        self.text = data["text"].lower().split()
        self.subject = subject
        self.data_id = data["id"]
        self.categorie = categorie

    def get_text(self):
        """Return the text of the source Tweet or the reply."""
        return self.text

    def get_subject(self):
        """Return the subject of the source Tweet or the reply."""
        return self.subject

    def get_id(self):
        """Return the id of the source Tweet or the reply."""
        return self.data_id

    def get_categorie(self):
        """Return the categorie of the source Tweet or the reply."""
        return self.categorie
