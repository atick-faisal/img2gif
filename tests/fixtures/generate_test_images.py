"""Generate test images using Pillow for testing img2gif.

This script can be run standalone to generate test images, or called from pytest
fixtures. It creates simple, distinguishable test images in various formats.

NOTE: This script is intended to be temporary and can be removed once real-world
test images are provided. To replace with real images:
1. Add your test images to the tests/fixtures/ directory
2. Update tests/conftest.py to use your images instead of generated ones
3. Delete this script
"""

from pathlib import Path
from typing import List

from PIL import Image, ImageDraw, ImageFont


def generate_basic_sequence(
    output_dir: Path,
    count: int = 5,
    size: tuple[int, int] = (200, 200),
    prefix: str = "frame",
) -> List[Path]:
    """Generate a basic sequence of test images with changing colors.

    Args:
        output_dir: Directory to save images.
        count: Number of frames to generate.
        size: Image size as (width, height).
        prefix: Filename prefix.

    Returns:
        List of paths to generated images.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = []

    colors = [
        (255, 100, 100),  # Red
        (100, 255, 100),  # Green
        (100, 100, 255),  # Blue
        (255, 255, 100),  # Yellow
        (255, 100, 255),  # Magenta
    ]

    for i in range(count):
        # Create image with solid color background
        color = colors[i % len(colors)]
        img = Image.new("RGB", size, color=color)

        # Draw frame number
        draw = ImageDraw.Draw(img)
        text = str(i + 1)

        # Draw text in center (white with black outline for visibility)
        text_bbox = draw.textbbox((0, 0), text, font=None)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        x = (size[0] - text_width) // 2
        y = (size[1] - text_height) // 2

        # Black outline
        for dx in [-2, 0, 2]:
            for dy in [-2, 0, 2]:
                draw.text((x + dx, y + dy), text, fill=(0, 0, 0))

        # White text
        draw.text((x, y), text, fill=(255, 255, 255))

        # Save image
        path = output_dir / f"{prefix}_{i+1:03d}.png"
        img.save(path)
        paths.append(path)

    return paths


def generate_different_formats(
    output_dir: Path,
    size: tuple[int, int] = (150, 150),
) -> dict[str, Path]:
    """Generate test images in different formats.

    Args:
        output_dir: Directory to save images.
        size: Image size as (width, height).

    Returns:
        Dictionary mapping format name to file path.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {}

    # Create a simple gradient image
    img = Image.new("RGB", size)
    pixels = img.load()

    for y in range(size[1]):
        for x in range(size[0]):
            r = int(255 * x / size[0])
            g = int(255 * y / size[1])
            b = 128
            pixels[x, y] = (r, g, b)

    # Save in different formats
    formats = {
        "png": "test_image.png",
        "jpg": "test_image.jpg",
        "jpeg": "test_image.jpeg",
        "bmp": "test_image.bmp",
    }

    for fmt, filename in formats.items():
        path = output_dir / filename
        if fmt in ["jpg", "jpeg"]:
            img.save(path, quality=95)
        else:
            img.save(path)
        paths[fmt] = path

    return paths


def generate_different_sizes(
    output_dir: Path,
) -> List[Path]:
    """Generate test images with different dimensions.

    Args:
        output_dir: Directory to save images.

    Returns:
        List of paths to generated images.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = []

    sizes = [
        (100, 100),
        (200, 100),
        (100, 200),
        (300, 300),
    ]

    colors = [
        (200, 100, 100),
        (100, 200, 100),
        (100, 100, 200),
        (200, 200, 100),
    ]

    for i, (size, color) in enumerate(zip(sizes, colors)):
        img = Image.new("RGB", size, color=color)

        # Draw size label
        draw = ImageDraw.Draw(img)
        text = f"{size[0]}x{size[1]}"
        draw.text((10, 10), text, fill=(255, 255, 255))

        path = output_dir / f"size_{size[0]}x{size[1]}.png"
        img.save(path)
        paths.append(path)

    return paths


def generate_single_image(
    output_dir: Path,
    size: tuple[int, int] = (200, 200),
) -> Path:
    """Generate a single test image.

    Args:
        output_dir: Directory to save image.
        size: Image size as (width, height).

    Returns:
        Path to generated image.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create a simple pattern
    img = Image.new("RGB", size, color=(150, 150, 150))
    draw = ImageDraw.Draw(img)

    # Draw a circle
    margin = 20
    draw.ellipse(
        [margin, margin, size[0] - margin, size[1] - margin],
        fill=(100, 150, 255),
        outline=(50, 100, 200),
        width=3,
    )

    path = output_dir / "single_image.png"
    img.save(path)
    return path


def generate_all_test_images(base_dir: Path) -> dict:
    """Generate all test images for the test suite.

    Args:
        base_dir: Base directory for test fixtures.

    Returns:
        Dictionary containing paths to all generated images.
    """
    return {
        "basic_sequence": generate_basic_sequence(
            base_dir / "basic_sequence",
            count=5,
        ),
        "formats": generate_different_formats(
            base_dir / "formats",
        ),
        "sizes": generate_different_sizes(
            base_dir / "sizes",
        ),
        "single": generate_single_image(
            base_dir / "single",
        ),
    }


if __name__ == "__main__":
    """Generate test images when run as a script."""
    import sys

    # Get the fixtures directory
    script_dir = Path(__file__).parent
    fixtures_dir = script_dir

    print(f"Generating test images in: {fixtures_dir}")

    try:
        result = generate_all_test_images(fixtures_dir)
        print("\nGenerated test images:")
        print(f"  Basic sequence: {len(result['basic_sequence'])} images")
        print(f"  Different formats: {len(result['formats'])} images")
        print(f"  Different sizes: {len(result['sizes'])} images")
        print(f"  Single image: {result['single']}")
        print("\nTest images generated successfully!")
    except Exception as e:
        print(f"Error generating test images: {e}", file=sys.stderr)
        sys.exit(1)
