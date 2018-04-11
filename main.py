import requests
import time
import simpleaudio as sa

song = sa.WaveObject.from_wave_file('Napalm Death - You Suffer.wav')
apiUrl = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'

def getPercent():
    response = requests.get(apiUrl).json()
    value = response[0]['percent_change_1h']
    return value

def intervalCheck():
    currentP = float(getPercent())
    print(currentP)
    if(currentP < 0):
        song.play()
    time.sleep(30)

while True:
    intervalCheck()
