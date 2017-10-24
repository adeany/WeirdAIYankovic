import sox
from random import randint

tfm  = sox.Transformer()
tfm.pitch(5.0)
tfm.build('./marytts/output_wav.wav', 'out.wav')

