import cairo

# Set up the canvas dimensions
WIDTH, HEIGHT = 800, 800
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)
context.set_source_rgb(1,1,1)
context.paint()
#create roof
# left side
context.set_source_rgb(0.5,0.5,0.5)
context.move_to(180, 200)
context.line_to(250, 150)
context.line_to(320, 200)
context.close_path()
context.set_source_rgb(0.9,0.85,0.8)
context.fill_preserve()
context.stroke()

#right side
context.set_source_rgb(0.5,0.5,0.5)
context.move_to(540, 67)
context.line_to(610, 17)
context.line_to(680, 67)
context.stroke()
#connect right side
context.move_to(320, 200)
context.line_to(680, 67)
context.line_to(610, 17)
context.line_to(250, 150)
context.close_path()
context.fill_preserve()
context.set_source_rgb(0.5,0.5,0.5)
context.set_line_width(2)
context.stroke()
#connect left side
context.move_to(180, 200)
context.line_to(540, 67)
context.line_to(610, 17)
context.line_to(250, 150)
context.close_path()
context.fill_preserve()
context.set_source_rgb(0.5,0.5,0.5)
context.set_line_width(2)
context.stroke()
#Housebody
context.move_to(330, 200)
context.line_to(330, 600)
context.line_to(670, 467)
context.line_to(670, 67)
context.close_path()
context.set_source_rgb(0.9,0.85,0.8)
context.fill_preserve()
context.set_line_width(2)
context.stroke()
#LEFT HOUSE
context.move_to(182, 200)
context.line_to(180, 467)
context.line_to(330, 600)
context.line_to(330, 200)
context.close_path()
context.set_source_rgb(0.9,0.85,0.8)
context.fill_preserve()
context.set_line_width(2)
context.stroke()
#door
context.rectangle(610, 400, 60, 80)
context.close_path()
context.set_source_rgb(0.5,0.5,0.5)
context.fill_preserve()
context.set_line_width(2)
context.stroke()

# Save the image
surface.write_to_png("2d_house.png")
