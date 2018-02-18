'''
Himanshu Joshi (joshi271@umn.edu)
CSCI 1133 by Dr. Amy Larson
Project 1- Sudoku
'''
import turtle, random
output = turtle.Turtle()
output.hideturtle()
output.color("red")
output.penup()
output.goto(-200,-250)

def makegrid():             #makes a grid for 4X4 sudoku puzzzle
    turtle.clear()
    turtle.title("Sudoku")
    turtle.showturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,-200)
    turtle.pendown()
    turtle.pensize(5)
    turtle.forward(400)
    turtle.goto(200,200)
    turtle.goto(-200,200)
    turtle.goto(-200,-200)
    turtle.goto(-200,0)
    turtle.goto(200,0)
    turtle.goto(0,0)
    turtle.goto(0,-200)
    turtle.goto(0,200)
    turtle.pensize(1)
    turtle.penup()
    turtle.goto(100,200)
    turtle.pendown()
    turtle.goto(100,-200)
    turtle.penup()
    turtle.goto(-100,200)
    turtle.pendown()
    turtle.goto(-100,-200)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.goto(200,100)
    turtle.penup()
    turtle.goto(-200,-100)
    turtle.pendown()
    turtle.goto(200,-100)
    turtle.penup()
    turtle.goto(-265,-180)
    turtle.write("D", move=True, align="left", font=("Arial", 45, "normal"))
    turtle.goto(-265,-80)
    turtle.write("C", move=True, align="left", font=("Arial", 45, "normal"))
    turtle.goto(-265,20)
    turtle.write("B", move=True, align="left", font=("Arial", 45, "normal"))
    turtle.goto(-265,120)
    turtle.write("A", move=True, align="left", font=("Arial", 45, "normal"))
    turtle.goto(-165,220)
    turtle.write("1", move=True, align="left", font=("Arial", 45, "normal"))
    turtle.goto(-65,220)
    turtle.write("2", move=True, align="left", font=("Arial", 45, "normal"))
    turtle.goto(35,220)
    turtle.write("3", move=True, align="left", font=("Arial", 45, "normal"))
    turtle.goto(135,220)
    turtle.write("4", move=True, align="left", font=("Arial", 45, "normal"))

makegrid()

def firstquestion():
    global askrealtime
    askrealtime=turtle.textinput("Real time correction?", "Yes or No?")
    output.clear()
    #Loop to make sure user answers in yes or no
    if askrealtime.lower()=="no" or askrealtime.lower()=="yes":
        pass
    else:
        output.write("You can only enter yes or no.", move=False, align="left", font=("Times New Roman", 18, "normal"))

        try:
            return askrealtime
        finally:
            firstquestion()
firstquestion()
realtime=askrealtime.lower()
empty=""
puzzles=[]
puzzles.extend([[[3,4,1,2],[empty,empty,empty,empty],[empty,empty,empty,empty],[4,2,3,1]]])
puzzles.extend([[[empty,empty,empty,empty],[2,3,4,1],[3,4,1,2],[empty,empty,empty,empty]]])
puzzles.extend([[[4,empty,empty,1],[empty,1,3,empty],[empty,4,1,empty],[1,empty,empty,3]]])
puzzles.extend([[[empty,2,4,empty],[1,empty,empty,3],[4,empty,empty,2],[empty,1,3,empty]]])
puzzles.extend([[[empty,4,empty,1],[3,empty,4,empty],[1,empty,empty,4],[empty,2,1,empty]]])
solutions=[]
solutions.extend([[[3,4,1,2],[2,1,4,3],[1,3,2,4],[4,2,3,1]]])
solutions.extend([[[4,1,2,3],[2,3,4,1],[3,4,1,2],[1,2,3,4]]])
solutions.extend([[[4,3,2,1],[2,1,3,4],[3,4,1,2],[1,2,4,3]]])
solutions.extend([[[3,2,4,1],[1,4,2,3],[4,3,1,2],[2,1,3,4]]])
solutions.extend([[[2,4,3,1],[3,1,4,2],[1,3,2,4],[4,2,1,3]]])

