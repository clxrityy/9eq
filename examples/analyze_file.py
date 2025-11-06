"""
Example: Analyze an audio file

This example demonstrates how to analyze nineeq frequencies
in a pre-recorded audio file.
"""

import sys
import importlib
_9eq = importlib.import_module('nineeq')
FrequencyVisualizer = _9eq.FrequencyVisualizer


def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_file.py <path_to_audio_file>")
        print("Example: python analyze_file.py meditation.wav")
        return
    
    audio_file = sys.argv[1]
    
    print(f"Analyzing: {audio_file}\n")
    
    # Create visualizer
    visualizer = FrequencyVisualizer()
    
    # Analyze the file
    results = visualizer.analyze_file(audio_file)
    
    print("\nAnalysis complete!")
    print(f"Found {len([v for v in results.values() if v > 1000])} strong frequencies")


if __name__ == "__main__":
    main()
