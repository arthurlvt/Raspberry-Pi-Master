# THIS PROGRAM ALLOWS TO FIND THE ADRESS OF THE LCD OR ANY COMPONENTS WICH USES I2C

import machine
sda = machine.Pin() # You need to enter the SDA Pin number
scl = machine.Pin() # You need to enter the SCL Pin number
i2c = machine.I2C(0,sda=sda,scl=scl, freq=400000)
print(i2c.scan())
