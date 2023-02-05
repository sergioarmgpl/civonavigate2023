import time
import board
import adafruit_dht
import psutil
import sys
import requests

# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
   if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(board.D22)

device = 1
url = 'http://172.16.0.152:3000/device'

def main():
   while True:
      temperature = sensor.temperature
      humidity = sensor.humidity
      print(temperature,humidity)
      json_data = {'d':device,'t':str(temperature),'h':str(humidity)}
      x = requests.post(url, json = json_data)
      print(x.text)
      time.sleep(1)
try:
  main()
except KeyboardInterrupt:
  pass
finally:
  sensor.exit()
