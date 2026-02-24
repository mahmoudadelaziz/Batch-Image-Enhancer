# Batch Image Enhancer

A simple Python command-line tool for applying image enhancement operations to entire directories of images in one go.

---

## Features

- **Noise Reduction** — Smooths out image noise using a Gaussian blur filter
- **Brightness & Contrast Adjustment** — Boosts image clarity with configurable alpha/beta scaling via OpenCV
- **Sharpening** — Enhances edges and fine detail using a 3×3 high-pass convolution kernel
- **Batch Processing** — Processes all supported images in a directory at once
- **Non-destructive Output** — Saves enhanced images with an `enhanced_` prefix to a separate output directory, leaving originals untouched

---

## Supported Formats

`.jpg` · `.jpeg` · `.png` · `.bmp` · `.tiff`

---

## Requirements

- Python >= 3.9
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

---

## Installation

**Clone the repository:**

```bash
git clone https://github.com/mahmoudadelaziz/Batch-Image-Enhancer.git
cd Batch-Image-Enhancer
```

**Install dependencies using `uv` (recommended):**

```bash
uv sync
```

**Or using pip:**

```bash
pip install opencv-python rich
```

---

## Usage

```bash
python src/cli.py [OPTIONS] <SourceDirectory> <OutputDirectory>
```

### Arguments

| Argument            | Description                                      |
|---------------------|--------------------------------------------------|
| `SourceDirectory`   | Path to the folder containing the input images   |
| `OutputDirectory`   | Path to the folder where enhanced images are saved |

### Options

| Flag          | Long form                   | Description                                              |
|---------------|-----------------------------|----------------------------------------------------------|
| `-denoise`    | `--reduce_noise`            | Reduce noise using Gaussian blur (5×5 kernel)            |
| `-adjustBC`   | `--fix_brightness_contrast` | Adjust brightness (β=32.5) and contrast (α=1.25)         |
| `-sharpen`    | `--sharpen_image`           | Sharpen edges using a 3×3 high-pass filter               |

Flags can be combined freely. If no enhancement flag is provided, no output is saved.

---

## Examples

**Sharpen only:**
```bash
python src/cli.py -sharpen ./input_images ./output_images
```

**Denoise and adjust brightness/contrast:**
```bash
python src/cli.py -denoise -adjustBC ./input_images ./output_images
```

**Apply all three enhancements:**
```bash
python src/cli.py -denoise -adjustBC -sharpen ./input_images ./output_images
```

Enhanced images will be saved as `enhanced_<original_filename>` in the output directory. The output directory is created automatically if it doesn't exist.

---

## Project Structure

```
Batch-Image-Enhancer/
├── src/
│   ├── cli.py                  # Entry point — argument parsing and pipeline orchestration
│   ├── input_loader.py         # Loads supported images from a directory
│   ├── output_saver.py         # Saves processed images to the output directory
│   ├── adjust_brightness.py    # Brightness and contrast adjustment
│   ├── reduce_noise.py         # Gaussian blur noise reduction
│   └── sharpen.py              # High-pass kernel sharpening
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Dependencies

| Package          | Purpose                                 |
|------------------|-----------------------------------------|
| `opencv-python`  | Core image loading, processing, saving  |
| `rich`           | Formatted terminal output               |

---

## License


This project is open source. Feel free to use, modify, and distribute it.
