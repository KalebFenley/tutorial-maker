import os
from PIL import Image
import matplotlib.pyplot as plt

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
        
        # Resize the image (e.g., reduce to 50% of the original size)
        max_size = (800, 600)  # Example maximum size (width, height)
        img.thumbnail(max_size)
        
        # Display the resized image
        plt.figure(figsize=(img.width / 100, img.height / 100), dpi=100)
        plt.imshow(img)
        plt.axis('off')  # Hide the axes
        plt.show(block=False)  # Non-blocking call to show the image

        # Prompt for description
        description = input(f"Describe the action for screenshot {screenshot_file}: ")
        
        # Close the image window
        plt.close()

        # Write the screenshot and description to the markdown file
        file.write(f'## {description}\n\n')
        file.write(f'![{description}]({img_path})\n\n')

print("Tutorial markdown file generated successfully.")
