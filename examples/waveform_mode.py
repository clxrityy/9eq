"""
Example: Waveform visualization mode

This example demonstrates the waveform visualization mode,
which shows both the time-domain waveform and frequency spectrum.
"""

import importlib
_9eq = importlib.import_module('nineeq')
FrequencyVisualizer = _9eq.FrequencyVisualizer


def main():
    # Create visualizer in waveform mode
    visualizer = FrequencyVisualizer(
        mode='wave',
        buffer_size=8192,  # Larger buffer for smoother waveform
    )
    
    print("Starting Waveform Visualization...")
    print("This mode shows both the audio waveform and frequency spectrum")
    print("Press Ctrl+C to stop\n")
    
    try:
        visualizer.start()
    except KeyboardInterrupt:
        print("\nStopping...")
        visualizer.stop()


if __name__ == "__main__":
    main()
