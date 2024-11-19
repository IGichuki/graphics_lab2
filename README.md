# 2D House Rendering Project

This project is a simple implementation of 2D rendering to create a 3D-like house illustration using Python and the **Cairo Graphics Library**. It demonstrates basic graphics programming concepts, including shapes, colors, and layering to create depth and perspective.

## Features

- **Grass Platform**: A 3D platform with top and side faces to simulate depth.
- **House Structure**: A 3D-style house with walls, roof, and chimney.
- **Windows with Panes**: Reflective blue windows divided into four panes for added detail.
- **Door with Steps**: A detailed entrance with a door window and a three-step staircase.
- **Customizable Design**: Easy-to-modify shapes, colors, and dimensions.

## Requirements

- Python 3.x
- [pycairo](https://pycairo.readthedocs.io/en/latest/) library for graphics rendering

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/Igichuki/graphics_lab2.git
   cd 3d-house-rendering
Install the required library:

bash
Copy code
pip install pycairo
Run the script:

bash
Copy code
python house_rendering.py
File Structure
house_rendering.py: Main script for generating the house illustration.
updated_3d_house.png: The output image rendered by the script.
README.md: Documentation file.
How It Works
This project uses the Cairo Graphics Library to draw various components of the house step-by-step:

Grass Platform: Two rectangles are drawn to simulate a 3D platform with top and side faces.
House Structure:
The walls and roof are layered to give the house a 3D perspective.
The chimney is added on top for extra detail.
Windows and Panes: Blue rectangles are divided into four quadrants with white lines to simulate reflective glass with panes.
Door and Steps:
The door includes a small window.
Three stacked rectangles simulate a staircase leading to the door.
Output
Running the script will generate a PNG file named updated_3d_house.png, which looks like this:


Customization
You can easily modify the code to customize the design:

Colors: Update the RGB values in the set_color() function calls.
Dimensions: Adjust rectangle sizes and positions to change the proportions of the house and its components.
Additional Features: Add more elements like trees, fences, or pathways by creating new shapes.
Learning Objectives
This project is ideal for students or developers interested in:

Learning basic 2D rendering with Python
Understanding the layering technique to simulate 3D objects
Practicing modular and reusable code design for graphical applications
Troubleshooting
Ensure you have Python and pycairo installed correctly.
If the output image looks distorted, check your screen resolution or adjust the canvas size (WIDTH and HEIGHT).
License
This project is licensed under the MIT License. Feel free to use and modify the code for personal or educational purposes.
