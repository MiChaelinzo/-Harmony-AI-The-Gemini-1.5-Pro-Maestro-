# Import necessary libraries
import pyo
import random

# Initialize pyo server
s = pyo.Server().boot()

# Define tempo and time signature
tempo = 120
beats_per_measure = 4
beat_duration = 60 / tempo

# Define scales and chords
major_scale = [0, 2, 4, 5, 7, 9, 11]
minor_scale = [0, 2, 3, 5, 7, 8, 10]
chords = [
    [0, 4, 7],  # Major
    [0, 3, 7],  # Minor
    [0, 4, 8],  # Major 7th
    [0, 3, 6]   # Diminished
]

# Function to generate random notes from a scale
def generate_notes(scale, root_note, num_notes):
    notes = [(root_note + interval) % 12 for interval in scale]
    return [random.choice(notes) for _ in range(num_notes)]

# Create synth objects
lead_synth = pyo.SuperSaw(freq=261.63, detune=0.5, bal=0.7, mul=0.3)
bass_synth = pyo.Sine(freq=130.81, mul=0.4)
pad_synth = pyo.Pad(pad="saw", feedback=0.7, cutoff=6000, mul=0.2)

# Create arpeggiator
arp_tempo = 3  # Arp speed relative to beat
arp_steps = 8
arp_notes = generate_notes(minor_scale, 0, arp_steps)
arp = pyo.Pattern(function=lambda x: arp_notes[x % arp_steps], time=beat_duration/arp_tempo).play()
arp_sound = pyo.SineLoop(freq=arp*12+60, feedback=0.1, mul=0.2).out()

# Create drums with more flexibility
kick_pattern = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0]
snare_pattern = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
hihat_pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def play_drum(pattern, sound):
    for i, step in enumerate(pattern):
        if step == 1:
            sound.play(delay=i*beat_duration)

kick = pyo.Sine(freq=100, mul=0.6)
snare = pyo.Noise(mul=0.4)
hihat = pyo.Noise(mul=0.2)
play_drum(kick_pattern, kick)
play_drum(snare_pattern, snare)
play_drum(hihat_pattern, hihat)

# Start the audio server
s.gui(locals())
