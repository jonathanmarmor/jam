"""A simple synthesizer for rhythmic unison parts using the sox utility.

install dependencies:

    brew install sox

"""

import os


TEST_MUSIC = [
    (0.16, ['Ab2', 'Ab4', 'B4', 'Eb4']),
    (0.48, ['B2', 'B4', 'Eb4', 'Gb4']),
    (0.16, ['B2', 'B4', 'Eb4', 'Gb4']),
    (0.64, ['E2', 'E4', 'Ab4', 'B4']),
]


def play(music):
    command = make_command(music)
    print command
    os.system(command)


def make_command(music):
    """
    >>> make_command(TEST_MUSIC)
    'play "| sox --volume 0.95 -n -p synth 0.16 pluck Ab2 pluck Ab4 pluck B4 pluck Eb4" "| sox --volume 0.95 -n -p synth 0.48 pluck B2 pluck B4 pluck Eb4 pluck Gb4" "| sox --volume 0.95 -n -p synth 0.16 pluck B2 pluck B4 pluck Eb4 pluck Gb4" "| sox --volume 0.95 -n -p synth 0.64 pluck E2 pluck E4 pluck Ab4 pluck B4";'
    """
    note_commands = ' '.join(make_note_command(duration, pitches) for duration, pitches in music)
    return 'play {};'.format(note_commands)


def make_note_command(duration, pitches, timbre='pluck'):
    """
    >>> make_note_command(0.64, ['E2', 'E4', 'Ab4', 'B4'])
    '"| sox --volume 0.95 -n -p synth 0.64 pluck E2 pluck E4 pluck Ab4 pluck B4"'

    """
    pitch_format = '{timbre} {pitch}'
    pitches_string = ' '.join(pitch_format.format(timbre=timbre, pitch=p) for p in pitches)
    command = '"| sox --volume 0.95 -n -p synth {duration} {pitches_string}"'.format(
        duration=duration,
        pitches_string=pitches_string
    )
    return command


if __name__ == '__main__':
    import doctest
    doctest.testmod()
