from machine import Pin, I2C

# Initialize I2C bus 1 (or 0) using GPIO 2 (SDA) and GPIO 3 (SCL) for example
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
print("Scanning for I2C devices on bus 1...")
devices = i2c.scan()

if devices:
    print("I2C devices found:", devices)
else:
    print("No I2C devices found.")
