import sox



tfm  = sox.Transformer()
tfm.pitch(5.0)
tfm.build('./marytts/output_wav.wav', 'out.wav')

