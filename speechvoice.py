# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 10:40:46 2025

@author: Karthik
"""

import pyttsx3

def speak(text):
        speaker = pyttsx3.init()
        speaker.setProperty('rate',100)
        voices = speaker.getProperty('voices')
        speaker.setProperty('voice',voices[1].id) #for female voice
        speaker.say(text)
        speaker.runAndWait()
    
if __name__=="__main__" :
    a="Hello..How are you..."
    speak(a)
                     