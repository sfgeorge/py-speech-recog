#!/usr/bin/env python

import speech_recognition
import sys

def run(audio_path):
    errprint("Processing '" + audio_path + "'")
    errprint()
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)  # read the entire audio file

    transcription = process_audio_data(audio_data = audio_data, recognizer = recognizer)

    return transcription

def errprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def process_audio_data(audio_data, recognizer):
    # recognize speech using Sphinx
    try:
       transcription = recognizer.recognize_sphinx(audio_data)
       print(transcription)
       return transcription
    except speech_recognition.UnknownValueError:
        print("Sphinx could not understand audio")
    except speech_recognition.RequestError as e:
        print("Sphinx error; {0}".format(e))

transcription = run(sys.argv[1])
