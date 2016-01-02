"""Utilities for manipulating and processing chords and harmonies

`intervals` in this file always means a list or tuple containing the intervals
    between adjacent pitchclasses, not including the interval between the
    highest pitchclass and the octave. For a major triad, this would be (4, 3)

`pitchclasses` means a list or tuple of the pitchclasses in the chord. A major
    triad would be (0, 4, 7).

"""

from collections import Counter

from misc import ngrams


def intervals_to_relative_pitch_classes(intervals):
    """
    >>> intervals_to_relative_pitch_classes([4])
    (0, 4)
    >>> intervals_to_relative_pitch_classes([4, 3])
    (0, 4, 7)

    """

    pitch_classes = [0]
    total = 0
    for interval in intervals:
        total += interval
        pitch_classes.append(total)
    return tuple(pitch_classes)


def dyad_to_size(dyad):
    """
    >>> dyad_to_size((2, 7))
    5

    """
    higher = max(dyad)
    lower = min(dyad)
    return higher - lower


def get_interval_base_inversion(interval):
    """
    >>> [get_interval_base_inversion(n) for n in range(25)]
    [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]

    >>> get_interval_base_inversion(7)
    5

    >>> get_interval_base_inversion((1, 4))
    3

    """

    if isinstance(interval, (tuple, list)):
        interval = dyad_to_size(interval)

    interval = interval % 12
    if interval > 6:
        interval = 12 - interval

    return interval


def get_interval_content(intervals):
    """Get counts of each interval appearing in a chord
    (m2, M2, m3, M3, P4, TT)

    >>> get_interval_content((4, 3))
    (0, 0, 1, 1, 1, 0)

    >>> get_interval_content((4, 3, 3))
    (0, 1, 2, 1, 1, 1)

    >>> get_interval_content((6, ))
    (0, 0, 0, 0, 0, 1)


    """

    counter = Counter()
    for n in range(1, len(intervals) + 1):
        for gram in ngrams(intervals, n):
            interval = sum(gram)
            interval = get_interval_base_inversion(interval)
            counter[interval] += 1

    return tuple([counter[i] for i in range(1, 7)])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
