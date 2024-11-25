import utime
import machine
from machine import Pin, I2C

class DS3231_I2C:
    ADDRESS = 0x68  # I2C address of the DS3231
    REGISTER = 0x00  # Register to start reading from

    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        self.reg = 0x00

    def set_time(self, NowTime):
        """
        Sets the time and date on the DS3231.
        """
        try:
            self.i2c.writeto_mem(int(self.addr), int(self.reg), NowTime)
            print("Time and date successfully set.")
        except OSError as e:
            print("Error while setting the time:", e)

    def read_time(self):
        """
        Reads the time and date from the DS3231.
        Returns a list of 7 elements containing RTC data.
        """
        try:
            # Read the first 7 bytes (seconds, minutes, hours, day, month, year, weekday)
            data = self.i2c.readfrom_mem(int(self.addr), int(self.reg), 7)
            print("Raw RTC data:", data)  # Display raw data
            if len(data) == 7:
                return data
            else:
                print(f"Error: Incorrect number of data bytes. Returned size: {len(data)}")
                return None
        except OSError as e:
            print("Error while reading the RTC:", e)
            return None

# Function to convert BCD to decimal
def bcd_to_dec(bcd):
    return (bcd & 0x0F) + ((bcd >> 4) * 10)

# I2C configuration
i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # Replace pins if necessary
rtc = DS3231_I2C(i2c)  # Create an instance of the DS3231 RTC module

# Function to read and display the time and date
def read_time():
    # Read the current time from the DS3231
    t = rtc.read_time()  # Returns a list of 7 values [seconds, minutes, hours, day, month, year, weekday]
    
    if t is not None:
        # Verify the size of the data before attempting to access it
        if len(t) < 7:
            print("Error: Insufficient data to read the time and date.")
            return
        
        # Convert BCD values to decimal
        second = bcd_to_dec(t[0])
        minute = bcd_to_dec(t[1])
        hour = bcd_to_dec(t[2])
        day = bcd_to_dec(t[3])
        month = bcd_to_dec(t[4])
        year = bcd_to_dec(t[5]) + 2000  # Add 2000 for the year
        week_day = t[6]

        # Format the time and date
        time_str = "{:02}:{:02}:{:02}".format(hour, minute, second)
        date_str = "{:02}/{:02}/{}".format(day, month, year)
        
        # Display the time and date
        print("Time: ", time_str)
        print("Date: ", date_str)
        print("Weekday: ", ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][week_day])

# Main loop to read and display the time every second
while True:
    print("Reading time...")
    read_time()  # Read and display the time
    utime.sleep(1)  # Wait for one second before the next reading
