"""
Example: Basic real-time visualization

This example shows how to start a simple real-time visualization
of nineeq frequencies from your microphone input.
"""

import importlib
_9eq = importlib.import_module('nineeq')
FrequencyVisualizer = _9eq.FrequencyVisualizer


def main():
    # Create visualizer with default settings
    visualizer = FrequencyVisualizer(mode='bar')
    
    print("Starting nineeq Frequency Visualizer...")
    print("Speak, play music, or use a tone generator near your microphone")
    print("Press Ctrl+C to stop\n")
    
    try:
        visualizer.start()
    except KeyboardInterrupt:
        print("\nStopping...")
        visualizer.stop()


if __name__ == "__main__":
    main()
