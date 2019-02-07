from tkinter import *

def createGrid ():
    ''' Draws an orange grid using the constants GRIDSIZE and SQUARESIZE constants'''
    for row in range (0,GRIDSIZE):
        for column in range (0,GRIDSIZE):
            canvas.create_rectangle (column* SQUARESIZE, row* SQUARESIZE, column* SQUARESIZE+ SQUARESIZE, row * SQUARESIZE+SQUARESIZE,fill = "orange" ,outline = "black")
                             
    
def whereIsTheMouseXY (event):
    '''Outputs the mouse position x and y coordinates on the Idle window and the tkinter canvas.
    event is an action from the user (ie. mouse click or keyboard press). It is interpreted by the "event listener"
    This function is binded (joined) with the click of the left mouse button - <Button 1>'''
    
    canvas.create_rectangle (50,450,550,550,fill = "white", outline = "black")   
    print ("Clicked at", event.x, event.y)  # Outputs the x and y position of the mouse click on the Idle window
    stringOutput = "Clicked at " + str(event.x)+", "+ str(event.y) # Concatenates the info into a string to use the create_text function 
    canvas.create_text (300,500, text=stringOutput, fill='blue', font=('verdana',20)) #Outputs the mouse positon on the canvas

def whereIsTheMouseRowColumn (event):
    '''Outputs the row and column using the x and y coordinates of the mouse position  on the Idle window and the tkinter canvas.
    event is an action from the user (ie. mouse click or keyboard press). It is interpreted by the "event listener"
    This function is binded (joined) with the click of the right mouse button - <Button 3>'''
    
    print ("clicked at", event.x, event.y )
    canvas.create_rectangle (50,450,550,550,fill = "white", outline = "black")

    row = event.y//SQUARESIZE       # Calculates the row using the y coordinate of the mouse click
    column = event.x //SQUARESIZE   # Calculates the column using the x coordinate of the mouse click
    
    stringOutput = "Clicked at row " + str(row)+" and column "+ str(column) # Concatenates the info into a string 
    canvas.create_text (300,500, text=stringOutput, fill='blue', font=('verdana',20)) #Outputs the mouse positon on the canvas

    canvas.create_rectangle (column* SQUARESIZE, row* SQUARESIZE, column* SQUARESIZE+ SQUARESIZE, row * SQUARESIZE+SQUARESIZE,fill = "pink" ,outline = "black")

def outputKey (event):
    '''Outputs a message on the Idle window - used to show binding keyboard events.
    event is an action from the user (ie. mouse click or keyboard press). It is interpreted by the "event listener"
    This function is binded (joined) with the user pressing the 'a' key on the keyboard'''

    print ("User inputted the 'a' key") # Outputted on the Idle window

    
	 
# Constants store data like variables but they are not changed in the program. The name is often all in capitals to make them distinguishable from variables 

SQUARESIZE = 30 # A constant which is the size of each square in pixels.

GRIDSIZE =5	# A constant which is the number of rows and columns in the grid

root=Tk()   #Creates a tkinter object (ie. starts tkinter

# Draws a surface to display our graphics
canvas = Canvas (root, width = 600, height = 600, background="white")
canvas.pack() # Tells the computer to get the canvas (surface) ready

# Binds events to specific void functions created above
root.bind("<Button-1>", whereIsTheMouseXY)  # If user presses left mouse button, function 'whereIsTheMouseXY' is called

root.bind("<Button-3>", whereIsTheMouseRowColumn)   # If user presses right mouse button, function 'whereIsTheMouseRowColumn' is called

root.bind("<a>" , outputKey) # If user presses the 'a' key, function 'outputKey' is called

# Functions which are called
createGrid()    # Calls the function to call the grid

root.mainloop ()    # # The event listener. This built in function "listens" for an event, identifies  the event and then calls the appropriate binded function
