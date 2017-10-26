import sox
from random import randint

tfm  = sox.Transformer()

tfm.pitch(2.0)
tfm.speed(.8)

tfm.build('previous_out.wav', 'out.wav')

