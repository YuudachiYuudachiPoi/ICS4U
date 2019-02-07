from tkinter import *

def loadList(questions):
    aSingleQuestion = {}
    aSingleQuestion["Question"]="What course is this?"
    aSingleQuestion["a"]="ICS 3U"
    aSingleQuestion["b"]="ICS 3C"
    aSingleQuestion["Answer"]="a"
    questions.append(aSingleQuestion)

    aSingleQuestion = {}
    aSingleQuestion["Question"]="What time is the exam?"
    aSingleQuestion["a"]="8:30 a.m."
    aSingleQuestion["b"]="12:00 p.m."
    aSingleQuestion["Answer"]="b"
    questions.append(aSingleQuestion)

    aSingleQuestion = {}
    aSingleQuestion["Question"]="What day is the exam?"
    aSingleQuestion["a"]="Friday"
    aSingleQuestion["b"]="Monday"
    aSingleQuestion["Answer"]="a"
    questions.append(aSingleQuestion)

    aSingleQuestion = {}
    aSingleQuestion["Question"]="What date is exam?"
    aSingleQuestion["a"]="February 1"
    aSingleQuestion["b"]="January 29"
    aSingleQuestion["Answer"]="b"
    questions.append(aSingleQuestion)
    print (questions)

def start (questions):
    global numCorrect
    global questionNum
    questionNum = -1
    numCorrect=0
    instructionWindow = Toplevel(background="red")
    instructionWindow.geometry ("400x400+200+200")
    instructionWindow.wm_attributes('-topmost', 1)

    instructionArea=Canvas(instructionWindow)
    instructionArea.pack()
    instructionArea.create_text (200,120, text="Type instructions here", fill='blue', font=('verdana',20))

    buttonFunction = lambda :newQuestion(questions,instructionWindow)

    startButton = Button(instructionWindow, text ="Start program",
                         command = buttonFunction)
    startButton.pack()
    
def newQuestion(questions,previousWindow):
        global numCorrect
        global questionNum
        questionNum+=1

        previousWindow.destroy()
        
        questionWindow = Toplevel(background="blue")
        questionWindow.geometry ("400x400+200+200")
        questionWindow.wm_attributes('-topmost', 1)

        if questionNum < len (questions):

            radioValue= IntVar()  
            
            questionText = Label(questionWindow, text=questions[questionNum]["Question"])
            questionText.pack()
            
            radioButtonFunction = lambda :checkAnswer(questions[questionNum]["Answer"],radioValue,questionWindow)

            radButA=Radiobutton(questionWindow, text=questions[questionNum]["a"],variable = radioValue,value=1,
                                command=radioButtonFunction)
            radButA.pack()
            
            radButB=Radiobutton(questionWindow, text=questions[questionNum]["b"],variable = radioValue, value=2,
                                command=radioButtonFunction)
            radButB.pack()

        else:

            questionNum=-1
            numCorrect=0
            
            doneText = Label(questionWindow, text="All questions answered")
            doneText.pack()
            
            buttonFunction = lambda :newQuestion(questions,questionWindow)
            
            startButton = Button(questionWindow, text ="Re-start quiz",
                    command = buttonFunction)
            startButton.pack()
            exitButton = Button(questionWindow, text ="Exit program",
                    command =lambda: destroyStuff(questionWindow))
            exitButton.pack()

def destroyStuff(win):
    win.destroy()
    root.destroy()

def checkAnswer(answer,radioValue,previousWindow):
    previousWindow.destroy()

    global numCorrect
    answerWindow = Toplevel(background="yellow")
    answerWindow.geometry ("400x400+200+200")
    answerWindow.wm_attributes('-topmost', 1)

    answerArea=Canvas(answerWindow)
    answerArea.pack()
    
    if radioValue.get() == 1:
        selection = "a"
    elif radioValue.get() == 2:
        selection = "b"

    if selection ==answer:
        answerArea.create_text (100,100, text="Correct", fill='blue', font=('verdana',20))
        numCorrect+=1
        answerArea.create_text (100,120, text="num right"+str(numCorrect), fill='blue', font=('verdana',20))

    else :
        answerArea.create_text (100,100, text="Wrong", fill='blue', font=('verdana',20))

    continueButton = Button(answerWindow, text ="nextQuestion",
                         command = lambda :newQuestion(questions,answerWindow))
    continueButton.pack()


root=Tk()
root.geometry ("400x400+200+200")

questions=[]
loadList(questions)

start(questions)

root.mainloop()




