# Makefile for 9eq

.PHONY: help install dev-install test clean run demo format lint

help:
	@echo "9eq - Available Commands:"
	@echo ""
	@echo "  make install      - Install package for normal use"
	@echo "  make dev-install  - Install with development dependencies"
	@echo "  make test         - Run unit tests"
	@echo "  make demo         - Run complete demo"
	@echo "  make format       - Format code with black"
	@echo "  make lint         - Check code with flake8"
	@echo "  make clean        - Remove build artifacts"
	@echo "  make run          - Start real-time visualizer"
	@echo ""

install:
	pip install -e .

dev-install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

test-coverage:
	pytest --cov=nineeq --cov-report=html tests/

demo:
	python examples/complete_demo.py

format:
	black nineeq/ examples/ tests/

lint:
	flake8 nineeq/ --max-line-length=100

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf __pycache__
	rm -rf **/__pycache__
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov/
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

run:
	nineeq visualize

generate-tones:
	python examples/generate_tones.py

analyze:
	@echo "Usage: make analyze FILE=path/to/audio.wav"
	@if [ -z "$(FILE)" ]; then \
		echo "Error: Please specify FILE=path/to/audio.wav"; \
	else \
		nineeq analyze $(FILE); \
	fi
