# Import necessary libraries
import pyo

# Initialize pyo server
s = pyo.Server().boot()

# Create synth objects
lead_synth = pyo.SuperSaw(freq=261.63, detune=0.5, bal=0.7, mul=0.3)  # C4
bass_synth = pyo.Sine(freq=130.81, mul=0.4)  # C3
pad_synth = pyo.Pad(pad="saw", feedback=0.7, cutoff=6000, mul=0.2)
arp_synth = pyo.LFO(freq=[3, 2.5, 4], sharp=0.7, type=3, mul=4).play()
arp_notes = pyo.Choice(choice=[0, 4, 7], freq=arp_synth, scale=1)
arp_sound = pyo.SineLoop(freq=arp_notes, feedback=0.1, mul=0.2).out()

# Create drum pattern
beat = pyo.Beat(time=0.5, taps=16, w1=[99, 0, 0, 0, 99, 0, 0, 0, 99, 0, 0, 0, 99, 0, 0, 0],
                w2=[0, 0, 60, 0, 0, 0, 60, 0, 0, 0, 60, 0, 0, 0, 60, 0],
                w3=[30, 0, 0, 0, 0, 30, 0, 0, 30, 0, 0, 0, 0, 30, 0, 0]).play()
kick = pyo.Sine(freq=beat["freq"], mul=beat["amp"]).out()
snare = pyo.Noise(mul=beat["amp2"] * 0.6).out()
hihat = pyo.Noise(mul=beat["amp3"] * 0.3).out()

# Start the audio server
s.gui(locals())
