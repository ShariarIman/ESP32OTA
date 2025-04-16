import urequests as requests
import os

def check_for_update(url):
    response = requests.get(url + "/version.txt")
    with open("version.txt") as f:
        local_version = f.read().strip()

    remote_version = response.text.strip()

    if local_version != remote_version:
        print("New update found.")
        download_and_replace_files(url)
        return True
    return False

def download_and_replace_files(url):
    files = ["main.py", "version.txt"]  # Add other files as needed
    for file in files:
        r = requests.get(url + "/" + file)
        with open(file, "w") as f:
            f.write(r.text)
    print("Files updated. Rebooting...")
    import machine
    machine.reset()
