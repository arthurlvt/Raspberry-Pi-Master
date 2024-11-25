# TO MAKE THIS COMPONENT FUNCTIONAL, PUT OFF ALL SWITCHES EXCEPTED THE 1 OF RIGHT BLOCK 

import sys # Importing sys library
import time # Importing time library
from mfrc522 import SimpleMFRC522 # Importing mfrc522 library to use RFID reader
reader = SimpleMFRC522()
import warnings # Importing warnings to remove useless warnings
warnings.filterwarnings("ignore")

vibration_pin = 13 # The vibrator sensor is connected by the pin 13

GPIO.setmode(GPIO.BOARD) # The mode is defined as BOARD MODE
GPIO.setup(vibration_pin, GPIO.OUT) # The vibrator is defined as Output Sensor

try:
  for i in range(1):
    print('Please put your tag on RFID reader')
    authenticated = False
    
    while not authenticated:
      try:
        id, text = reader.read()
        authenticated = True
      except Exception as e:
        print(f'Auth Error : {e}')
        time.sleep(1)
    
    if text.strip():
      print(f'Tag ID: {id}')
      if id == '123456654321':
        name = 'John'
        print('Welcome', name, '!')
        GPIO.output(vibration_pin, HIGH)
        time.sleep(0.1)
        GPIO.output(vibration_pin, LOW)
      else:
        print(f"ID: {id}, Content: {text}")
    else:
      print('Invalid tag ! Rebooting in progress...')
      GPIO.output(vibration_pin, GPIO.HIGH)
      time.sleep(0.5)
      GPIO.output(vibration_pin, GPIO.LOW)
      sys.exit(0)

except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()
