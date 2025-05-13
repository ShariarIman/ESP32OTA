import ota_updater

if ota_updater.check_for_update("https://raw.githubusercontent.com/ShariarIman/ESP32OTA/main", verbose=True):
    print("Hello OTA 1.3.1")
    print("[OTA] Running updated code.")

print("Running main program.")
