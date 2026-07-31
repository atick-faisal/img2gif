# 🎬 Welcome to imgif!

> ✨ A playful Python library for converting image sequences into animated GIFs with ease!

Turn your image sequences into delightful animated GIFs with just a few lines of code. Whether you're creating animations from screenshots, visualizing data, or just having fun, `imgif` makes it simple and enjoyable! 🚀

## Features

- 🎨 **Simple API** - Convert images to GIF in just 3 lines of code
- ⚡ **Fast & Efficient** - Built on Pillow for optimal performance
- 🎛️ **Highly Configurable** - Control duration, quality, size, and more
- 💻 **CLI Interface** - Use directly from the command line
- 📝 **Fully Typed** - Complete type annotations for great IDE support
- 🧪 **100% Test Coverage** - Reliable and well-tested
- 🎭 **Rich Output** - Beautiful progress indicators and error messages

## Quick Example

=== "Python API"

    ```python
    from imgif import ImageToGifConverter

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

=== "Command Line"

    ```bash
    # Basic usage
    imgif ./my_images output.gif

    # With options
    imgif ./my_images output.gif --duration 0.5 --loop 0

    # See all options
    imgif --help
    ```

=== "Advanced Config"

    ```python
    from imgif import ImageToGifConverter, GifConfig

    # Create custom configuration
    config = GifConfig(fps=10, loop=0, width=800, optimize=True, maintain_aspect_ratio=True)

    # Convert with config
    converter = ImageToGifConverter()
    converter.convert_with_config("./images", "output.gif", config)
    ```

## Installation

Install imgif using pip:

```bash
pip install imgif
```

For development:

```bash
# Clone the repository
git clone https://github.com/atick-faisal/img2gif.git
cd img2gif

# Install with uv
uv sync
```

## Next Steps

- 📖 [Quick Start Guide](getting-started/quickstart.md) - Get started in 5 minutes
- 🎨 [Examples](getting-started/examples.md) - See what you can create
- 📚 [API Reference](api/converter.md) - Detailed API documentation
- 💻 [CLI Reference](guide/cli.md) - Command-line usage

## Why imgif?

Creating animated GIFs from images shouldn't be complicated. imgif provides a clean, intuitive API that makes GIF creation fun and straightforward, while still offering powerful configuration options for advanced users.

!!! tip "Perfect for"
    - 📸 Creating animations from screenshots
    - 📊 Visualizing data over time
    - 🎮 Game development assets
    - 📱 Social media content
    - 🎓 Educational materials
    - 🎨 Digital art projects

## Community & Support

- 🐛 [Report Issues](https://github.com/atick-faisal/img2gif/issues)
- 💬 [Discussions](https://github.com/atick-faisal/img2gif/discussions)
- 🤝 [Contributing Guide](contributing/development.md)

---

Made with ❤️ and Python 🐍
