import sox



tfm  = sox.Transformer()
tfm.pitch(5.0)
tfm.build('./pysox/tests/data/input.wav', 'out.wav')

