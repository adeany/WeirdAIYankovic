import sox

tfm  = sox.Transformer()
tfm.pitch(3.0)
tfm.build('./pysox/tests/data/input.wav', 'out.wav')

