import fitz


doc = fitz.open('testpdf.pdf')	

page = doc[0]

r = fitz.Rect(50,50,300,300)
r1 = fitz.Rect(150,150,300,400)
r2 = fitz.Rect(300,400,600,700)

# annot = page.add_rect_annot(r)
page.draw_rect(r, color=(1,0,0), width = 2, dashes="[1 2] 0", fill = (0.50,0.8,0.02), fill_opacity = 0.5)
page.draw_oval(r1, color=(0.50,0.8,0.02), width = 0.5, dashes="[1 2] 0", fill = (1,0,0), fill_opacity = 0.5)
page.draw_circle(r1.tl, radius = 45, color=(0.02,0.8,0.02), width = 4, dashes="[4] 0", fill = (1,0,0), fill_opacity = 0.5)

page.draw_rect(r2, color=(0,0,0), width = 1, dashes="[2]", fill = (0.50,0.8,0.02), fill_opacity = 0.5)
page.insert_textbox(r2, "hello world", fontsize = 12, color = (1,0,0), border_width = 0.7) #, border_width = 0.7, fill = None, fill_opacity=0.4, stroke_opacity = 1)


# page  .draw
# annot.set_border(width = 0.3, dashes = [2])

# annot.update()

doc.save('out6.pdf')
doc.close()
