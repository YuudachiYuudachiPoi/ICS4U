from tkinter import * #Same as before
import time     # We must import the time library so we can use a delay later in the program

root = Tk ()            # Same as before
myCanvas = Canvas (root, width =1000, height = 200, background = 'white')
                        # Same as before, except the background colour is set to white
myCanvas.pack()         # Same as before

xPositionTop = 50       # Variable that stores the current x position of the graphic's top left corner

moveAmt = 10 # How many pixels the graphic will move

drawSens = PhotoImage(file = "Sens.gif") # Creates a graphic object

movingGraphic = myCanvas.create_image(xPositionTop, 50, image=drawSens) # Creates a sprite (moving graphic)

while True:

    xPositionTop += moveAmt    # Needed to keep track of position of graphic
    
    myCanvas.move(movingGraphic, moveAmt, 0) # Moves by the moveAmt
    
    if xPositionTop >800 : # Exits the program
        break
    
    myCanvas.update()   # Refreshes the canvas window each time the rectangle makes one movement. This line is needed in any program with moving graphics because it redraws the window. '''

    time.sleep(0.1) # Calls the "sleep" function from the library "time". This function halts the program for the given amount of time (in this case, half a second). In programming, this is called a delay'''
    
root.mainloop()   
