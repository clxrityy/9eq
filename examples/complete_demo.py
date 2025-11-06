"""
Complete Demo: nineeq Frequency Visualizer

This demo showcases all major features:
1. Generate test tones
2. Analyze generated tones
3. Detect frequencies
4. Visualize in real-time
"""

import importlib
import numpy as np
import time

_9eq = importlib.import_module('nineeq')
FrequencyVisualizer = _9eq.FrequencyVisualizer
FrequencyDetector = _9eq.FrequencyDetector
ToneGenerator = _9eq.ToneGenerator
nineeq_FREQS = _9eq.nineeq_FREQS
FREQ_COLORS = _9eq.FREQ_COLORS
FREQ_MEANINGS = importlib.import_module('nineeq.config').FREQ_MEANINGS


def demo_tone_generation():
    """Demo: Generate nineeq tones"""
    print("\n" + "=" * 70)
    print("DEMO 1: Tone Generation")
    print("=" * 70)
    
    generator = ToneGenerator()
    
    # Generate the famous 528 Hz "Miracle" tone
    print("\nGenerating 528 Hz 'Miracle' tone (DNA Repair)...")
    generator.save_tone("demo_528hz.wav", frequency=528, duration=3.0)
    
    # Generate a chord
    print("\nGenerating nineeq chord (all 9 frequencies)...")
    chord = generator.generate_nineeq_chord(duration=2.0)
    
    import soundfile as sf
    sf.write("demo_chord.wav", chord, generator.sample_rate)
    print("✓ Saved to demo_chord.wav")


def demo_frequency_detection():
    """Demo: Detect frequencies in synthesized audio"""
    print("\n" + "=" * 70)
    print("DEMO 2: Frequency Detection")
    print("=" * 70)
    
    detector = FrequencyDetector()
    generator = ToneGenerator()
    
    # Generate test signal with multiple frequencies
    print("\nGenerating test signal with 396 Hz, 528 Hz, and 741 Hz...")
    tone1 = generator.generate_tone(396, duration=1.0, amplitude=0.3)
    tone2 = generator.generate_tone(528, duration=1.0, amplitude=0.5)
    tone3 = generator.generate_tone(741, duration=1.0, amplitude=0.2)
    mixed = tone1 + tone2 + tone3
    
    # Detect frequencies
    print("\nDetecting frequencies...")
    detected = detector.detect_frequencies(mixed)
    normalized = detector.normalize_magnitudes(detected)
    
    # Display results
    print("\nDetection Results:")
    print("-" * 70)
    print(f"{'Frequency':<12} {'Bar':<40} {'Level':<8} {'Meaning'}")
    print("-" * 70)
    
    for freq in nineeq_FREQS:
        magnitude = normalized.get(freq, 0)
        bar_length = int(magnitude * 35)
        bar = "█" * bar_length
        color = FREQ_COLORS.get(freq, '#FFFFFF')
        meaning = FREQ_MEANINGS.get(freq, "")[:25]
        
        print(f"{freq:4d} Hz      {bar:<35} {magnitude:>6.1%}   {meaning}")
    
    print("-" * 70)
    
    # Find dominant frequency
    dominant = detector.get_dominant_frequency(mixed)
    print(f"\n🎵 Dominant frequency: {dominant} Hz - {FREQ_MEANINGS.get(dominant, '')}")


def demo_file_analysis():
    """Demo: Analyze audio file"""
    print("\n" + "=" * 70)
    print("DEMO 3: File Analysis")
    print("=" * 70)
    
    # First generate a test file
    generator = ToneGenerator()
    print("\nGenerating test file with 528 Hz and harmonics...")
    
    # Create a more complex signal
    duration = 2.0
    tone = generator.generate_tone(528, duration, amplitude=0.6)
    
    # Add some harmonics
    harmonic1 = generator.generate_tone(528 * 2, duration, amplitude=0.2)
    harmonic2 = generator.generate_tone(528 * 3, duration, amplitude=0.1)
    
    complex_signal = tone + harmonic1 + harmonic2
    
    import soundfile as sf
    sf.write("demo_complex.wav", complex_signal, generator.sample_rate)
    print("✓ Saved to demo_complex.wav")
    
    # Analyze the file
    print("\nAnalyzing file...")
    visualizer = FrequencyVisualizer()
    visualizer.analyze_file("demo_complex.wav")


