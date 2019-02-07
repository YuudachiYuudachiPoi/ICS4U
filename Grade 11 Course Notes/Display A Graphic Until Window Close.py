from tkinter import * #Same as before
from PIL import Image, ImageTk

import time 	# We must import the time library so we can use a delay later in the program


def showPic (graphicFile):
    root = Tk ()  		# Same as before

    image = Image.open(graphicFile)
    photo = ImageTk.PhotoImage(image)
    print ("h",photo.height())
    print ("w",photo.width())
    photoHeight = photo.height()
    photoWidth = photo.width()

    root.geometry (str(photoWidth)+"x"+str(photoHeight)+"+100+100")      #  ("400x600+00+230")
    root.wm_attributes('-topmost', 1)

    myCanvas = Canvas (root, width =photoWidth, height = photoHeight, background = 'white')
    myCanvas.pack()

    myCanvas.create_image(photoWidth//2, photoHeight//2, image=photo)
    myCanvas.update()
    root.mainloop()
    #time.sleep(5)
    #root.destroy()
    
showPic ("joystick.jpg")
