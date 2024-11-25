# THIS PROGRAM ALLOWS TO READ THE TEMPERATURE AND HUMIDITY BY DHT11

from machine import Pin
import utime
from DHT11 import DHT11  # Ensure that DHT11.py is present

# Initialize the DHT11 sensor on GPIO 11
dht_sensor = DHT11(Pin(11))  # Replace 11 with the pin your DHT is connected to

while True:
    # Read temperature and humidity
    humidity, temperature = dht_sensor.read()
    
    # Check if the reading is valid
    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%")  # Display the values
    else:
        print("Sensor reading failed. Try again!")
    
    utime.sleep(2)  # Wait for 2 seconds before reading again