def demo_custom_detection():
    """Demo: Custom detection with bandpass filtering"""
    print("\n" + "=" * 70)
    print("DEMO 4: Advanced Detection (Bandpass Filtering)")
    print("=" * 70)
    
    detector = FrequencyDetector()
    generator = ToneGenerator()
    
    # Generate noisy signal
    signal = generator.generate_tone(528, duration=1.0)
    noise = np.random.randn(len(signal)) * 0.1
    noisy_signal = signal + noise
    
    print("\nComparing detection methods on noisy 528 Hz signal...")
    
    # Standard FFT detection
    detected_fft = detector.detect_frequencies(noisy_signal)
    
    # Bandpass filter detection
    magnitude_bp, filtered = detector.detect_with_bandpass(noisy_signal, 528)
    
    print(f"\nFFT Detection:       {detected_fft[528]:.2f}")
    print(f"Bandpass Detection:  {magnitude_bp:.4f}")
    print(f"\nBandpass filtering provides more accurate isolation of specific frequencies.")


def demo_visualization_info():
    """Demo: Display visualization information"""
    print("\n" + "=" * 70)
    print("DEMO 5: Real-time Visualization")
    print("=" * 70)
    
    print("\nAvailable visualization modes:")
    print("  • 'bar'  - Bar chart (default, best for general use)")
    print("  • 'wave' - Waveform + spectrum (advanced visualization)")
    
    print("\nTo start real-time visualization:")
    print("  $ nineeq visualize")
    print("  $ nineeq visualize --mode wave")
    
    print("\nOr in Python:")
    print("  viz = FrequencyVisualizer(mode='bar')")
    print("  viz.start()")
    
    choice = input("\nStart real-time visualization now? (y/n): ").lower()
    if choice == 'y':
        visualizer = FrequencyVisualizer(mode='bar')
        print("\nStarting visualization...")
        print("Play audio near your microphone or use a tone generator app")
        print("Press Ctrl+C to stop\n")
        time.sleep(1)
        
        try:
            visualizer.start()
        except KeyboardInterrupt:
            print("\n✓ Visualization stopped")
            visualizer.stop()


def main():
    """Run all demos"""
    print("\n" + "=" * 70)
    print(" nineeq FREQUENCY VISUALIZER - COMPLETE DEMO")
    print("=" * 70)
    print("\nThis demo will showcase all features of the visualizer:")
    print("  1. Tone Generation")
    print("  2. Frequency Detection")
    print("  3. File Analysis")
    print("  4. Advanced Detection")
    print("  5. Real-time Visualization")
    
    input("\nPress Enter to begin...")
    
    try:
        # Run demos
        demo_tone_generation()
        input("\nPress Enter to continue to next demo...")
        
        demo_frequency_detection()
        input("\nPress Enter to continue to next demo...")
        
        demo_file_analysis()
        input("\nPress Enter to continue to next demo...")
        
        demo_custom_detection()
        input("\nPress Enter to continue to next demo...")
        
        demo_visualization_info()
        
        print("\n" + "=" * 70)
        print(" DEMO COMPLETE!")
        print("=" * 70)
        print("\nGenerated files:")
        print("  • demo_528hz.wav")
        print("  • demo_chord.wav")
        print("  • demo_complex.wav")
        print("\nNext steps:")
        print("  • Try: nineeq visualize")
        print("  • Check: examples/ directory for more scripts")
        print("  • Read: docs/GETTING_STARTED.md for detailed guide")
        print("\n")
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\n\nError during demo: {e}")
        print("Make sure all dependencies are installed: pip install -e .")


if __name__ == "__main__":
    main()
