import cairo

# Set up the canvas
WIDTH, HEIGHT = 1000, 800
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Colors
def set_color(context, r, g, b):
    context.set_source_rgb(r, g, b)

# Draw the grass platform as a 3D cuboid
def draw_grass_platform():
    # Bottom face of the cuboid (light green)
    set_color(context, 0.5, 0.8, 0.4)  # Light green
    context.move_to(150, 500)  # Extended left side of the platform
    context.line_to(800, 500)  # Extend the platform's length
    context.line_to(800, 550)
    context.line_to(150, 550)  # Bottom face, extended left side
    context.close_path()
    context.fill()

    # Left side face (darker green)
    set_color(context, 0.3, 0.6, 0.3)  # Darker green
    context.move_to(150, 500)  # Extended left side
    context.line_to(150, 550)
    context.line_to(200, 580)
    context.line_to(200, 530)  # Increased length of left face
    context.close_path()
    context.fill()

    # Right side face (darker green)
    set_color(context, 0.4, 0.7, 0.4)  # Slightly darker green
    context.move_to(800, 500)
    context.line_to(800, 550)
    context.line_to(750, 580)
    context.line_to(750, 530)
    context.close_path()
    context.fill()

# Draw the house
def draw_house():
    # Front wall
    set_color(context, 0.85, 0.8, 0.75)  # Light beige
    context.rectangle(400, 250, 200, 300)  # Larger house
    context.fill()

    # Side wall
    set_color(context, 0.8, 0.75, 0.7)  # Slightly darker beige
    context.move_to(400, 250)
    context.line_to(400, 550)
    context.line_to(330, 500)
    context.line_to(330, 200)
    context.close_path()
    context.fill()

    # Pitched Roof
    set_color(context, 0.1, 0.2, 0.4)  # Dark blue
    context.move_to(330, 200)  # Left corner
    context.line_to(400, 250)  # Front-left top
    context.line_to(600, 250)  # Front-right top
    context.line_to(530, 200)  # Right corner
    context.line_to(465, 160)  # Roof apex
    context.close_path()
    context.fill()

    # Roof Overhang
    set_color(context, 0.05, 0.1, 0.3)  # Darker blue
    context.move_to(330, 200)
    context.line_to(465, 160)  # Apex
    context.line_to(530, 200)
    context.line_to(465, 140)  # Higher apex for overhang
    context.close_path()
    context.fill()

    # Chimney
    set_color(context, 0.7, 0.7, 0.7)  # Gray
    context.rectangle(490, 180, 30, 70)
    context.fill()

# Draw windows
def draw_windows():
    set_color(context, 0.6, 0.85, 1)  # Light blue

    # Top-floor windows
    context.rectangle(420, 270, 50, 70)  # Left window
    context.fill()
    context.rectangle(530, 270, 50, 70)  # Right window
    context.fill()

    # Bottom-floor windows
    context.rectangle(420, 380, 50, 70)  # Left window
    context.fill()
    context.rectangle(530, 380, 50, 70)  # Right window
    context.fill()

# Draw the door
def draw_door():
    set_color(context, 0.1, 0.3, 0.6)  # Dark blue
    context.rectangle(480, 450, 40, 100)  # Taller door
    context.fill()

    # Door window
    set_color(context, 0.5, 0.8, 1)  # Light blue
    context.rectangle(485, 470, 30, 50)
    context.fill()

# Draw steps in front of the door
def draw_steps():
    set_color(context, 0.7, 0.7, 0.7)  # Light gray

    # Three descending steps
    context.rectangle(470, 550, 60, 15)  # Bottom step
    context.fill()
    context.rectangle(475, 535, 50, 15)  # Middle step
    context.fill()
    context.rectangle(480, 520, 40, 15)  # Top step
    context.fill()

# Combine all components
draw_grass_platform()
draw_house()
draw_windows()
draw_door()
draw_steps()

# Save to file
surface.write_to_png("2d_house.png")
print("improved house is done!")
