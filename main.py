import pyautogui
import time
import keyboard
import os

os.system('')

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def exit_program():
    print(f"\n{RED}Shortcut pressed (Ctrl+Q). Exiting...{RESET}")
    os._exit(0)

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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    buttons_dir = os.path.join(script_dir, "buttons")
    
    if not os.path.exists(buttons_dir):
        os.makedirs(buttons_dir)
        print(f"\n{YELLOW}Created folder 'buttons'. Please place your target images inside and restart.{RESET}")
        os._exit(0)

    current_status = "Starting up..."
    
    valid_extensions = ('.png', '.jpg', '.jpeg')

    while True:
        draw_cli(current_status)
        
        target_images = [f for f in os.listdir(buttons_dir) if f.lower().endswith(valid_extensions)]
        
        if not target_images:
            current_status = f"{YELLOW}No images found in the '{os.path.basename(buttons_dir)}' folder.{RESET}"
            time.sleep(2)
            continue
            
        found_any = False
        
        for img_name in target_images:
            img_path = os.path.join(buttons_dir, img_name)
            
            try:
                button_location = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)
                
                if button_location is not None:
                    current_status = f"Clicked '{img_name}' at ({button_location.x}, {button_location.y})!"
                    draw_cli(current_status)
                    
                    pyautogui.click(button_location.x, button_location.y)
                    
                    found_any = True
                    time.sleep(1)
                    break 
                    
            except pyautogui.ImageNotFoundException:
                pass
            except Exception as e:
                current_status = f"{RED}Error scanning '{img_name}': {e}{RESET}"
                draw_cli(current_status)
                time.sleep(1)
        
        if not found_any:
            current_status = f"Searching for {len(target_images)} images in '{os.path.basename(buttons_dir)}'..."
            
        time.sleep(1)