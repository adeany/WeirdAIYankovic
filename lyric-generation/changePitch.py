import sox

tfm  = sox.Transformer()

tfm.pitch(0.1)
tfm.speed(1.15)

tfm.build('./lyrics.mp3', 'lyrics_pitched.wav')
