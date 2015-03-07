from setuptools import setup

setup(
    name='jam',
    version='0.0.1',
    description="Jonathan's assorted music utilities",
    author='Jonathan Marmor',
    author_email='jmarmor@gmail.com',
    url='https://github.com/jonathanmarmor/jam',
    packages=['jam'],
    long_description="""
        A class which makes handling MIDI data easy in Python.  Provides methods for extracting and modifying the useful parts of MIDI files.
    """,
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
    ],
    keywords='music',
    license='GPL',
    install_requires=[
        'matplotlib',
    ],
)
