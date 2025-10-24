"""
🧪 Pytest configuration and shared fixtures for img2gif tests

This module provides reusable test fixtures that create temporary
test environments, sample images, and other testing utilities.
"""

from pathlib import Path

import numpy as np
import pytest
from PIL import Image


@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    """
    📁 Create a temporary directory for test files.

    Args:
        tmp_path: Pytest's built-in temporary directory fixture

    Returns:
        Path to temporary directory
    """
    return tmp_path


@pytest.fixture
def sample_images_dir(temp_dir: Path) -> Path:
    """
    🖼️ Create a directory with sample test images.

    Creates 3 simple colored images (red, green, blue) for testing.

    Args:
        temp_dir: Temporary directory fixture

    Returns:
        Path to directory containing sample images
    """
    images_dir = temp_dir / "images"
    images_dir.mkdir()

    # Create 3 simple colored images 🎨
    colors = [
        (255, 0, 0),  # Red
        (0, 255, 0),  # Green
        (0, 0, 255),  # Blue
    ]

    for idx, color in enumerate(colors):
        # Create a 100x100 solid color image
        img_array = np.full((100, 100, 3), color, dtype=np.uint8)
        img = Image.fromarray(img_array)
        img.save(images_dir / f"image_{idx + 1}.png")

    return images_dir


@pytest.fixture
def single_image(temp_dir: Path) -> Path:
    """
    🖼️ Create a single test image file.

    Args:
        temp_dir: Temporary directory fixture

    Returns:
        Path to single image file
    """
    # Create a simple yellow image
    img_array = np.full((100, 100, 3), (255, 255, 0), dtype=np.uint8)
    img = Image.fromarray(img_array)

    image_path = temp_dir / "single_image.png"
    img.save(image_path)

    return image_path


@pytest.fixture
def mixed_files_dir(temp_dir: Path) -> Path:
    """
    📁 Create a directory with mixed file types (images and non-images).

    Args:
        temp_dir: Temporary directory fixture

    Returns:
        Path to directory containing mixed files
    """
    mixed_dir = temp_dir / "mixed"
    mixed_dir.mkdir()

    # Create an image
    img_array = np.full((50, 50, 3), (128, 128, 128), dtype=np.uint8)
    img = Image.fromarray(img_array)
    img.save(mixed_dir / "valid_image.png")

    # Create a text file (should be ignored)
    (mixed_dir / "readme.txt").write_text("This is not an image")

    # Create a python file (should be ignored)
    (mixed_dir / "script.py").write_text("print('hello')")

    return mixed_dir


@pytest.fixture
def empty_dir(temp_dir: Path) -> Path:
    """
    📂 Create an empty directory.

    Args:
        temp_dir: Temporary directory fixture

    Returns:
        Path to empty directory
    """
    empty = temp_dir / "empty"
    empty.mkdir()
    return empty


@pytest.fixture
def corrupted_image_dir(temp_dir: Path) -> Path:
    """
    💥 Create a directory with a corrupted image file.

    Args:
        temp_dir: Temporary directory fixture

    Returns:
        Path to directory containing corrupted image
    """
    corrupt_dir = temp_dir / "corrupted"
    corrupt_dir.mkdir()

    # Create a file with .png extension but invalid content
    (corrupt_dir / "corrupted.png").write_bytes(b"This is not a valid PNG file")

    return corrupt_dir


@pytest.fixture
def output_path(temp_dir: Path) -> Path:
    """
    📤 Generate an output path for test GIF files.

    Args:
        temp_dir: Temporary directory fixture

    Returns:
        Path where test GIF should be saved
    """
    return temp_dir / "output.gif"


@pytest.fixture
def various_formats_dir(temp_dir: Path) -> Path:
    """
    🎨 Create a directory with images in various supported formats.

    Args:
        temp_dir: Temporary directory fixture

    Returns:
        Path to directory containing images in different formats
    """
    formats_dir = temp_dir / "formats"
    formats_dir.mkdir()

    # Create a simple image
    img_array = np.full((100, 100, 3), (200, 100, 50), dtype=np.uint8)
    img = Image.fromarray(img_array)

    # Save in different formats
    img.save(formats_dir / "test.png")
    img.save(formats_dir / "test.jpg")
    img.save(formats_dir / "test.bmp")
    img.convert("RGB").save(formats_dir / "test.webp")

    return formats_dir
