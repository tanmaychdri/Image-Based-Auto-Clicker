# Image Based Auto Clicker

A lightweight Python auto-clicker that searches your screen for image matches and clicks the center of the first matching button it finds. It keeps a simple terminal UI updated in place so the output stays readable while it runs.

## Features

- Scans a `buttons/` folder for image files
- Supports `.png`, `.jpg`, and `.jpeg` images
- Uses `pyautogui.locateCenterOnScreen(..., confidence=0.8)` to find matches even with slight visual differences
- Clicks the center of the detected image
- Watches for `Ctrl+Q` and exits immediately
- Creates the `buttons/` folder automatically if it does not exist
- Displays a simple live status screen instead of scrolling terminal output

## Requirements

Install the dependencies with:

```bash
pip install pyautogui keyboard opencv-python
```

`opencv-python` is needed for the `confidence` option used during image matching.

## Setup

1. Run the script once to create the `buttons/` directory automatically, or create it manually in the same folder as `main.py`.
2. Add screenshots of the UI elements you want to click into that `buttons/` folder.
3. Use clear images with minimal unnecessary background for better matching.

> The script checks all images in `buttons/` automatically. You do not need to rename a single file like `btn.png`.

## Usage

Run the app from the project directory:

```bash
python main.py
```

The script will:

- show a status screen labeled `Auto Clicker - Active`
- look through every image in `buttons/`
- locate the first match on screen
- move the mouse to the matched center and click it
- pause briefly after each click
- continue scanning until you press `Ctrl+Q`

## Notes

- The script pauses for about 1 second after each successful click to avoid spamming the target too quickly.
- If no images are found in `buttons/`, it will keep checking and show a message in the terminal.
- Match quality depends on how clean and specific your target screenshots are.
- The app currently searches the primary screen area and uses the first valid match it finds in the folder order returned by the OS.
