import sox
from random import randint

tfm  = sox.Transformer()

tfm.pitch(2.0)
tfm.speed(.8)

tfm.build('./out.mp3', 'out.wav')

