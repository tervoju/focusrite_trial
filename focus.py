import soundcard as sc
import numpy

sample_rate = 48000
duration = 5 # 5s

# get a list of all speakers:
speakers = sc.all_speakers()
# get the current default speaker on your system:
default_speaker = sc.default_speaker()
# get a list of all microphones:
mics = sc.all_microphones()
# get the current default microphone on your system:
default_mic = sc.default_microphone()
print(mics)
#[<Microphone Built-in Audio Analog Stereo (2 channels)>, <Microphone Scarlett 2i2 USB Analog Stereo (2 channels)>]
# search for a sound card by substring:
#sc.get_speaker('Scarlett')
#<Speaker Focusrite Scarlett 2i2 (2 channels)>
one_mic = sc.get_microphone('Scarlett')
#<Microphone Focusrite Scalett 2i2 (2 channels)>
# fuzzy-search to get the same results:
# one_speaker = sc.get_speaker('FS2i2')
one_mic = sc.get_microphone('2i2')

#print(default_speaker)
#<Speaker Focusrite Scarlett 2i2 (2 channels)>
 
print(default_mic)
#<Microphone Focusrite Scarlett 2i2 (2 channels)>

# record 5 seconds of audio:
audio_data = default_mic.record(samplerate=sample_rate, numframes=duration*sample_rate)

# alternatively, get a `Recorder` and `Player` object


# Specify the output file name
output_filename = "recorded_audio.txt"

# Save each audio sample on a new line in the text file
with open(output_filename, 'w') as text_file:
    idx = 1
    for sample in audio_data:
        text_file.write(f"{idx, sample[0], sample[1]}\n")
        idx += 1
