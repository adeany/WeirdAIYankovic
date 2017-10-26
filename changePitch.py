import sox
from random import randint

tfm  = sox.Transformer()

tfm.pitch(0.1)
tfm.speed(1.15)

tfm.build('previous_out.wav', 'out.wav')

