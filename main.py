import ota_updater

if ota_updater.check_for_update("https://raw.githubusercontent.com/ShariarIman/ESP32OTA/main", verbose=True):
    print("[OTA] Running updated code.")

print("Running main program.")
import time
from machine import Pin

import time
from machine import Pin

# Define LED pins
led1 = Pin(17, Pin.OUT)
led2 = Pin(4, Pin.OUT)
led3 = Pin(2, Pin.OUT)

# LED pattern sequence (each tuple is a step: (GPIO2, GPIO4, GPIO17))
pattern = [
    (1, 0, 0),
    (1, 1, 0),
    (1, 1, 1),
    (0, 0, 0),
]

while True:
    for state in pattern:
        led1.value(state[0])
        led2.value(state[1])
        led3.value(state[2])
        time.sleep(0.5)
