# Automated Tutorial Generator with Screenshots

This project automates the creation of tutorials by capturing screenshots and integrating user-provided descriptions into a markdown file.

## Features

* **Screenshot Capture:** Capture screenshots with highlighted cursor position on click.
* **Description Prompts:** Enter descriptions for each screenshot to explain actions.
* **Markdown Generation:** Generate a well-structured tutorial in markdown format using the images and descriptions you provided.

### Installation

This program requires Python 3.x to run. You can install it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

**Dependencies:**

Installation is made simple with python-pip. Just run:

`pip install requirements.txt`

### Usage

1. Run `screenshot-recorder.py`
2. Go through the proces of performing the action you want to create a tutorial for as you normally would
3. Close `screenshot-recorder.py`
4. Run `generate-md.py`
5. Answer the prompts, and thats it!

Your Markdown file will be generated and saved in the current directory with the title you supplied.

## Licencensing

This project is licensed under the MIT License. See the `LICENSE` file for details.
