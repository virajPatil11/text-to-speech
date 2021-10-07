# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:10:39 2021

@author: viraj
"""

def speak(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    text = input("What do you want to make python speak?: ")
    speak(text)