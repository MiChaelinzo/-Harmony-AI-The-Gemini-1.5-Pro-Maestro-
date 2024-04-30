# -Harmony-AI-The-Gemini-1.5-Pro-Maestro-

Harmony AI is a cutting-edge music creation tool powered by Google's Gemini 1.5 Pro technology. It offers an innovative platform for both amateur and professional musicians to explore new realms.

<img width="454" alt="Screenshot 2024-04-27 173627" src="https://github.com/MiChaelinzo/-Harmony-AI-The-Gemini-1.5-Pro-Maestro-/assets/68110223/ccdddb06-f0d4-45ab-874f-66eeaf6c0db7">
<img width="486" alt="Screenshot 2024-04-27 173651" src="https://github.com/MiChaelinzo/-Harmony-AI-The-Gemini-1.5-Pro-Maestro-/assets/68110223/903c4a3e-3c6b-44f9-89ca-7bbb107fe7fb">

Explanation:
- Import Libraries: We import the pyo library for sound generation and processing.
- Initialize Server: The pyo.Server().boot() command starts the audio server.
- Create Synths: We define different synth objects using pyo's built-in functions:
- lead_synth: A SuperSaw oscillator for the main melody.
- bass_synth: A Sine oscillator for the bassline.
- pad_synth: A Pad synth for atmospheric background sounds.
- arp_synth and arp_sound: A combination of LFO and SineLoop to create an arpeggiated sequence.
- Create Drums:
- beat: A Beat object generates a rhythmic pattern with different levels for kick, snare, and hi-hat.
- kick, snare, and hihat: Each drum sound is created using Sine or Noise oscillators controlled by the beat object.
- Start Audio: The s.gui(locals()) command starts the audio server and opens a graphical user interface to control the parameters of the synths and drums.

Improvements:
- Tempo and Time Signature: Defined tempo and beats_per_measure to calculate beat_duration for precise timing.
- Scales and Chords: Added major_scale, minor_scale, and chords to facilitate melodic and harmonic creation.
- generate_notes Function: This function generates random notes from a specified scale, making it easier to create melodies and arpeggios.
- Arpeggiator: Improved arpeggiator with variable tempo and steps, using the generate_notes function.
- Drums: More flexible drum patterns using lists and a play_drum function to trigger sounds based on the pattern.

<img width="445" alt="Screenshot 2024-04-27 173849" src="https://github.com/MiChaelinzo/-Harmony-AI-The-Gemini-1.5-Pro-Maestro-/assets/68110223/f81de5a8-0dac-473d-816d-6439f31782f0">


ICON:


![_8db0af81-e86a-4f3d-be23-0235be362aa4](https://github.com/MiChaelinzo/-Harmony-AI-The-Gemini-1.5-Pro-Maestro-/assets/68110223/4c91327c-4811-4140-9ece-86185c54bfb3)
