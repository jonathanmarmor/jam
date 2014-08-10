"""Miscellaneous utils."""

import itertools
from collections import Counter


def group(iterable, n):
    """Group items in `iterable` into `n` sized chunks

    >>> list(group(range(4), 3))
    [[0, 1, 2], [3]]

    >>> list(group(range(5), 3))
    [[0, 1, 2], [3, 4]]

    >>> list(group(range(6), 3))
    [[0, 1, 2], [3, 4, 5]]

    """

    chunk = []
    for progress, item in enumerate(iterable):
        chunk.append(item)
        if progress % n == n - 1:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def counter_percentages(counter):
    """
    >>> c = Counter()
    >>> for x in range(5) + range(3):
    ...     c[x] += 1
    >>> counter_percentages(c)
    [(0, 25.0), (1, 25.0), (2, 25.0), (3, 12.5), (4, 12.5)]
    """
    total = float(sum(counter.values()))
    return [(key, round((count / total) * 100, 1)) for key, count in counter.most_common()]


def pairwise(iterable):
    """
    >>> list(pairwise(range(5)))
    [(0, 1), (1, 2), (2, 3), (3, 4)]

    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)


def ngrams(iterable, n):
    """
    >>> list(ngrams(range(6), 3))
    [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]

    """
    for i, item in enumerate(iterable[:-n + 1]):
        yield iterable[i:i + n]


def get_first_item(items, value, key='id'):
    """
    >>> items = [{'c': 'd', 'bacon': 5}, {'a': 'b', 'bacon': 4}]
    >>> get_first_item(items, 4, key='bacon')
    {'a': 'b', 'bacon': 4}

    """
    return next((item for item in items if item.get(key) == value), None)


def get_multiple_items(items, value, key='id'):
    """
    >>> items = [{'c': 'd', 'bacon': 5}, {'a': 'b', 'bacon': 4}, {1: 7, 'bacon': 4}]
    >>> get_multiple_items(items, 4, key='bacon')
    [{'a': 'b', 'bacon': 4}, {1: 7, 'bacon': 4}]

    """
    return [item for item in items if item.get(key) == value]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
