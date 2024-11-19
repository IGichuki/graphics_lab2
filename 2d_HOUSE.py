import cairo

# Image dimensions
WIDTH, HEIGHT = 800, 600

# Create a new surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set the background color (white)
context.set_source_rgb(1, 1, 1)
context.rectangle(0, 0, WIDTH, HEIGHT)
context.fill()

# Helper function to draw polygons
def draw_polygon(context, points, color):
    """
    Draws a polygon on the given context.

    Parameters:
    - context: Cairo context to draw on.
    - points: List of (x, y) tuples defining the polygon's vertices.
    - color: Tuple (r, g, b) for the polygon's fill color.
    """
    context.set_source_rgb(*color)
    context.move_to(*points[0])
    for point in points[1:]:
        context.line_to(*point)
    context.close_path()
    context.fill()

# Define colors
wall_color = (0.9, 0.8, 0.7)      # Beige
roof_color = (0.2, 0.2, 0.2)      # Dark gray
window_color = (0.6, 0.8, 1)      # Light blue
door_color = (0.3, 0.3, 0.5)      # Dark blue
chimney_color = (0.8, 0.8, 0.8)   # Light gray
step_color = (0.7, 0.7, 0.7)      # Light gray for steps
grass_color = (0.4, 0.8, 0.4)     # Green for grass

# Draw elements of the scene

# Grass
draw_polygon(context, [(100, 500), (700, 500), (750, 550), (50, 550)], grass_color)

# Front wall
draw_polygon(context, [(250, 300), (450, 300), (450, 500), (250, 500)], wall_color)

# Side wall
draw_polygon(context, [(450, 300), (550, 350), (550, 500), (450, 500)], (0.85, 0.75, 0.65))

# Roof (front and side)
draw_polygon(context, [(230, 300), (470, 300), (350, 200)], roof_color)
draw_polygon(context, [(470, 300), (570, 350), (350, 200)], (0.1, 0.1, 0.1))

# Chimney
draw_polygon(context, [(420, 230), (450, 230), (450, 270), (420, 270)], chimney_color)

# Windows on front wall
draw_polygon(context, [(270, 320), (320, 320), (320, 370), (270, 370)], window_color)  # Top left
draw_polygon(context, [(380, 320), (430, 320), (430, 370), (380, 370)], window_color)  # Top right
draw_polygon(context, [(270, 400), (320, 400), (320, 450), (270, 450)], window_color)  # Bottom left
draw_polygon(context, [(380, 400), (430, 400), (430, 450), (380, 450)], window_color)  # Bottom right

# Door
draw_polygon(context, [(330, 420), (370, 420), (370, 500), (330, 500)], door_color)

# Steps in front of the door
draw_polygon(context, [(320, 500), (380, 500), (390, 510), (310, 510)], step_color)
draw_polygon(context, [(310, 510), (390, 510), (400, 520), (300, 520)], (0.6, 0.6, 0.6))

# Window on side wall
draw_polygon(context, [(470, 350), (520, 375), (520, 425), (470, 400)], window_color)

# Save the image
surface.write_to_png("house.png")
print("House drawing with perspective saved as house.png")
