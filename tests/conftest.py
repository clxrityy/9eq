"""
Test configuration and fixtures
"""

import pytest
import numpy as np


@pytest.fixture
def sample_audio():
    """Fixture providing sample audio data"""
    duration = 1.0
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    # Generate 528 Hz tone
    return 0.5 * np.sin(2 * np.pi * 528 * t)


@pytest.fixture
def mixed_audio():
    """Fixture providing mixed frequency audio"""
    duration = 1.0
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Mix 396, 528, and 741 Hz
    tone1 = 0.3 * np.sin(2 * np.pi * 396 * t)
    tone2 = 0.5 * np.sin(2 * np.pi * 528 * t)
    tone3 = 0.2 * np.sin(2 * np.pi * 741 * t)
    
    return tone1 + tone2 + tone3


@pytest.fixture
def noise_audio():
    """Fixture providing noise"""
    return np.random.randn(4096) * 0.1
