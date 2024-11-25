# THIS PROGRAM ALLOWS YOU TO USE THE LED THAT IS ON YOUR RASPBERRY PI PICO JUST ABOVE THE BOOTSEL BUTTON.

from machine import Pin
import time

led = Pin(25, Pin.OUT) # THIS LED IS ON THE GPIO 25

while True:
  led.value(1)
  time.sleep(1)
  led.value(0)
  time.sleep(1)
