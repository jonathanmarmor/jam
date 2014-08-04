"""Utilities for converting pitches between names."""

import math


NOTE_NAMES = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
NOTE_PITCHCLASSES = (0, 2, 4, 5, 7, 9, 11)
NAMES_TO_PITCHCLASSES = dict(zip(NOTE_NAMES, NOTE_PITCHCLASSES))

ACCIDENTALS = {
    'flat': 'b',
    'sharp': '#'
}
ACCIDENTALS_GERMAN = {
    'flat': 'es',
    'sharp': 'is'
}

LILYPOND_OCTAVES = {
    -1: ',,,,',
    0: ",,,",
    1: ",,",
    2: ",",
    3: '',
    4: "'",
    5: "''",
    6: "'''",
    7: "''''",
    8: "'''''",
    9: "''''''",
    10: "'''''''"
}


class PitchException(Exception):
    pass


def name_to_pc(name):
    """Convert pitch names to pitch class numbers.

    >>> name_to_pc('C')
    0
    >>> name_to_pc('C#')
    1
    >>> name_to_pc('Db')
    1
    >>> name_to_pc('Cb')
    11
    >>> name_to_pc('b')
    11
    >>> name_to_pc('Bb')
    10
    >>> name_to_pc('bb')
    10
    >>> name_to_pc('ebb')
    2
    """
    letter, accidental = name[0].upper(), name[1:]
    pc = NAMES_TO_PITCHCLASSES[letter]
    sharps = accidental.count('#')
    flats = accidental.count('b')
    if sharps:
        pc = (pc + sharps) % 12
    elif flats:
        pc = (pc - flats) % 12
    return pc


def pc_to_name(pc, accidental_type='flat'):
    """Convert pitch class numbers to pitch names

    >>> pc_to_name(0)
    'C'
    >>> pc_to_name(1)
    'Db'
    >>> pc_to_name(1, accidental_type='sharp')
    'C#'
    >>> pc_to_name(5)
    'F'

    """
    if pc in NOTE_PITCHCLASSES:
        index = NOTE_PITCHCLASSES.index(pc)
        name = NOTE_NAMES[index]
        return name

    accidental = ''
    if accidental_type == 'flat':
        pc = (pc + 1) % 12
        accidental = 'b'
    elif accidental_type == 'sharp':
        pc = (pc - 1) % 12
        accidental = '#'
    else:
        raise PitchException('accidental_type must be either `sharp` or `flat`')

    index = NOTE_PITCHCLASSES.index(pc)
    name = NOTE_NAMES[index]
    return name + accidental


def pitchspace_to_pitchclass(pitchspace):
    """
    >>> pitchspace_to_pitchclass(60)
    0.0

    >>> pitchspace_to_pitchclass(71)
    11.0

    >>> pitchspace_to_pitchclass(61.5)
    1.5

    """
    return float(pitchspace) % 12


def pitchspace_to_pitchclass_floor(pitchspace):
    """
    >>> pitchspace_to_pitchclass_floor(60)
    0

    >>> pitchspace_to_pitchclass_floor(71)
    11

    >>> pitchspace_to_pitchclass_floor(61.5)
    1

    """
    return int(math.floor(pitchspace % 12))


def pitchspace_to_octave(pitchspace):
    """
    >>> pitchspace_to_octave(60)
    4

    """
    return int(math.floor(pitchspace / 12.0)) - 1


def pitchspace_to_cent(pitchspace):
    """
    >>> pitchspace_to_cent(60.5)
    50

    """
    return int(round((pitchspace % 1), 2) * 100)


def pitchspace_to_octave_pitchclass_cent(pitchspace):
    """
    >>> pitchspace_to_octave_pitchclass_cent(60)
    (4, 0, 0)

    >>> pitchspace_to_octave_pitchclass_cent(42.33)
    (2, 6, 33)

    """

    octave = pitchspace_to_octave(pitchspace)
    pitchclass = pitchspace_to_pitchclass_floor(pitchspace)
    cent = pitchspace_to_cent(pitchspace)
    return octave, pitchclass, cent


def octave_pitchclass_cent_to_pitchspace(octave, pitchclass, cent):
    """Convert the octave, pitchclass, and cent of a pitch to a pitchspace number
    >>> octave_pitchclass_cent_to_pitchspace(4, 0, 0)
    60.0

    >>> octave_pitchclass_cent_to_pitchspace(2, 6, 33)
    42.33

    """
    return pitchclass + (cent / 100.0) + ((octave + 1) * 12)


def pitchspace_to_frequency(pitchspace, a440=440.0):
    """
    >>> pitchspace_to_frequency(69)
    440.0

    >>> pitchspace_to_frequency(57)
    220.0

    """
    try:
        frequency = a440 * (2.0 ** (((pitchspace - 60.0) - 9.0) / 12.0))
    except OverflowError:
        frequency = 0
    return frequency


def frequency_to_pitchspace(frequency, a440=440.0):
    """
    >>> frequency_to_pitchspace(440)
    69.0

    >>> frequency_to_pitchspace(220)
    57.0

    """
    return 12 * (math.log(frequency / a440) / math.log(2)) + 69


if __name__ == '__main__':
    import doctest
    doctest.testmod()
