# 📦 Installation

## Requirements

- Python 3.9 or higher 🐍
- pip or uv package manager

## Install from PyPI

The easiest way to install img2gif is from PyPI:

```bash
pip install img2gif
```

This will install img2gif and all required dependencies.

## Install from Source

For development or to get the latest features:

```bash
# Clone the repository
git clone https://github.com/atick-faisal/img2gif.git
cd img2gif

# Using uv (recommended)
uv sync

# Or using pip
pip install -e ".[dev]"
```

## Verify Installation

Check that img2gif is installed correctly:

```bash
# Check version
img2gif --help

# Or in Python
python -c "import img2gif; print(img2gif.__version__)"
```

## Dependencies

img2gif requires the following packages:

- **Pillow** (≥10.0.0) - Image I/O and GIF operations 📸
- **rich** (≥13.7.0) - Beautiful terminal output 💎
- **click** (≥8.1.0) - CLI interface 🖱️

All dependencies are automatically installed.

## Optional Dependencies

For development:

```bash
pip install img2gif[dev]
```

This includes:
- pytest - Testing framework
- pytest-cov - Coverage reporting
- ruff - Linting and formatting
- pre-commit - Git hooks

For documentation:

```bash
pip install img2gif[docs]
```

This includes:
- mkdocs - Documentation generator
- mkdocs-material - Material theme
- pymdown-extensions - Markdown extensions

## Next Steps

Now that you have img2gif installed:

- 🚀 [Quick Start Guide](quickstart.md) - Create your first GIF
- 🎨 [Examples](examples.md) - See what's possible
- 📚 [API Reference](../api/converter.md) - Dive into the details
