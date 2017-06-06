"""Simple chronometer permit to evaluate the time accuracy."""

# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time


class Chronometer():
    """Simple chronometer."""

    def __init__(self):
        """Initialisation."""
        self.start = time.time()

    def rinit(self):
        """Réinitialisation."""
        self.start = time.time()

    def stop(self):
        """Return time flow out since chronometer's departure."""
        return time.time() - self.start

    def str_flow_out(self):
        """Return a nice render for the chrono."""
        return "\nChronometer: {}s".format(round(self.stop(), 2))
