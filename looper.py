import os
import subprocess
import time


def main():
    loop_count = 0
    loop_limit = 10

    while True:
        os.system("cls")

        print("Cyberdrop-DL looper.py")

        subprocess.run(["python", "py/upgrade_pip_package.py", "cyberdrop-dl"])
        os.system("cls")
        subprocess.run(["python", "py/latest_thread_to_urls.py"])
        os.system("cls")
        subprocess.run(["python", "py/archive_logs.py"])
        os.system("cls")

        cdl_version = subprocess.run(
            ["cyberdrop-dl", "--version"], capture_output=True, text=True
        ).stdout.split(" ")[1]

        cdl_version = cdl_version.strip()
        title = f'{cdl_version}: Looped ({loop_count}) times. -- {time.strftime("%I:%M %p")}'

        os.system("title " + title)

        subprocess.run(["cyberdrop-dl", "--config-file", "config.yaml"])

        loop_count += 1
        if loop_count == loop_limit:
            print("Sleeping for 3 hours...")
            time.sleep(10800)
            loop_count = 0


if __name__ == "__main__":
    main()
