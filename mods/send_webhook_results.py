import re
import sys
import requests
import argparse
from pathlib import Path
from datetime import datetime

webhook_url = "YOUR_WEBHOOK_URL"


def read_results(profile_name, machine_name):
    current_dir = Path(__file__).resolve().parent
    profile_dir = current_dir.parent / "AppData" / "Configs" / profile_name
    log_file = profile_dir / "Logs" / "downloader.log"

    patterns = {
        "Organized: Audio Files": re.compile(r"Organized: (\d+) Audio Files"),
        "Organized: Image Files": re.compile(r"Organized: (\d+) Image Files"),
        "Organized: Video Files": re.compile(r"Organized: (\d+) Video Files"),
        "Organized: Other Files": re.compile(r"Organized: (\d+) Other Files"),
        "Downloaded files": re.compile(r"Downloaded (\d+) files"),
        "Previously Downloaded files": re.compile(r"Previously Downloaded (\d+) files"),
        "Skipped By Config files": re.compile(r"Skipped By Config (\d+) files"),
        "Failed files": re.compile(r"Failed (\d+) files"),
        "Scrape Failures (404 HTTP Status)": re.compile(
            r"Scrape Failures \(404 HTTP Status\): (\d+)"
        ),
        "Scrape Failures (403 HTTP Status)": re.compile(
            r"Scrape Failures \(403 HTTP Status\): (\d+)"
        ),
        "Scrape Failures (Unknown)": re.compile(r"Scrape Failures \(Unknown\): (\d+)"),
        "Scrape Failures (410 HTTP Status)": re.compile(
            r"Scrape Failures \(410 HTTP Status\): (\d+)"
        ),
        "Download Failures (404 HTTP Status)": re.compile(
            r"Download Failures \(404 HTTP Status\): (\d+)"
        ),
        "Download Failures (403 HTTP Status)": re.compile(
            r"Download Failures \(403 HTTP Status\): (\d+)"
        ),
        "Download Failures (418 HTTP Status)": re.compile(
            r"Download Failures \(418 HTTP Status\): (\d+)"
        ),
        "Download Failures (503 HTTP Status)": re.compile(
            r"Download Failures \(503 HTTP Status\): (\d+)"
        ),
        "Download Failures (1 HTTP Status)": re.compile(
            r"Download Failures \(1 HTTP Status\): (\d+)"
        ),
    }

    results = {}
    found_start = False
    start_time = None

    try:
        with open(log_file, "r") as file:
            lines = file.readlines()

            for line in lines:
                if not found_start:
                    match_start = re.search(
                        r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line
                    )
                    if match_start:
                        start_time = datetime.strptime(
                            match_start.group(0), "%Y-%m-%d %H:%M:%S"
                        )
                        found_start = True

                if "Sorting Downloads: Please Wait" in line:
                    continue

                if found_start:
                    for key, pattern in patterns.items():
                        match = pattern.search(line)
                        if match:
                            results[key] = int(match.group(1))

                    match_end = re.search(
                        r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line
                    )
                    if match_end:
                        end_time = datetime.strptime(
                            match_end.group(0), "%Y-%m-%d %H:%M:%S"
                        )
                        time_taken = end_time - start_time
                        results["Time Taken"] = str(time_taken)

                        if machine_name is not None and machine_name not in [
                            "",
                            "None",
                            "none",
                        ]:
                            results["Machine Name"] = machine_name

    except FileNotFoundError:
        print(f"Log file not found: {log_file}")

    return results


def send_webhook(results, webhook_url, profile_name):
    message_content = f"Results for profile '{profile_name}':\n"
    for key, value in results.items():
        message_content += f"{key}: {value}\n"

    data = {"content": message_content}

    headers = {"Content-Type": "application/json"}

    response = requests.post(webhook_url, json=data, headers=headers)

    if response.status_code == 204:
        print("Webhook sent successfully")
    elif response.status_code == 200:
        print("Webhook sent successfully (with content)")
    else:
        print(
            f"Failed to send webhook. Status code: {response.status_code}, Response: {response.text}"
        )


def main():
    parser = argparse.ArgumentParser(description="Send webhook for a given profile.")
    parser.add_argument("profile_name", help="Name of the profile")
    parser.add_argument("machine_name", help="Name of the machine running the scraper")

    args = parser.parse_args()

    if not args.profile_name:
        print("Error: Missing profile_name argument.")
        parser.print_help()
        input("Press Enter to exit...")
        sys.exit(1)

    results = read_results(args.profile_name, args.machine_name)

    if not results:
        print(f"No results found for profile '{args.profile_name}'. Exiting.")
        sys.exit(1)

    send_webhook(results, webhook_url, args.profile_name)


if __name__ == "__main__":
    main()
