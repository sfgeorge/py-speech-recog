## Requirements

For now, these instructions are tailored to OS X.

    brew install swig git openal-soft

## Installation

    pipenv install

Alternatively, if you prefer really long commands:

    pip install speechrecognition 'git+https://github.com/sfgeorge/pocketsphinx-python@OpenAL-lib-fix#egg=pocketsphinx'

## Usage

    pipenv run python speech_recog.py <AUDIO-FILE-PATH>
