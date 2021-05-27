#!/usr/bin/env python

from pprint import pprint
import sys

def run(audio_path):
    errprint("Processing '" + audio_path + "'")
    errprint()

def errprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


transcription = run(sys.argv[1])
