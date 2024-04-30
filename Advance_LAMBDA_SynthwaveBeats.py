# Import libraries
import pyo
import random

# Initialize pyo server
s = pyo.Server().boot()

# Global parameters
tempo = 120
beats_per_measure = 4
beat_duration = 60 / tempo
measures_per_section = 8

# Define scales, chords, and progressions
major_scale = [0, 2, 4, 5, 7, 9, 11]
minor_scale = [0, 2, 3, 5, 7, 8, 10]
chords = [
    [0, 4, 7],  # Major
    [0, 3, 7],  # Minor
    [0, 4, 8],  # Major 7th
    [0, 3, 6]   # Diminished
]
chord_progressions = [
    [0, 3, 4, 1],  # I - vi - VII - IV
    [0, 4, 1, 5]   # I - V - IV - vi
]

# Function to generate notes from a scale
def generate_notes(scale, root_note, num_notes):
    notes = [(root_note + interval) % 12 for interval in scale]
    return [random.choice(notes) for _ in range(num_notes)]

# Function to generate chords from a progression
def generate_chords(progression, root_note):
    return [[(root_note + i) % 12 for i in chord] for chord in chords[progression]]

# Create synth objects with LFO modulation
lead_synth = pyo.SuperSaw(freq=261.63, detune=0.5, bal=0.7, mul=0.3)
lfo1 = pyo.Sine(freq=0.2, mul=200, add=lead_synth.freq).out()
lead_synth.ctrl([lfo1], "freq")

bass_synth = pyo.Sine(freq=130.81, mul=0.4)
lfo2 = pyo.Sine(freq=0.1, mul=50, add=bass_synth.freq).out()
bass_synth.ctrl([lfo2], "freq")

pad_synth = pyo.Pad(pad="saw", feedback=0.7, cutoff=6000, mul=0.2)
lfo3 = pyo.Sine(freq=0.05, mul=2000, add=pad_synth.cutoff).out()
pad_synth.ctrl([lfo3], "cutoff")

# Arpeggiator function
def create_arp(root_note, scale, steps, tempo_factor):
    notes = generate_notes(scale, root_note, steps)
    arp = pyo.Pattern(
        function=lambda x: notes[x % steps], time=beat_duration / tempo_factor
    ).play()
    return pyo.SineLoop(freq=arp * 12 + 60, feedback=0.1, mul=0.2).out()

# Drum pattern function
def play_drum_pattern(pattern, sound):
    for i, step in enumerate(pattern):
        if step == 1:
            sound.play(delay=i * beat_duration)

# Effects
delay = pyo.Delay(lead_synth, delay=0.25, feedback=0.5, maxdelay=1.0)
reverb = pyo.Freeverb(delay, size=0.8, damp=0.5, bal=0.3).out()

# Song structure functions
def play_section(chords, lead_scale, arp_scale):
    for measure in range(measures_per_section):
        for beat in range(beats_per_measure):
            # Bassline
            bass_synth.freq = chords[measure % len(chords)][0] * 12 + 36
            # Lead melody
            lead_synth.freq = generate_notes(lead_scale, chords[measure % len(chords)][0], 1)[0] * 12 + 60
            # Drums
            play_drum_pattern(kick_pattern, kick)
            play_drum_pattern(snare_pattern, snare)
            play_drum_pattern(hihat_pattern, hihat)
            s.sleep(beat_duration)

def play_verse():
    chords = generate_chords(0, 0)  # I - vi - VII - IV progression in C major
    play_section(chords, minor_scale, minor_scale)

def play_chorus():
    chords = generate_chords(1, 0)  # I - V - IV - vi progression in C major 
    play_section(chords, major_scale, major_scale) 

# Play the song 
play_verse()
play_chorus()
play_verse()
play_chorus()

# Create arpeggiator after drums start 
arp_sound = create_arp(0, minor_scale, 8, 2) 

# Start the audio server
s.gui(locals())
