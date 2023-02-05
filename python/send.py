import time
import board
import adafruit_dht
import psutil
import sys

# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
   if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(board.D22)

host="192.168.0.243"

def main():
   while True:
      temperature = sensor.temperature
      humidity = sensor.humidity
      print(temperature,humidity)
      time.sleep(2)
try:
  main()
except KeyboardInterrupt:
  pass
finally:
  sensor.exit()
