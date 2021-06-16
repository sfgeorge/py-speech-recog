#!/usr/bin/env python

import speech_recognition
import sys

def run(audio_path):
    errprint("Processing '" + audio_path + "'")
    errprint()

def errprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


transcription = run(sys.argv[1])
