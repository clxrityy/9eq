"""
Example: Custom frequency detection

This example shows how to use the FrequencyDetector class
for custom frequency analysis.
"""

import importlib
import numpy as np

_9eq = importlib.import_module('nineeq')
FrequencyDetector = _9eq.FrequencyDetector
nineeq_FREQS = _9eq.nineeq_FREQS


def main():
    # Create detector
    detector = FrequencyDetector(sample_rate=44100)
    
    # Generate a test signal with multiple frequencies
    sample_rate = 44100
    duration = 2.0
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Create a signal with 528 Hz (DNA repair) and 741 Hz (intuition)
    signal = (
        0.5 * np.sin(2 * np.pi * 528 * t) +
        0.3 * np.sin(2 * np.pi * 741 * t) +
        0.1 * np.random.randn(len(t))  # Add some noise
    )
    
    print("Analyzing test signal containing 528 Hz and 741 Hz...\n")
    
    # Detect frequencies
    detected = detector.detect_frequencies(signal)
    
    # Normalize for display
    normalized = detector.normalize_magnitudes(detected)
    
    # Display results
    print("Detected Frequencies:")
    print("-" * 60)
    for freq in nineeq_FREQS:
        magnitude = normalized.get(freq, 0)
        bar = "█" * int(magnitude * 40)
        percentage = magnitude * 100
        print(f"{freq:4d} Hz | {bar:<40} | {percentage:5.1f}%")
    
    print("-" * 60)
    
    # Find dominant frequency
    dominant = detector.get_dominant_frequency(signal)
    if dominant:
        print(f"\nDominant frequency: {dominant} Hz")
    
    # Use bandpass filtering for more accurate detection
    print("\nUsing bandpass filter for 528 Hz:")
    magnitude, filtered_signal = detector.detect_with_bandpass(signal, 528)
    print(f"RMS Magnitude: {magnitude:.4f}")


if __name__ == "__main__":
    main()
