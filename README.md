## Requirements

For now, these instructions are tailored to OS X.

    brew install swig git openal-soft

## Installation

    pipenv install

Alternatively, if you prefer really long commands:

    pip install speechrecognition 'git+https://github.com/sfgeorge/pocketsphinx-python@OpenAL-lib-fix#egg=pocketsphinx'

## Usage

    pipenv run python speech_recog.py <AUDIO-FILE-PATH>

## Resources

* https://pypi.org/project/SpeechRecognition/
* https://cmusphinx.github.io/wiki/tutorialpocketsphinx/
* https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst
