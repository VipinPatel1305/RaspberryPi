from guizero import App
from guizero import App, Text
from datetime import datetime
import Adafruit_DHT as dht
DHT = 4

temp = 25.7
hum = 67.4
now = datetime.now()
dateValue = now.strftime("%a %d %b")
timeDot = False

def updateDate():
    dateValue = datetime.now().strftime("%a %d %b")
    dateText.value = dateValue

def updateTime():
    now = datetime.now()
    hour =  now.strftime("%I")
    min =  now.strftime("%M")
    hourText.value = hour
    minText.value = min
    global timeDot
    if timeDot:
        timeDot = False
        dotText.text_color = "black"
    else:
        timeDot = True
        dotText.text_color = "yellow"

def updateWeatherStats():
    hum, temp = dht.read_retry(dht.DHT22, DHT)
    tempText.value = ('{0:0.1f}*C'.format(temp))
    humText.value = ('{0:0.1f}%'.format(hum))


textColor = "yellow"
app = App(title="Clock", height=480, width=620, bg = "black", layout="grid")
app.full_screen = False
dateText = Text(app, text = "1", size = 50, grid=[0,0,5,1])
dateText.text_color = textColor
timeSize=150
hourText = Text(app, text = "1", size = timeSize, font = "Seven Segment", grid=[0,1])
dotText = Text(app, text = "1", size = timeSize,grid=[2,1])
minText = Text(app, text = "1", size = timeSize, font = "Seven Segment",grid=[3,1])

hourText.text_color = textColor
minText.text_color = textColor
dotText.text_color = textColor
dotText.value = ":"

tempText = Text(app, text = "25*C", size = 35, grid=[4,1])
humText = Text(app, text = "68.5%", size = 35, grid=[4,2,5,1])
tempText.text_color = textColor
humText.text_color = textColor

dateText.value = dateValue
dateText.repeat(60000, updateDate)
hourText.repeat(1000, updateTime)
humText.repeat(30000, updateWeatherStats)
app.display()

