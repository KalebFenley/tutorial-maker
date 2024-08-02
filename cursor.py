from pynput import mouse
import pyautogui
import os
from PIL import Image, ImageDraw

# Directory to save screenshots
screenshot_dir = 'screenshots'
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

# Counter for screenshot filenames
screenshot_counter = 1

# Create a simple crosshair cursor image
cursor_size = 20
cursor_image = Image.new('RGBA', (cursor_size, cursor_size), (255, 255, 255, 0))
draw = ImageDraw.Draw(cursor_image)
draw.line((cursor_size//2, 0, cursor_size//2, cursor_size), fill=(255, 0, 0, 255), width=2)
draw.line((0, cursor_size//2, cursor_size, cursor_size//2), fill=(255, 0, 0, 255), width=2)

# Create a semi-transparent blue circle to highlight the cursor
highlight_size = 50
highlight_image = Image.new('RGBA', (highlight_size, highlight_size), (255, 255, 255, 0))
highlight_draw = ImageDraw.Draw(highlight_image)
highlight_draw.ellipse(
    [(0, 0), (highlight_size, highlight_size)],
    fill=(0, 0, 255, 128)  # RGBA: blue with 50% transparency
)

def on_click(x, y, button, pressed):
    global screenshot_counter
    if pressed:
        # Take a screenshot
        screenshot = pyautogui.screenshot()

        # Overlay the highlight image at the click position
        screenshot.paste(highlight_image, (x - highlight_size//2, y - highlight_size//2), highlight_image)
        
        # Overlay the cursor image at the click position
        screenshot.paste(cursor_image, (x - cursor_size//2, y - cursor_size//2), cursor_image)

        # Create a unique filename
        filename = f'screenshot_{screenshot_counter:04d}.png'
        filepath = os.path.join(screenshot_dir, filename)

        # Save the screenshot
        screenshot.save(filepath)

        # Increment the counter
        screenshot_counter += 1

        print(f'Screenshot saved: {filepath}')

# Start the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    print("Listening for mouse clicks. Press Ctrl+C to exit.")
    listener.join()