allpuzzles=[]
allpuzzles.extend([[[3,4,1,2],[empty,empty,empty,empty],[empty,empty,empty,empty],[4,2,3,1]]])
allpuzzles.extend([[[empty,empty,empty,empty],[2,3,4,1],[3,4,1,2],[empty,empty,empty,empty]]])
allpuzzles.extend([[[4,empty,empty,1],[empty,1,3,empty],[empty,4,1,empty],[1,empty,empty,3]]])
allpuzzles.extend([[[empty,2,4,empty],[1,empty,empty,3],[4,empty,empty,2],[empty,1,3,empty]]])
allpuzzles.extend([[[empty,4,empty,1],[3,empty,4,empty],[1,empty,empty,4],[empty,2,1,empty]]])
def newgame():          #selects one random game
    global r1
    r1=random.randint(0,4)
    ngame=puzzles[r1]
    return ngame
newgame()
global thisgame
thisgame=newgame()
originalgame=allpuzzles[r1]
answer=solutions[r1]
def fillpuzzle():           #fills the puzzle
    turtle.penup()
    #row1
    if originalgame[0][0]==empty:
        turtle.pencolor("red")
    turtle.goto(-165,120)
    turtle.write(thisgame[0][0], move=False, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[0][1]==empty:
        turtle.pencolor("red")
    turtle.goto(-65,120)
    turtle.write(thisgame[0][1], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[0][2]==empty:
        turtle.pencolor("red")
    turtle.goto(35,120)
    turtle.write(thisgame[0][2], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[0][3]==empty:
        turtle.pencolor("red")
    turtle.goto(135,120)
    turtle.write(thisgame[0][3], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    #row2
    if originalgame[1][0]==empty:
        turtle.pencolor("red")
    turtle.goto(-165,20)
    turtle.write(thisgame[1][0], move=False, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[1][1]==empty:
        turtle.pencolor("red")
    turtle.goto(-65,20)
    turtle.write(thisgame[1][1], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[1][2]==empty:
        turtle.pencolor("red")
    turtle.goto(35,20)
    turtle.write(thisgame[1][2], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[1][3]==empty:
        turtle.pencolor("red")
    turtle.goto(135,20)
    turtle.write(thisgame[1][3], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    #row3
    if originalgame[2][0]==empty:
        turtle.pencolor("red")
    turtle.goto(-165,-80)
    turtle.write(thisgame[2][0], move=False, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[2][1]==empty:
        turtle.pencolor("red")
    turtle.goto(-65,-80)
    turtle.write(thisgame[2][1], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[2][2]==empty:
        turtle.pencolor("red")
    turtle.goto(35,-80)
    turtle.write(thisgame[2][2], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[2][3]==empty:
        turtle.pencolor("red")
    turtle.goto(135,-80)
    turtle.write(thisgame[2][3], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    #row4
    if originalgame[3][0]==empty:
        turtle.pencolor("red")
    turtle.goto(-165,-180)
    turtle.write(thisgame[3][0], move=False, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[3][1]==empty:
        turtle.pencolor("red")
    turtle.goto(-65,-180)
    turtle.write(thisgame[3][1], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[3][2]==empty:
        turtle.pencolor("red")
    turtle.goto(35,-180)
    turtle.write(thisgame[3][2], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    if originalgame[3][3]==empty:
        turtle.pencolor("red")
    turtle.goto(135,-180)
    turtle.write(thisgame[3][3], move=True, align="left", font=("Arial", 45, "normal"))
    turtle.pencolor("black")
    turtle.hideturtle()
fillpuzzle()


def changevalue(locationn,thechange):   #uses input and changes the grids
    global originalgame
    if locationn=="a1":
        if originalgame[0][0]==empty:
            thisgame[0][0]=thechange
            try:
                return thisgame[0][0]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[0][0]==empty and thechange==empty:
            thisgame[0][0]=empty
            try:
                return thisgame[0][0]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="a2":
        if originalgame[0][1]==empty:
            thisgame[0][1]=thechange
            try:
                return thisgame[0][1]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[0][1]==empty and thechange==empty:
            thisgame[0][1]=empty
            try:
                return thisgame[0][1]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="a3":
        if originalgame[0][2]==empty:
            thisgame[0][2]=thechange
            try:
                return thisgame[0][2]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[0][2]==empty and thechange==empty:
            thisgame[0][2]=empty
            try:
                return thisgame[0][2]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="a4":
        if originalgame[0][3]==empty:
            thisgame[0][3]=thechange
            try:
                return thisgame[0][3]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[0][3]==empty and thechange==empty:
            thisgame[0][3]=empty
            try:
                return thisgame[0][3]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="b1":
        if originalgame[1][0]==empty:
            thisgame[1][0]=thechange
            try:
                return thisgame[1][0]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[1][0]==empty and thechange==empty:
            thisgame[1][0]=empty
            try:
                return thisgame[1][0]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="b2":
        if originalgame[1][1]==empty:
            thisgame[1][1]=thechange
            try:
                return thisgame[1][1]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[1][1]==empty and thechange==empty:
            thisgame[1][1]=empty
            try:
                return thisgame[1][1]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="b3":
        if originalgame[1][2]==empty:
            thisgame[1][2]=thechange
            try:
                return thisgame[1][2]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[1][2]==empty and thechange==empty:
            thisgame[1][2]=empty
            try:
                return thisgame[1][2]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="b4":
        if originalgame[1][3]==empty:
            thisgame[1][3]=thechange
            try:
                return thisgame[1][3]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[1][3]==empty and thechange==empty:
            thisgame[1][3]=empty
            try:
                return thisgame[1][3]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="c1":
        if originalgame[2][0]==empty:
            thisgame[2][0]=thechange
            try:
                return thisgame[2][0]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[2][0]==empty and thechange==empty:
            thisgame[2][0]=empty
            try:
                return thisgame[2][0]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="c2":
        if originalgame[2][1]==empty:
            thisgame[2][1]=thechange
            try:
                return thisgame[2][1]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[2][1]==empty and thechange==empty:
            thisgame[2][1]=empty
            try:
                return thisgame[2][1]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="c3":
        if originalgame[2][2]==empty:
            thisgame[2][2]=thechange
            try:
                return thisgame[2][2]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[2][2]==empty and thechange==empty:
            thisgame[2][2]=empty
            try:
                return thisgame[2][2]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="c4":
        if originalgame[2][3]==empty:
            thisgame[2][3]=thechange
            try:
                return thisgame[2][3]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[2][3]==empty and thechange==empty:
            thisgame[2][3]=empty
            try:
                return thisgame[2][3]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="d1":
        if originalgame[3][0]==empty:
            thisgame[3][0]=thechange
            try:
                return thisgame[3][0]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[3][0]==empty and thechange==empty:
            thisgame[3][0]=empty
            try:
                return thisgame[3][0]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="d2":
        if originalgame[3][1]==empty:
            thisgame[3][1]=thechange
            try:
                return thisgame[3][1]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[3][1]==empty and thechange==empty:
            thisgame[3][1]=empty
            try:
                return thisgame[3][1]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="d3":
        if originalgame[3][2]==empty:
            thisgame[3][2]=thechange
            try:
                return thisgame[3][2]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[3][2]==empty and thechange==empty:
            thisgame[3][2]=empty
            try:
                return thisgame[3][2]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    if locationn=="d4":
        if originalgame[3][3]==empty:
            thisgame[3][3]=thechange
            try:
                return thisgame[3][3]
            finally:
                makegrid()
                fillpuzzle()
        if originalgame[3][3]==empty and thechange==empty:
            thisgame[3][3]=empty
            try:
                return thisgame[3][3]
            finally:
                makegrid()
                fillpuzzle()
        else:
            playgame()
    else:
        playgame()

def lastmove(locationn,thechange):
    output.goto(-150,-250)
    output.write("Last Move: You added ", move=True, align="left", font=("Times New Roman", 18, "normal"))
    output.write(thechange, move=True, align="left", font=("Times New Roman", 18, "normal"))
    output.write(" at ", move=True, align="left", font=("Times New Roman", 18, "normal"))
    output.write(locationn.upper(), move=True, align="left", font=("Times New Roman", 18, "normal"))
    output.goto(-200,-250)

correct=1
def realtimecheck(locationn,thechange):
    global correct
    if locationn=="a1":
        if thechange==answer[0][0]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="a2":
        if thechange==answer[0][1]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="a3":
        if thechange==answer[0][2]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="a4":
        if thechange==answer[0][3]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="b1":
        if thechange==answer[1][0]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="b2":
        if thechange==answer[1][1]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="b3":
        if thechange==answer[1][2]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="b4":
        if thechange==answer[1][3]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="c1":
        if thechange==answer[2][0]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="c2":
        if thechange==answer[2][1]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="c3":
        if thechange==answer[2][2]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="c4":
        if thechange==answer[2][3]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="d1":
        if thechange==answer[3][0]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="d2":
        if thechange==answer[3][1]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="d3":
        if thechange==answer[3][2]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0
    if locationn=="d4":
        if thechange==answer[3][3]:
            lastmove(locationn,thechange)
            correct=1
        else:
            output.write("Incorrect Value", move=False, align="left", font=("Times New Roman", 18, "normal"))
            correct=0

def playgame(): #interacts with user and asks for input
    global realtime
    if thisgame[0].count(empty)<1 and thisgame[1].count(empty)<1 and thisgame[2].count(empty)<1 and thisgame[3].count(empty)<1:
            submit()
    else:
        pass
    if counter>2:
        userinputt=turtle.textinput("What do you want to do next?","Addval, remval or submit?")
        userinput=userinputt.lower()
        if userinput=="addval":
            output.clear()
            addvalue=turtle.textinput("Add a Value", "Where do you want to add the value? (eg. A4 or C2)")
            locationn=addvalue.lower()
            thechange=int(turtle.numinput("Enter number","This number will be added to the puzzle", default=None, minval=1, maxval=4))
            if realtime=="yes":
                realtimecheck(locationn,thechange)
            else:
                lastmove(locationn,thechange)
            try:
                return locationn
                return thechange
            finally:
                if correct==1:
                    changevalue(locationn,thechange)
                pass

        if userinput=="remval":
            output.clear()
            remvalue=turtle.textinput("Remove a Value", "Where do you want to remove the value from? (eg. B1 or D3")
            locationn=remvalue.lower()
            thechange=empty
            try:
                return locationn
                return thechange
            finally:
                changevalue(locationn,thechange)
        if userinput=="submit":
            submit()
        else:
            playgame()

counter=3
def submit(): #checks if the answer is correct or not
    global counter
    output.clear()
    for f in thisgame:
        if f.count(empty)>=1:
            output.write("The puzzle is not complete yet, keep playing!", move=False, align="left", font=("Times New Roman", 18, "normal"))
            break
        elif thisgame==answer:
            output.write("You have solved this puzzle!", move=False, align="left", font=("Times New Roman", 18, "normal"))
            counter=0
            try:
                return counter
            finally:
                print("Thank you for Playing!")
                break
        else:
            output.write("The solution is incorrect, try again!", move=False, align="left", font=("Times New Roman", 18, "normal"))
            break

while counter>2:
    playgame()
    counter=counter+1
