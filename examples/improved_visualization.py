"""
Example: Improved visualization with smooth gradient display

This example demonstrates the enhanced visualization with:
- Frequency band detection (captures energy around target frequencies)
- Exponential moving average smoothing (reduces jitter)
- Customizable bandwidth and smoothing parameters
"""

import importlib

# Import the nineeq package
_nineeq = importlib.import_module('nineeq')
FrequencyVisualizer = _nineeq.FrequencyVisualizer

# Create visualizer with custom parameters for smooth gradient display
visualizer = FrequencyVisualizer(
    mode='bar',
    smoothing_factor=0.8,  # Higher = smoother (0-1)
    bandwidth=40.0,        # Wider bandwidth captures more energy around target freq
)

print("Starting improved visualization...")
print("Parameters:")
print("  - Smoothing: 0.8 (high smoothing for stable display)")
print("  - Bandwidth: 40 Hz (captures energy in ±20 Hz around each frequency)")
print("\nThis will show:")
print("  - Smoother transitions between frames")
print("  - More stable frequency representation")
print("  - Energy gradients around target frequencies")
print("\nPress Ctrl+C to stop\n")

try:
    visualizer.start()
except KeyboardInterrupt:
    print("\nVisualization stopped")
    visualizer.stop()
