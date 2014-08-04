"""Utilities for choosing things."""

import random


def weighted_choice(pairs):
    """Choose an item from a list of (item, weight) pairs"""
    weights = [weight for item, weight in pairs]
    sum_of_weights = sum(weights)
    rand = random.uniform(0, sum_of_weights)
    total = 0
    for item, weight in pairs:
        total += weight
        if rand < total:
            return item


def dict_weighted_choice(d):
    """Choose a key from a dict using the values as weights.

    Works for collections.Counter using the counts as weights.

    """
    return weighted_choice(d.items())
