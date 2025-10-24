# Test Fixtures

This directory contains test fixtures for the img2gif test suite, including a script to generate test images programmatically.

## Overview

Test images are generated using the `generate_test_images.py` script, which creates simple, reproducible test images for various testing scenarios. These generated images ensure consistent test behavior across all environments.

## Directory Structure

```
fixtures/
├── README.md                   # This file
├── generate_test_images.py    # Image generation script
├── basic_sequence/             # Sequential frames (5 images)
│   ├── frame_001.png
│   ├── frame_002.png
│   ├── frame_003.png
│   ├── frame_004.png
│   └── frame_005.png
├── formats/                    # Different image formats
│   ├── test_image.png
│   ├── test_image.jpg
│   ├── test_image.jpeg
│   └── test_image.bmp
├── single/                     # Single test image
│   └── single_image.png
└── sizes/                      # Various dimensions
    ├── size_100x100.png
    ├── size_100x200.png
    ├── size_200x100.png
    └── size_300x300.png
```

## Generating Test Images

### Automatic Generation

Test images are automatically generated when needed by the test suite through fixtures defined in `conftest.py`.

### Manual Generation

To manually regenerate all test images, run:

```bash
python tests/fixtures/generate_test_images.py
```

This will create/overwrite all test images in their respective subdirectories.

## Test Image Types

### Basic Sequence
- **Location**: `basic_sequence/`
- **Purpose**: Testing animation sequences with multiple frames
- **Count**: 5 images
- **Format**: PNG
- **Size**: 200×200 pixels
- **Features**: Each image has a distinct color and displays its frame number

### Different Formats
- **Location**: `formats/`
- **Purpose**: Testing support for various image formats
- **Formats**: PNG, JPG, JPEG, BMP
- **Size**: 150×150 pixels
- **Features**: Gradient pattern for visual verification

### Different Sizes
- **Location**: `sizes/`
- **Purpose**: Testing handling of various image dimensions
- **Sizes**: 100×100, 200×100, 100×200, 300×300
- **Format**: PNG
- **Features**: Each image displays its dimensions as text

### Single Image
- **Location**: `single/`
- **Purpose**: Testing single image to GIF conversion
- **Format**: PNG
- **Size**: 200×200 pixels
- **Features**: Circle pattern for visual verification

## Using Real Images

This fixture system is designed to be temporary. To replace generated images with real-world test images:

1. **Add your images** to the appropriate subdirectories (or create new ones)
2. **Update `conftest.py`** to reference your images instead of generating them
3. **Optional**: Delete `generate_test_images.py` if no longer needed

## Notes

- Generated images are committed to the repository to ensure test consistency
- Images are deliberately simple to keep the repository size small
- All generated images use basic shapes and solid colors for fast generation
- The generation script uses only Pillow (PIL) to avoid additional dependencies
