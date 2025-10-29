<div align="center"><a href="https://donate.unrwa.org/int/en/general"><img src="https://raw.githubusercontent.com/Safouene1/support-palestine-banner/master/banner-support.svg" alt="Support Palestine" style="width: 100%;"></a></div>
<img width="100%" alt="imgif_banner" src="https://github.com/user-attachments/assets/a8637f6f-70d6-4ec5-b827-c3d836543256" />

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.9--3.14-blue?style=for-the-badge&colorA=363a4f&colorB=8aadf4&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&colorA=363a4f&colorB=a6da95&logo=opensourceinitiative&logoColor=white"/>
    <img src="https://img.shields.io/badge/Tests-Passing-success?style=for-the-badge&colorA=363a4f&colorB=a6da95&logo=githubactions&logoColor=white"/>
    <img src="https://img.shields.io/badge/Coverage-82%25-brightgreen?style=for-the-badge&colorA=363a4f&colorB=eed49f&logo=codecov&logoColor=white"/>
    <img src="https://img.shields.io/badge/PyPI-imgif-orange?style=for-the-badge&colorA=363a4f&colorB=f5a97f&logo=pypi&logoColor=white"/>
    <img src="https://img.shields.io/badge/Docs-ReadTheDocs-blue?style=for-the-badge&colorA=363a4f&colorB=8bd5ca&logo=readthedocs&logoColor=white"/>
</p>

> ✨ A playful Python library for converting image sequences into animated GIFs with ease!

Turn your image sequences into delightful animated GIFs with just a few lines of code. Whether you're creating animations from screenshots, visualizing data, or just having fun, `imgif` makes it simple and enjoyable! 🚀

## 🌟 Features

- 🎨 **Simple API** - Convert images to GIF in just 3 lines of code
- ⚡ **Fast & Efficient** - Built on Pillow for optimal performance
- 🎛️ **Highly Configurable** - Control duration, quality, size, and more
- 💻 **CLI Interface** - Use directly from the command line
- 📝 **Fully Typed** - Complete type annotations for great IDE support
- 🧪 **100% Test Coverage** - Reliable and well-tested
- 🎭 **Rich Output** - Beautiful progress indicators and error messages

## 📦 Installation

```bash
# Using pip
pip install imgif

# Using uv (recommended for development)
uv pip install imgif
```

## 🚀 Quick Start

### Python API

```python
from img2gif import ImageToGifConverter

# Create converter
converter = ImageToGifConverter()

# Convert images to GIF
converter.convert(
    input_dir="./my_images",
    output_path="./output.gif",
    duration=0.5,  # seconds per frame
)

print("🎉 GIF created successfully!")
```

### Command Line

```bash
# Basic usage
imgif ./my_images output.gif

# With options
imgif ./my_images output.gif --duration 0.5 --loop 0

# See all options
imgif --help
```

## 📖 Documentation
<img src="https://img.shields.io/badge/Docs-ReadTheDocs-blue?style=for-the-badge&colorA=363a4f&colorB=8bd5ca&logo=readthedocs&logoColor=white"/>

Full documentation is available at [imgif.readthedocs.io](https://imgif.readthedocs.io)

## 🛠️ Development

### Setup

```bash
# Clone the repository
git clone https://github.com/atick-faisal/img2gif.git
cd img2gif

# Install dependencies using uv
uv sync

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run tests on default Python version
hatch run test:all

# Run tests on all supported Python versions
hatch run test:all

# Run with coverage
hatch run test:cov
```

### Linting & Formatting

```bash
# Check code
ruff check .

# Format code
ruff format .
```

## 🤝 Contributing

Contributions are welcome! Please check out our [Contributing Guide](CONTRIBUTING.md) for details.


## 🙏 Acknowledgments

- Built with [Pillow](https://pillow.readthedocs.io/) 📸
- CLI powered by [click](https://click.palletsprojects.com/) 🖱️
- Beautiful output by [rich](https://rich.readthedocs.io/) 💎


<p align="center"><img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" /></p>
<p align="center"><a href="https://github.com/atick-faisal/Jetpack-Android-Starter/blob/main/LICENSE"><img src="https://img.shields.io/github/license/atick-faisal/Jetpack-Android-Starter?style=for-the-badge&colorA=363a4f&colorB=b7bdf8"/></a></p>
