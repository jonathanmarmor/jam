"""Utilities for choosing things."""

import random


def weighted_choice_lists(weights, options):
    """Choose an item from options using weights

    >>> weighted_choice_lists([100000, 0.000001], [1, 2])
    1

    """
    sum_of_weights = sum(weights)
    rand = random.uniform(0, sum_of_weights)
    total = 0
    for item, weight in zip(options, weights):
        total += weight
        if rand < total:
            return item


def weighted_choice(pairs):
    """Choose an item from a list of (item, weight) pairs

    >>> pairs = [(1, 10000), (2, 0.000001)]
    >>> weighted_choice(pairs)
    1

    """
    options, weights = zip(*pairs)
    return weighted_choice_lists(weights, options)


def weighted_choice_dict(d):
    """Choose a key from a dict using the values as weights.

    Works for collections.Counter using the counts as weights.

    >>> chords = {(0, 4, 7): 10000, (0, 1, 2): 0.000001}
    >>> weighted_choice_dict(chords)
    (0, 4, 7)

    """
    return weighted_choice(d.items())


def weighted_choice_list_of_dicts(items, item_key='item', weight_key='weight'):
    """Choose an item from a list of dicts where one of each dict's members is a weight.

    >>> chords = [{'chord': (0, 4, 7), 'count': 10}, {'chord': (0, 4, 7), 'count': 5}]
    >>> weighted_choice_list_of_dicts(chords, item_key='chord', weight_key='count')
    (0, 4, 7)

    """
    pairs = [(i[item_key], i[weight_key]) for i in items]
    return weighted_choice(pairs)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
