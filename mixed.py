from pydub import AudioSegment
from pydub.playback import play

audio1 = AudioSegment.from_file("./lyric-generation/lyrics_pitched.wav")
audio2 = AudioSegment.from_file("./melody-generation/melody1.wav")

mixed = audio1.overlay(audio2)

mixed.export("mixed.wav", format='wav')
