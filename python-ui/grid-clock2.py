from guizero import App, Picture
from guizero import App, Text
from datetime import datetime
import requests
from os.path import exists
from pathlib import Path
import urllib.request
import Adafruit_DHT as dht
from gpiozero import CPUTemperature
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
    #hum, temp = dht.read_retry(dht.DHT22, DHT)
    #tempText.value = ('{0:0.1f}*C'.format(temp))
    #humText.value = ('{0:0.1f}%'.format(hum))
    cpu = CPUTemperature()
    tempText.value = ('CPU: {0:0.1f}*C'.format(cpu.temperature))
def outsideWeather():
    api_url = "https://api.openweathermap.org/data/2.5/weather?lat=12.9789637&lon=77.7582743&appid=391f2d7402f1682aca33e1b678f4a4b7&units=metric"
    response = requests.get(api_url)
    weatherDet.value = response.json()['weather'][0]['description']
    iconFile = response.json()['weather'][0]['icon'] + "@2x.png"
    my_file = Path(iconFile)
    if my_file.is_file() == False:
        url = "https://openweathermap.org/img/wn/" + iconFile
        urllib.request.urlretrieve(url, "/home/pi/python-ui/"+iconFile)
    picture.value = "/home/pi/python-ui/"+iconFile
    outTempText.value = ('{0:0.1f}*C'.format(response.json()['main']['temp']))
    outHumText.value = ('{0:0.1f}%'.format(response.json()['main']['humidity']))
    outTempValue = response.json()['main']['temp']
    if outTempValue < 26:
        clothIcon = Picture(app, image="/home/pi/python-ui/jacket.png", grid=[2, 5, 2, 1], align="bottom")
    else:
        clothIcon = Picture(app, image="/home/pi/python-ui/tshirt.png", grid=[2, 5, 2, 1], align="bottom")

textColor = "green"
timeSize=190
app = App(title="Clock", height=480, width=800, bg = "black", layout="grid")
app.full_screen = True
dateText = Text(app, text = "1", size = 50, grid=[0,0,4,1])
hourText = Text(app, text = "1", size = timeSize, font = "Seven Segment", grid=[0,1,1,4])
dotText = Text(app, text = "1", size = timeSize,grid=[1,1,1,4])
minText = Text(app, text = "1", size = timeSize, font = "Seven Segment",grid=[2,1,1,4])
outTempText = Text(app, text = "0*C", size = 35, grid=[3,1])
outHumText = Text(app, text = "0*C", size = 35, grid=[3,2])
picture = Picture(app, image="/home/pi/python-ui/10d@2x.png", grid=[3, 3], align="bottom")
weatherDet = Text(app, text = "Rain", size = 25,grid=[3,4], align="top")
tempText = Text(app, text = "5*C", size = 35, grid=[0,5])
humText = Text(app, text = "8.5%", size = 35, grid=[1,5])
clothIcon = Picture(app, image="/home/pi/python-ui/tshirt.png", grid=[2, 5, 2, 1], align="bottom")

hourText.text_color = textColor
minText.text_color = textColor
dotText.text_color = textColor
dotText.value = ":"
weatherDet.text_color = textColor
outTempText.text_color = textColor
outHumText.text_color = textColor
tempText.text_color = textColor
humText.text_color = textColor
dateText.text_color = textColor

dateText.value = dateValue
dateText.repeat(60000, updateDate)
hourText.repeat(1000, updateTime)
humText.repeat(30000, updateWeatherStats)
weatherDet.repeat(300000, outsideWeather)
outsideWeather()
updateWeatherStats()
app.display()

