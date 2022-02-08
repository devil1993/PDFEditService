def hex_to_rgb(hex):
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

def draw_on_pdf(base_file, draw_details, output_name):
	import fitz
	doc = fitz.open(base_file)
	if(not doc.isPDF):
		return (False, "The base document is not pdf.")	
	if(len(draw_details) = 0):
		return (False, "No drawing detail provided.")
	drawing_success = True
	try:
		for drawing in draw_details:
			if(drawing[PAGE] >= doc.page_count):
				return (False, 'Page count out of limit - pages in document: ' + doc.page_count)
			page = doc[drawing[PAGE]]
			drawing_type = drawing[TYPE]
			drawing_success = True
			if(drawing_type not in ALLOWED_DRAWING_TYPES):
				return (False, "Drawing type " + drawing_type + " is not supported")
			if(drawing_type = DRAWING_TYPE_RECT):
				drawing_success = draw_rect(page, drawing)
			elif(drawing_type = DRAWING_TYPE_OVAL):
				drawing_success = draw_oval(page, drawing)	
			elif(drawing_type = DRAWING_TYPE_CIRCLE):
				drawing_success = draw_circle(page, drawing)	
			elif(drawing_type = DRAWING_TYPE_TEXT):
				drawing_success = draw_text(page, drawing)	
			if(not drawing_success):
				return (False, "Failed drawing " + drawing_type + " at location " + drawing[LOCATION])
	except Exception:
		pass
	finally:
		doc.close()
		return drawing_success
