"""
Example: Generate nineeq tones

This example generates individual tones for each nineeq frequency
and saves them as WAV files.
"""

import importlib
import os

_9eq = importlib.import_module('nineeq')
ToneGenerator = _9eq.ToneGenerator
nineeq_FREQS = _9eq.nineeq_FREQS
FREQ_MEANINGS = importlib.import_module('nineeq.config').FREQ_MEANINGS


def main():
    # Create output directory
    output_dir = "generated_tones"
    os.makedirs(output_dir, exist_ok=True)
    
    generator = ToneGenerator()
    
    print("Generating nineeq frequency tones...\n")
    
    for freq in nineeq_FREQS:
        meaning = FREQ_MEANINGS.get(freq, "Unknown")
        filename = f"{output_dir}/nineeq_{freq}hz.wav"
        
        print(f"Generating {freq} Hz - {meaning}")
        generator.save_tone(filename, frequency=freq, duration=10.0)
    
    print(f"\n✅ All tones generated in '{output_dir}/' directory")
    print("Each tone is 10 seconds long")


if __name__ == "__main__":
    main()
