# Image-Based Auto Clicker

A Python script that continuously scans your screen for a specific image (like a button) and instantly teleports the cursor to click it when found. It features a clean, fixed CLI "GUI" that updates in real-time without endlessly scrolling your terminal.

## Prerequisites

This script requires Python 3 and a few external libraries. You can install all dependencies via pip:

```bash
pip install pyautogui keyboard opencv-python
```

*Note: `opencv-python` is required for the `confidence` parameter, which allows the script to find the image even if there are slight pixel variations.*

## Setup

1. Take a screenshot of the specific button or element you want the script to click. Make sure to capture *only* the element itself, without too much background.
2. Save this image as **`btn.png`** in the exact same directory as `main.py`.

> [!IMPORTANT]
> **Make sure to replace the existing `btn.png` file with your own button image.**

## Usage

Run the script from your terminal:

```bash
python main.py
```

- The script will launch and display an `Auto Clicker - Active` terminal UI.
- It will continuously scan your primary monitor for `btn.png`.
- As soon as the image appears on screen, it will teleport the cursor and left-click its center.
- **Panic Button:** You can press **`Ctrl+Q`** at any time while the script is running to immediately terminate it.

## Notes
- The program requires a brief 1-second pause after every click to prevent rapidly spamming the button.
- If you change the name of your screenshot, be sure to update the `target_element` variable in `main.py`!
