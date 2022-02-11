from cmath import rect
from ssl import cert_time_to_seconds
from turtle import fillcolor
import fitz

def hex_to_rgb(hex):
	if(not hex):
		return None
	if(hex[0] == '#'):
		hex = hex[1:]
	return tuple(float(int(hex[i:i+2], 16))/255 for i in (0, 2, 4)) 

DRAWING_TYPE_RECT = 'rect'
DRAWING_TYPE_OVAL = 'oval'
DRAWING_TYPE_CIRCLE = 'circle'
DRAWING_TYPE_TEXT = 'text'
ALLOWED_DRAWING_TYPES = ['rect', 'oval', 'circle', 'text']
PAGE = 'page'
TYPE = 'type'
LOCATION = "location"
STROKE_COLOR = "strokeColor"
FILL_COLOR = "fillColor"
STROKE_OPACITY = "strokeOpacity"
FILL_OPACITY = "fillOpacity"
DASHES = "dashes"
BORDER_WIDTH = "borderWidth"
CENTER = "center"
RADIUS = "radius"
TEXT = "text"
FONT_COLOR = "fontColor"
FONT_SIZE = "fontSize"

def get_location_from_string(input) -> fitz.Rect:
	print("Creating fitz rect from:", input)
	_ = list(map(lambda s:int(s), input.split(',')))
	return fitz.Rect(_[0], _[1], _[2], _[3])

def get_point_from_string(input) -> fitz.Point:
	print("Creating fitz point from:", input)
	_ = list(map(lambda s:int(s), input.split(',')))
	return fitz.Point(_[0], _[1])

def draw_rect(page, drawing):
	print("Drawing a rectangle: ", drawing)
	if(LOCATION not in drawing):
		return False
	location = drawing[LOCATION]
	if(STROKE_COLOR not in drawing):
		stroke_color = None
	else:
		stroke_color = hex_to_rgb(drawing[STROKE_COLOR])
	if(FILL_COLOR not in drawing):
		fillcolor = None
	else:
		fillcolor = hex_to_rgb(drawing[FILL_COLOR])
	if(STROKE_OPACITY in drawing):	
		stroke_opacity = drawing[STROKE_OPACITY]
	else:
		stroke_opacity = 1
	if(FILL_OPACITY in drawing):
		fillopacity = drawing[FILL_OPACITY]
	else:
		fillopacity = 1
	if(DASHES in drawing):
		dashes = drawing[DASHES]
		dashes = (str(dashes[0:2]) + " " +  str(dashes[2])).replace(',','')
	else:
		dashes = None
	if(BORDER_WIDTH in drawing):
		width = drawing[BORDER_WIDTH]
	else: 
		width = 1
	rect_location = get_location_from_string(location)
	print("Parameters :", rect_location, stroke_color, stroke_opacity, fillcolor, fillopacity, dashes, width)
	page.draw_rect(rect_location, width = width, color = stroke_color, fill = fillcolor, fill_opacity = fillopacity, dashes= dashes)
	return True

def draw_oval(page, drawing):
	print("Drawing a oval: ", drawing)
	if(LOCATION not in drawing):
		return False
	location = drawing[LOCATION]
	if(STROKE_COLOR not in drawing):
		stroke_color = None
	else:
		stroke_color = hex_to_rgb(drawing[STROKE_COLOR])
	if(FILL_COLOR not in drawing):
		fillcolor = None
	else:
		fillcolor = hex_to_rgb(drawing[FILL_COLOR])
	if(STROKE_OPACITY in drawing):	
		stroke_opacity = drawing[STROKE_OPACITY]
	else:
		stroke_opacity = 1
	if(FILL_OPACITY in drawing):
		fillopacity = drawing[FILL_OPACITY]
	else:
		fillopacity = 1
	if(DASHES in drawing):
		dashes = drawing[DASHES]
		dashes = (str(dashes[0:2]) + " " +  str(dashes[2])).replace(',','')
	else:
		dashes = None
	if(BORDER_WIDTH in drawing):
		width = drawing[BORDER_WIDTH]
	else: 
		width = 1
	rect_location = get_location_from_string(location)
	print("Parameters :", rect_location, stroke_color, stroke_opacity, fillcolor, fillopacity, dashes, width)
	page.draw_oval(rect_location, width = width, color = stroke_color, fill = fillcolor, fill_opacity = fillopacity, dashes= dashes)
	return True

