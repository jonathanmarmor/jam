from itertools import groupby
import random


def dither_shuffle(items, property, width=1):
    """Shuffle a list of items attempting to evenly distribute items with the same property.

    http://labs.spotify.com/2014/02/28/how-to-shuffle-songs/
    http://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering

    notes = [
        {'pc': 0},
        {'pc': 0},
        {'pc': 0},
        {'pc': 1},
        {'pc': 1},
        {'pc': 1},
        {'pc': 1},
        {'pc': 2},
        {'pc': 2},
        {'pc': 3},
        {'pc': 3},
    ]
    dither_shuffle(notes, 'pc', width=0.25)

    """
    rv = []
    for _, group in groupby(items, lambda x: x[property]):
        group = list(group)
        random.shuffle(group)

        window = 1.0 / len(group)
        offset = random.random()
        for item in group:
            window_end = offset + (window * width)
            start = random.uniform(offset, window_end) % 1.0
            rv.append((start, item))
            offset = (offset + window) % 1.0
    rv.sort(key=lambda x: x[0])
    return rv
