# THIS PROGRAM ALLOWS TO DEFINE TIME IN THE BATTERY

from machine import I2C, Pin
import utime

# Initialize I2C with a frequency of 100 kHz
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

DS3231_ADDRESS = 0x68  # DS3231 address

# Function to convert BCD values to decimal
def bcd_to_dec(bcd):
    return (bcd // 16) * 10 + (bcd % 16)

# Function to set the time on the DS3231
def set_rtc_time(hour, minute, second, day, month, year, weekday):
    # Convert values to BCD
    second_bcd = (second // 10) << 4 | (second % 10)
    minute_bcd = (minute // 10) << 4 | (minute % 10)
    hour_bcd = (hour // 10) << 4 | (hour % 10)
    day_bcd = (day // 10) << 4 | (day % 10)
    month_bcd = (month // 10) << 4 | (month % 10)
    year_bcd = ((year - 2000) // 10) << 4 | ((year - 2000) % 10)
    weekday_bcd = (weekday // 10) << 4 | (weekday % 10)

    # Write the values to the DS3231
    i2c.writeto_mem(DS3231_ADDRESS, 0x00, bytearray([second_bcd, minute_bcd, hour_bcd, weekday_bcd, day_bcd, month_bcd, year_bcd]))

# Set a date and time (example: 10:30:00, August 12, 2024, Monday)
set_rtc_time(18, 37, 40, 16, 11, 2024, 7)  # 1 = Monday

# Verify if the time is correctly programmed
while True:
    try:
        # Read the time from the DS3231 (first 7 bytes)
        time_data = i2c.readfrom_mem(DS3231_ADDRESS, 0x00, 7)
        second = bcd_to_dec(time_data[0] & 0x7F)  # Mask the alert bit
        minute = bcd_to_dec(time_data[1])
        hour = bcd_to_dec(time_data[2] & 0x3F)  # Mask AM/PM bits
        weekday = bcd_to_dec(time_data[3])
        day = bcd_to_dec(time_data[4])
        month = bcd_to_dec(time_data[5])
        year = bcd_to_dec(time_data[6]) + 2000  # Add 2000 to get the full year
        
        # Display the time read in a readable format
        print("Time: {:02}:{:02}:{:02} - Date: {:02}/{:02}/{:04} - Weekday: {}".format(
            hour, minute, second, day, month, year, ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][weekday - 1]
        ))
    except Exception as e:
        print("Error while reading:", e)

    utime.sleep(1)  # 1-second delay
