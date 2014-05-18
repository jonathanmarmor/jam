NOTE_NAMES = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
NOTE_PITCHCLASSES = (0, 2, 4, 5, 7, 9, 11)
NAMES_TO_PITCHCLASSES = dict(zip(NOTE_NAMES, NOTE_PITCHCLASSES))


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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
