from gtts import gTTS
import os


f = open('input.txt', 'r')


tts = gTTS(text=f.read(), lang='en')
tts.save("out.mp3")
