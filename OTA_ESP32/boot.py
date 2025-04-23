def connect_wifi():
    import network
    import time

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('STARLINK', 'spacex69')

    timeout = 20
    while not wlan.isconnected() and timeout > 0:
        print("Waiting for connection...")
        time.sleep(1)
        timeout -= 1

    if wlan.isconnected():
        print("Connected:", wlan.ifconfig())
    else:
        print("Failed to connect to Wi-Fi")

connect_wifi()
