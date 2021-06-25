#!/usr/bin/env python

import speech_recognition
import sys

def run(audio_path):
    errprint("Processing '" + audio_path + "'")
    errprint()
    recognizer = speech_recognition.Recognizer()

    transcription = process_audio_data(audio_data = audio_path, recognizer = recognizer)

    return transcription

def errprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def process_audio_data(audio_data, recognizer):
    # recognize speech using Sphinx
    transcription = recognizer.recognize_sphinx(audio_data)
    print(transcription)
    return transcription

transcription = run(sys.argv[1])
