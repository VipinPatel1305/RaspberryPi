
from guizero import App, Text, Picture
import time

currentFloor = 10
desiredFloor = -1
def checkFloorState():
    global currentFloor
    global desiredFloor

    if desiredFloor == -1:
        f = open("/home/pi/lift/floorState.txt", "r")
        desiredFloor = int(f.read())

    if desiredFloor < currentFloor:
        currentFloor = currentFloor - 1
        floorView.value = currentFloor
       
    elif desiredFloor > currentFloor:
        currentFloor = currentFloor + 1
        floorView.value = currentFloor
    else:
        f = open("/home/pi/lift/floorState.txt", "r")
        desiredFloor = int(f.read())
        if desiredFloor < currentFloor:
            print("going up")
        elif desiredFloor > currentFloor:
            print("going down")
        



textColor = "red"
app = App(title="Lift", height=600, width=560, bg = "black", layout="grid")
#app.full_screen = True
upArrow = Text(app, text = "⬆", size = 30, grid=[0,0,2,1], align="left")
upArrow.text_color = textColor

buttonTextSize = 50
buttonsView1 = Text(app, text = 1, size = buttonTextSize, grid=[3,0], align='left')
buttonsView1.text_color = textColor

buttonsView2 = Text(app, text = 2, size = buttonTextSize, grid=[4,0], align='right')
buttonsView2.text_color = textColor

floorView = Text(app, text = "10", font = "Seven Segment", size = 300, grid=[0,1,3,5], align="left")
floorView.text_color = textColor
row = 1

buttonsView3 = Text(app, text = 3, size = buttonTextSize, grid=[3,1], align='left')
buttonsView3.text_color = textColor
    
buttonsView4 = Text(app, text = 4, size = buttonTextSize, grid=[4, 1], align='right')
buttonsView4.text_color = textColor

buttonsView5 = Text(app, text = 5, size = buttonTextSize, grid=[3,2], align='left')
buttonsView5.text_color = textColor
    
buttonsView6 = Text(app, text = 6, size = buttonTextSize, grid=[4, 2], align='right')
buttonsView6.text_color = textColor

buttonsView7 = Text(app, text = 7, size = buttonTextSize, grid=[3,3], align='left')
buttonsView7.text_color = textColor
    
buttonsView8 = Text(app, text = 8, size = buttonTextSize, grid=[4, 3], align='right')
buttonsView8.text_color = textColor

buttonsView9 = Text(app, text = 9, size = buttonTextSize, grid=[3,4], align='left')
buttonsView9.text_color = textColor
    
buttonsView10 = Text(app, text = 10, size = buttonTextSize, grid=[4, 4], align='right')
buttonsView10.text_color = textColor

buttonsViewB1 = Text(app, text = "0", size = buttonTextSize - 5, grid=[3, 5], align='left')
buttonsViewB1.text_color = textColor

#buttonsViewB2 = Text(app, text = "B2", size = buttonTextSize - 5, grid=[4, 5], align='right')
#buttonsViewB2.text_color = textColor

downArrow = Text(app, text = "⬇", size = 30, grid=[0,6, 3, 1], align='left')
downArrow.text_color = textColor

openDoor = Text(app, text = "<|>", size = 30, grid=[3,6], align='left')
openDoor.text_color = textColor

closeDoor = Text(app, text = ">|<", size = 30, grid=[4,6], align='right')
closeDoor.text_color = textColor

#openDoor = Picture(app, image="open.png", grid=[1,6], align="bottom")
#closeDoor = Picture(app, image="close.png", grid=[2,6], align="bottom")

floorView.repeat(600, checkFloorState)
checkFloorState()
app.display()
