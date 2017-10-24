import sox
from random import randint

tfm  = sox.Transformer()

#do auto tune here

tfm.build('./out.mp3', 'out.wav')

