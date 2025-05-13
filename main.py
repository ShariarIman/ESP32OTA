import ota_updater

if ota_updater.check_for_update("https://raw.githubusercontent.com/ShariarIman/ESP32OTA/main", verbose=True):
    print("[OTA] Running updated code.")

print("Running main program.")
import time
from machine import Pin

led1 = Pin(2, Pin.OUT)   # Built-in LED on most ESP32 boards

while True:
    led1.on()
    time.sleep(0.5)
    led1.off()
    time.sleep(0.5)