def draw_circle(page, drawing):
	print("Drawing a circle: ", drawing)
	if(CENTER not in drawing):
		return False
	center = drawing[CENTER]
	if(RADIUS not in drawing):
			return False
	radius = drawing[RADIUS]
	if(STROKE_COLOR not in drawing):
		stroke_color = None
	else:
		stroke_color = hex_to_rgb(drawing[STROKE_COLOR])
	if(FILL_COLOR not in drawing):
		fillcolor = None
	else:
		fillcolor = hex_to_rgb(drawing[FILL_COLOR])
	if(STROKE_OPACITY in drawing):	
		stroke_opacity = drawing[STROKE_OPACITY]
	else:
		stroke_opacity = 1
	if(FILL_OPACITY in drawing):
		fillopacity = drawing[FILL_OPACITY]
	else:
		fillopacity = 1
	if(DASHES in drawing):
		dashes = drawing[DASHES]
		dashes = (str(dashes[0:2]) + " " +  str(dashes[2])).replace(',','')
	else:
		dashes = None
	if(BORDER_WIDTH in drawing):
		width = drawing[BORDER_WIDTH]
	else: 
		width = 1
	
	center_point = get_point_from_string(center)
	print("Parameters :", center, radius, stroke_color, stroke_opacity, fillcolor, fillopacity, dashes, width)
	page.draw_circle(center_point, radius=radius, width = width, color = stroke_color, fill = fillcolor, fill_opacity = fillopacity, dashes= dashes)
	return True

def draw_text(page, drawing):
	return True


def draw_on_pdf(base_file, draw_details, output_name):
	doc = fitz.open(base_file)
	if (not doc.isPDF) :
		return (False, "The base document is not pdf.")	
	if (len(draw_details) == 0) :
		return (False, "No drawing detail provided.")
	drawing_success = True
	# print("Attempting draw:", draw_details)
	try:
		for drawing in draw_details:
			if(drawing[PAGE] >= doc.page_count):
				return (False, 'Page count out of limit - pages in document: ' + doc.page_count)
			page = doc[drawing[PAGE]]
			if not page.is_wrapped:
				page.wrap_contents()
			drawing_type = drawing[TYPE]
			drawing_success = True
			if(drawing_type not in ALLOWED_DRAWING_TYPES):
				return (False, "Drawing type " + drawing_type + " is not supported")
			else:
				print("Drawing", drawing_type, "on page", page)
			if (drawing_type == DRAWING_TYPE_RECT) :
				drawing_success = draw_rect(page, drawing)
				# print("Drawing a rectangle: ", drawing)
				# location = drawing[LOCATION]
				# stroke_color = hex_to_rgb(drawing[STROKE_COLOR])
				# fillcolor = hex_to_rgb(drawing[FILL_COLOR])
				# stroke_opacity = drawing[STROKE_OPACITY]
				# fillopacity = drawing[FILL_OPACITY]
				# dashes = drawing[DASHES]
				# width = drawing[BORDER_WIDTH]
				# rect_location = get_location_from_string(location)
				# print("Parameters :", rect_location, stroke_color, stroke_opacity, fillcolor, fillopacity, dashes, width)
				# page.draw_rect(rect_location, width = width, color = stroke_color, fill = fillcolor, fill_opacity = fillopacity, dashes= dashes)
			elif (drawing_type == DRAWING_TYPE_OVAL) :
				drawing_success = draw_oval(page, drawing)	
			elif (drawing_type == DRAWING_TYPE_CIRCLE) :
				drawing_success = draw_circle(page, drawing)	
			elif (drawing_type == DRAWING_TYPE_TEXT) :
				drawing_success = draw_text(page, drawing)	
		if(not drawing_success):
			return (False, "Failed drawing " + drawing_type + " at location " + drawing[LOCATION])
		else:
			print("Saving", output_name)
			doc.save(output_name)
	except Exception as e:
		print(e)
		return (False, str(e))
	finally:
		doc.close()
	return (drawing_success,)
