import pyautogui
import time
import keyboard
import os

# Enable ANSI escape codes in Windows terminal for colors and cursor movement
os.system('')

# ANSI Colors
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def exit_program():
    print(f"\n{RED}Shortcut pressed (Ctrl+Q). Exiting...{RESET}")
    os._exit(0)

# Register the exit shortcut
keyboard.add_hotkey('ctrl+q', exit_program)

def draw_cli(status_msg):
    """
    Clears the terminal and draws the 'GUI' interface to avoid text scrolling.
    Uses ANSI escape codes to prevent flickering:
    \033[H moves cursor to top-left, \033[J clears screen below cursor.
    """
    print("\033[H\033[J", end="")
    print(f"Auto Clicker - {GREEN}Active{RESET}")
    print("Press 'Ctrl+Q' at any time to exit.")
    print("-" * 40)
    print(f"Status: {status_msg}")

if __name__ == "__main__":
    # Get the absolute path to the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_element = os.path.join(script_dir, "btn.png")
    current_status = "Starting up..."
    
    while True:
        draw_cli(current_status)
        
        try:
            # Look for the submit button on the screen
            button_location = pyautogui.locateCenterOnScreen(target_element, confidence=0.8)
            
            if button_location is not None:
                # Update UI before performing the action
                current_status = f"Clicked '{target_element}' at ({button_location.x}, {button_location.y})!"
                draw_cli(current_status)
                
                # Teleport and click
                pyautogui.click(button_location.x, button_location.y)
                
                # Extra pause so the 'clicked' message stays on screen briefly
                time.sleep(1)
            else:
                current_status = f"Searching for '{target_element}'..."
                
        except pyautogui.ImageNotFoundException:
            current_status = f"Searching for '{target_element}'..."
        except Exception as e:
            current_status = f"Error: {e}"
            
        time.sleep(1)  # Brief pause before checking again
