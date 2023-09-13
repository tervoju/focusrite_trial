 import numpy

    >>> print(default_speaker)
    <Speaker Focusrite Scarlett 2i2 (2 channels)>
    >>> print(default_mic)
    <Microphone Focusrite Scarlett 2i2 (2 channels)>

    # record and play back one second of audio:
    data = default_mic.record(samplerate=48000, numframes=48000)
    default_speaker.play(data/numpy.max(data), samplerate=48000)

    # alternatively, get a `Recorder` and `Player` object
    # and play or record continuously:
    with default_mic.recorder(samplerate=48000) as mic, \
          default_speaker.player(samplerate=48000) as sp:
        for _ in range(100):
            data = mic.record(numframes=1024)
            sp.play(data)