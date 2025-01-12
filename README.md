
# Pi Image Generator

This Python script generates an image based on the digits of π (pi), where each pixel's color is determined by a corresponding digit of π. You can specify the image dimensions (width and height) and choose between **color mode** or **grayscale mode**.

## Features
- Uses the digits of π to generate unique patterns.
- Allows customizable dimensions for the image.
- Option to render the image in **colors** or **grayscale**.
- Saves the output image with a descriptive filename that includes the dimensions and mode.

---

## Requirements

This script requires Python 3 and the following libraries:
- `Pillow` (for image generation)
- `mpmath` (for high-precision calculation of π)

---

## Installation

1. Clone this repository or download the script:
   ```bash
   git clone git@github.com:MrJhonny/py_pi_ncolors.git
   cd py_pi_ncolors
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate   # macOS/Linux
   env\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install the required libraries manually:
   ```bash
   pip install pillow mpmath
   ```

---

## Usage

Run the script using Python:

```bash
python main.py
```

### Steps:
1. The script will prompt you to enter the width and height of the image (in pixels).
   Example:
   ```
   Enter the width of the image (in pixels): 800
   Enter the height of the image (in pixels): 600
   ```

2. It will then ask if you want the image in **colors** (default) or **grayscale**:
   ```
   Do you want the image in colors? (yes/no): yes
   ```

3. Once complete, the image will be saved with a name like `pi_800x600_colors.png` or `pi_800x600_gray.png` in the same directory as the script.

---

## File Description

- `main.py`: The main Python script for generating the image.
- `requirements.txt`: A file listing all required Python packages for the script.

---

## Example Output

- **Color Image**: `pi_100x100_colors.png`
- **Grayscale Image**: `pi_100x100_gray.png`

![Example Image](pi_100x100_colors.png)
![Example Image](pi_100x100_gray.png)


*(Note: Replace `example-output.png` with an actual example output file if you have one.)*

---

## Troubleshooting

1. **Error: ModuleNotFoundError: No module named 'Pillow' or 'mpmath'**
   - Ensure you have installed the dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Python Version Issues**:
   - Ensure you're using Python 3. You can check your Python version with:
     ```bash
     python --version
     ```
