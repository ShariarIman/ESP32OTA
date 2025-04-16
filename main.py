from machine import Pin
import time

# List of GPIO pins connected to LEDs (edit as needed)
led_pin = [2]

# Initialize LED pins as outputs
leds = [Pin(pin, Pin.OUT) for pin in led_pin]

def blink_all(delay=0.3):
    while True:
        # Turn all LEDs ON
        for led in led:
            led.value(1)
        time.sleep(delay)
        
        # Turn all LEDs OFF
        for led in led:
            led.value(0)
        time.sleep(delay)

blink_all()
