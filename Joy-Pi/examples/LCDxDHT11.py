# THIS PROJECT ALLOWS TO LEARN HOW TO USE LCD AND ALSO DHT11 AT THE SAME TIME
# DHT11 IS LITERALLY A DIGITAL HUMIDITY AND TEMPERATURE SENSOR WITH ACCURACY OF ±5%
# YOU NEED TO INSTALL 2 MORE LIBRARIES : adafruit-circuitpython-charlcd and Adafruit_DHT.
# TO INSTALL BLINKA, YOU SHOULD FOLLOW THIS PAGE: https://gallaugher.com/makersnack-installing-circuitpython-on-a-raspberry-pi/
# TO MAKE THIS COMPONENT FUNCTIONAL, PUT OFF ALL SWITCHES

import time # Importing time
import datetime as dt # Importing datetime
import board # It's installed with Blinka
import busio # It's installed with Blinka
import adafruit_character_lcd.character_lcd_i2c as character lcd # This library allows to do a lot of thinks with sensors and components
import Adafruit_DHT # This library allows to use DHT11 (or DHT22 if you have it)

# Number of columns in the LCD screen
lcd_columns = '16' # Don't try to change it, it won't change

# Number of rows in the LCD screen
lcd_rows = '2' # Don't try to change it, it won't change

# Setup of DHT11
sensor = Adafruit_DHT.DHT11
dht_pin = 4

i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)
humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)

lcd.backlight = True # Screen Display ON

try:
  while True:
        now = dt.datetime.now()
        lcd.message ='   ' + now.strftime('%d/%m/%Y') + '\n' + '' + now.strftime('%X') + ' | ' + str(temperature) + 'C'
except KeyboardInterrupt:
  lcd.clear() # REMOVE ALL ELEMENT ON THE SCREEN
  lcd.backlight = False # Screen Display OFF
