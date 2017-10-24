import sox
from random import randint

tfm  = sox.Transformer()

tfm.bend(5, [1,5,10,15,20], [3,8,14,19,24], [-5, 15, -3, 10, 5], 80, 32)
tfm.phaser()
tfm.flanger()
tfm.build('./marytts/output_wav.wav', 'result.wav')

