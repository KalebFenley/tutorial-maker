import os
from PIL import Image

# Directory containing screenshots
screenshot_dir = 'screenshots'

# Get the list of screenshots
screenshot_files = [f for f in os.listdir(screenshot_dir) if f.endswith('.png')]

# Prompt for tutorial title
title = input("Enter the title of the tutorial: ")

# Open the markdown file for writing
with open('tutorial.md', 'w') as file:
    # Write the title
    file.write(f'# {title}\n\n')

    # Iterate over each screenshot
    for screenshot_file in sorted(screenshot_files):
        # Display the screenshot
        img_path = os.path.join(screenshot_dir, screenshot_file)
        img = Image.open(img_path)
        img.show()
        
        # Prompt for description
        description = input(f"Describe the action for screenshot {screenshot_file}: ")

        # Close the image window
        img.close()

        # Write the screenshot and description to the markdown file
        file.write(f'## {description}\n')
        file.write(f'![{description}]({img_path})\n\n')

print("Tutorial markdown file generated successfully.")
