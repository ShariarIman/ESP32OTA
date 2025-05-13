import ota_updater

if ota_updater.check_for_update("https://raw.githubusercontent.com/ShariarIman/ESP32OTA/main", verbose=True):
    print("[OTA] Running updated code.")

print("Running main program.")
import time
from machine import Pin

led = Pin(2, Pin.OUT)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
