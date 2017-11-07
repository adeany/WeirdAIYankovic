from gtts import gTTS
import os


f = open('lyrics.txt', 'r')


tts = gTTS(text=f.read(), lang='en')
tts.save("lyrics.mp3")
