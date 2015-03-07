"""Utilities for choosing things."""

import random


def weighted_choice_lists(weights, options):
    sum_of_weights = sum(weights)
    rand = random.uniform(0, sum_of_weights)
    total = 0
    for item, weight in zip(options, weights):
        total += weight
        if rand < total:
            return item


def weighted_choice(pairs):
    """Choose an item from a list of (item, weight) pairs

    >>> chords = [((0, 4, 7), 10), ((0, 4, 7), 5)]

    """
    weights, options = zip(*pairs)
    return weighted_choice_lists(weights, options)


def weighted_choice_dict(d):
    """Choose a key from a dict using the values as weights.

    Works for collections.Counter using the counts as weights.

    >>> chords = {(0, 4, 7): 10, (0, 4, 7): 5}
    >>> dict_weighted_choice(chords)
    (0, 4, 7)

    """
    return weighted_choice(d.items())


def weighted_choice_list_of_dicts(items, item_key='item', weight_key='weight'):
    """Choose an item from a list of dicts where one of each dict's members is a weight.

    >>> chords = [{'chord': (0, 4, 7), 'count': 10}, {'chord': (0, 4, 7), 'count': 5}]
    >>> list_of_dicts_weighted_choice(chords, item_key='chord', weight_key='count')
    (0, 4, 7)

    """
    pairs = [(i[item_key], i[weight_key]) for i in items]
    return weighted_choice(pairs)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
