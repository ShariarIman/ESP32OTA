import ota_updater

if ota_updater.check_for_update("https://raw.githubusercontent.com/ShariarIman/ESP32OTA/main", verbose=True):
    print("[OTA] Running updated code.")

print("Running main program.")
import ota_updater

# OTA check
if ota_updater.check_for_update("https://raw.githubusercontent.com/ShariarIman/ESP32OTA/main", verbose=True):
    print("[OTA] Running updated code.")

# --- Main Program Starts Here ---
print("Running main program.")

import time
from machine import Pin

# LED pins
led2 = Pin(2, Pin.OUT)
led4 = Pin(4, Pin.OUT)
led17 = Pin(17, Pin.OUT)

# Sensor pin (Laser sensor digital output)
sensor = Pin(18, Pin.IN)

# LED pattern sequence
pattern = [
    (1, 0, 0),
    (1, 1, 0),
    (1, 1, 1),
    (0, 0, 0),
]

while True:
    if sensor.value() == 1:
        print("🚨 Object detected!")
        for step in pattern:
            led2.value(step[0])
            led4.value(step[1])
            led17.value(step[2])
            time.sleep(0.5)
    else:
        # Clear LEDs when nothing is detected
        led2.off()
        led4.off()
        led17.off()
        time.sleep(0.1)
