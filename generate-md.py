import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import simpledialog

# Directory containing screenshots
screenshot_dir = 'screenshots'

# Get the list of screenshots
screenshot_files = [f for f in os.listdir(screenshot_dir) if f.endswith('.png')]

# Prompt for tutorial title
title = input("Enter the title of the tutorial: ")
file_title = title.lower().replace(' ','-')
# Open the markdown file for writing
with open(f'{file_title}.md', 'w') as file:
    # Write the title
    file.write(f'# {title}\n\n')

    # Iterate over each screenshot
    for screenshot_file in sorted(screenshot_files):
        # Load the screenshot
        img_path = os.path.join(screenshot_dir, screenshot_file)
        img = Image.open(img_path)
        
        # Create a new tkinter window
        window = tk.Tk()
        window.title("Screenshot")
        
        # Convert the image to a format that can be used by tkinter
        img_tk = ImageTk.PhotoImage(img)
        
        # Create a label to display the image
        label = tk.Label(window, image=img_tk)
        label.pack()
        
        # Create a dialog to prompt for the description
        description = simpledialog.askstring("Description", "Describe the action for screenshot " + screenshot_file)
        
        # Close the window
        window.destroy()
        
        # Write the screenshot and description to the markdown file
        file.write(f'## {description}\n\n')
        file.write(f'![{description}]({img_path})\n\n')

print("Tutorial markdown file generated successfully.")