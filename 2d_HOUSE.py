import cairo

# Set up the canvas
WIDTH, HEIGHT = 800, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Colors
def set_color(context, r, g, b):
    context.set_source_rgb(r, g, b)

# Draw the isometric grass platform
def draw_grass_platform():
    # Top face of the grass platform
    set_color(context, 0.5, 0.8, 0.4)  # Green
    context.move_to(200, 400)
    context.line_to(600, 400)
    context.line_to(700, 450)
    context.line_to(300, 450)
    context.close_path()
    context.fill()

    # Side face (front)
    set_color(context, 0.3, 0.6, 0.2)  # Darker green
    context.move_to(300, 450)
    context.line_to(700, 450)
    context.line_to(700, 480)
    context.line_to(300, 480)
    context.close_path()
    context.fill()

# Draw the house
def draw_house():
    # Front wall
    set_color(context, 0.85, 0.8, 0.75)  # Light beige
    context.rectangle(330, 250, 140, 150)
    context.fill()

    # Side wall
    set_color(context, 0.8, 0.75, 0.7)  # Slightly darker beige
    context.move_to(330, 250)
    context.line_to(330, 400)
    context.line_to(250, 350)
    context.line_to(250, 200)
    context.close_path()
    context.fill()

    # Roof
    set_color(context, 0.1, 0.2, 0.4)  # Dark blue
    context.move_to(250, 200)
    context.line_to(330, 250)
    context.line_to(470, 250)
    context.line_to(390, 200)
    context.close_path()
    context.fill()

    # Chimney
    set_color(context, 0.7, 0.7, 0.7)  # Gray
    context.rectangle(370, 190, 20, 40)
    context.fill()

# Draw windows
def draw_windows():
    set_color(context, 0.6, 0.85, 1)  # Light blue
    # Left-side window
    context.rectangle(265, 230, 30, 40)
    context.fill()

    # Front windows
    for y in [270, 310]:
        context.rectangle(350, y, 40, 40)
        context.fill()

# Draw the door
def draw_door():
    set_color(context, 0.1, 0.3, 0.6)  # Dark blue
    context.rectangle(380, 350, 30, 50)
    context.fill()

    # Door frame
    set_color(context, 0.5, 0.8, 1)  # Light blue for window
    context.rectangle(385, 360, 20, 30)
    context.fill()

# Draw steps in front of the door
def draw_steps():
    set_color(context, 0.7, 0.7, 0.7)  # Light gray
    context.rectangle(370, 400, 50, 10)  # Bottom step
    context.fill()
    context.rectangle(375, 390, 40, 10)  # Top step
    context.fill()

# Combine all components
draw_grass_platform()
draw_house()
draw_windows()
draw_door()
draw_steps()

# Save to file
surface.write_to_png("isometric_house.png")
print("Isometric house image saved as isometric_house.png")
