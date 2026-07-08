import hashlib
import json
import os
import time
from datetime import datetime
from colorama import Fore, Style, init

init()

HASH_DB = "hashes.json"


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def load_hashes():

    if not os.path.exists(HASH_DB):
        return {}

    with open(HASH_DB, "r") as file:
        return json.load(file)


def save_hashes(hashes):

    with open(HASH_DB, "w") as file:
        json.dump(hashes, file, indent=4)


def get_folder_hashes(folder_path):

    hashes = {}

    for file_name in os.listdir(folder_path):

        full_path = os.path.join(folder_path, file_name)

        if os.path.isfile(full_path):

            hashes[full_path] = calculate_hash(full_path)

    return hashes


def monitor_folder(folder_path):

    print("\nMonitoring folder...")
    print("Press CTRL + C to stop\n")

    old_hashes = get_folder_hashes(folder_path)

    try:

        while True:

            time.sleep(5)

            new_hashes = get_folder_hashes(folder_path)


            if old_hashes == new_hashes:

                print(
                    Fore.GREEN +
                    "✓ No changes detected."
                    + Style.RESET_ALL
                )

            else:

                print(
                    Fore.RED +
                    "\n⚠ Change detected!"
                    + Style.RESET_ALL
                )


                for file in new_hashes:

                    if file not in old_hashes:

                        print(
                            Fore.YELLOW +
                            f"+ New file: {os.path.basename(file)}"
                            + Style.RESET_ALL
                        )


                    elif old_hashes[file] != new_hashes[file]:

                        print(
                            Fore.RED +
                            f"✗ Modified: {os.path.basename(file)}"
                            + Style.RESET_ALL
                        )


                for file in old_hashes:

                    if file not in new_hashes:

                        print(
                            Fore.RED +
                            f"✗ Deleted: {os.path.basename(file)}"
                            + Style.RESET_ALL
                        )


                old_hashes = new_hashes


    except KeyboardInterrupt:

        print("\n\nMonitoring stopped.")



while True:

    print("\n===== File Integrity Checker =====")
    print("1. Monitor Folder")
    print("2. Exit")


    choice = input("\nEnter your choice: ")


    if choice == "1":

        folder_path = input("Enter folder path: ")

        if os.path.isdir(folder_path):

            monitor_folder(folder_path)

        else:

            print("\n❌ Folder not found.")


    elif choice == "2":

        print("\n👋 Exiting...")
        break


    else:

        print("\n❌ Invalid choice.")