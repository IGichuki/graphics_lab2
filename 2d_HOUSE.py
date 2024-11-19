import cairo

# Set up the canvas dimensions
WIDTH, HEIGHT = 800, 800
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)
context.set_source_rgb(1, 1, 1)
context.paint()

# Create roof
# Left side
context.set_source_rgb(0.5, 0.5, 0.5)
context.move_to(180, 200)
context.line_to(250, 150)
context.line_to(320, 200)
context.close_path()
context.set_source_rgb(0.9, 0.85, 0.8)
context.fill_preserve()
context.stroke()

# Right side
context.set_source_rgb(0.5, 0.5, 0.5)
context.move_to(540, 67)
context.line_to(610, 17)
context.line_to(680, 67)
context.stroke()

# Connect right side
context.move_to(320, 200)
context.line_to(680, 67)
context.line_to(610, 17)
context.line_to(250, 150)
context.close_path()
context.fill_preserve()
context.set_source_rgb(0.5, 0.5, 0.5)
context.set_line_width(2)
context.stroke()

# Connect left side
context.move_to(180, 200)
context.line_to(540, 67)
context.line_to(610, 17)
context.line_to(250, 150)
context.close_path()
context.fill_preserve()
context.set_source_rgb(0.5, 0.5, 0.5)
context.set_line_width(2)
context.stroke()

# House body
context.move_to(330, 200)
context.line_to(330, 600)
context.line_to(670, 467)
context.line_to(670, 67)
context.close_path()
context.set_source_rgb(0.9, 0.85, 0.8)
context.fill_preserve()
context.set_line_width(2)
context.stroke()

# Left house
context.move_to(182, 200)
context.line_to(180, 467)
context.line_to(330, 600)
context.line_to(330, 200)
context.close_path()
context.set_source_rgb(0.9, 0.85, 0.8)
context.fill_preserve()
context.set_line_width(2)
context.stroke()


context.set_source_rgb(0.678, 0.847, 0.902)  # Light blue
# Top-left window
context.move_to(200, 230)
context.line_to(260, 210)
context.line_to(260, 300)
context.line_to(200, 320)
context.close_path()
context.fill_preserve()
context.set_source_rgb(0, 0, 0)
context.stroke()

# Top-right window
context.set_source_rgb(0.678, 0.847, 0.902)  # Light blue
context.move_to(265, 215)
context.line_to(325, 200)
context.line_to(325, 290)
context.line_to(265, 310)
context.close_path()
context.fill_preserve()
context.set_source_rgb(0, 0, 0)
context.stroke()

# Bottom-left window
context.set_source_rgb(0.678, 0.847, 0.902)  # Light blue
context.move_to(200, 360)
context.line_to(260, 340)
context.line_to(260, 430)
context.line_to(200, 450)
context.close_path()
context.fill_preserve()
context.set_source_rgb(0, 0, 0)
context.stroke()

# Bottom-right window
context.set_source_rgb(0.678, 0.847, 0.902)  # Light blue
context.move_to(265, 350)
context.line_to(325, 330)
context.line_to(325, 425)
context.line_to(265, 445)
context.close_path()
context.fill_preserve()
context.set_source_rgb(0, 0, 0)
context.stroke()

# Add slanted door
context.set_source_rgb(0.5, 0.5, 0.5)  # Grey
context.move_to(570, 370)
context.line_to(660, 350)
context.line_to(660, 470)
context.line_to(570, 505)
context.close_path()
context.fill_preserve()
context.stroke()


# Add chimney on the roof
context.set_source_rgb(0.9, 0.85, 0.8)
context.move_to(510, 60)  
context.line_to(510, 30)  
context.line_to(540, 30)  
context.line_to(540, 60)  
context.close_path()
context.fill_preserve()
context.stroke()

# Chimney cap
context.set_source_rgb(0.3, 0.15, 0.15) 
context.move_to(505, 30)
context.line_to(545, 30)
context.line_to(540, 25)
context.line_to(510, 25)
context.close_path()
context.fill_preserve()
context.stroke()


# Save the image
surface.write_to_png("2d_house.png")
