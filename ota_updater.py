import urequests as requests
import machine
import os

def check_for_update(base_url, verbose=False):
    try:
        # Get remote version
        remote_version_url = base_url + "/version.txt"
        r = requests.get(remote_version_url)
        remote_version = r.text.strip()
        r.close()

        # Get local version
        try:
            with open("version.txt") as f:
                local_version = f.read().strip()
        except OSError:
            local_version = "0.0.0"  # Assume no version if file missing

        if verbose:
            print("Local version:", local_version)
            print("Remote version:", remote_version)

        if remote_version != local_version:
            print("[OTA] New version found. Updating...")
            download_and_replace_files(base_url)
            return True
        else:
            print("[OTA] No update available.")
            return False

    except Exception as e:
        print("[OTA] Update check failed:", e)
        return False

def download_and_replace_files(base_url):
    try:
        # Get file list from remote files.txt
        r = requests.get(base_url + "/files.txt")
        file_list = r.text.strip().split(",")
        r.close()

        for filename in file_list:
            filename = filename.strip()
            if not filename:
                continue

            print(f"[OTA] Updating {filename}...")
            try:
                r = requests.get(base_url + f"/{filename}")
                tmp_filename = filename + ".tmp"

                with open(tmp_filename, "w") as f:
                    f.write(r.text)
                r.close()

                # Replace old file with new
                os.remove(filename)
                os.rename(tmp_filename, filename)
            except Exception as e:
                print(f"[OTA] Failed to update {filename}:", e)

        print("[OTA] Update complete. Rebooting...")
        machine.reset()

    except Exception as e:
        print("[OTA] Failed to download update list:", e)
