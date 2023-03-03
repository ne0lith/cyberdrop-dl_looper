import re
import pathlib
import requests
from datetime import datetime


def send_discord_webhook(webhook_url, message):
    payload = {"content": message}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(webhook_url, json=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending webhook: {e}")
        return None
    else:
        return response.status_code


def parse_log_file(log_file):
    files_complete = None
    files_skipped = None
    files_failed = None

    pattern = re.compile(
        r"\[green\]Files Complete: (\d+)\[/green\] - \[yellow\]Files Skipped: (\d+)\[/yellow\] - \[red\]Files Failed: (\d+)\[/red\]"
    )

    with log_file.open("r") as f:
        for line in reversed(f.readlines()):
            match = pattern.search(line)
            if match:
                files_complete = int(match.group(1))
                files_skipped = int(match.group(2))
                files_failed = int(match.group(3))
                break

    return files_complete, files_skipped, files_failed


def main():
    current_dir = pathlib.Path(__file__).parent.absolute()
    parent_dir = current_dir.parent
    logs_dir = parent_dir / "logs"
    log_file = logs_dir / "downloader.log"
    webhook_file = logs_dir / ".webhook"

    if webhook_file.exists():
        try:
            with webhook_file.open("r") as f:
                webhook_url = f.read().strip()
        except Exception as e:
            print(f"Error reading webhook file: {e}")
            webhook_url = None
    else:
        webhook_url = None

    if not webhook_url:
        print("No webhook url found")
        return

    if not log_file.exists():
        print(f"Log file does not exist: {log_file}")
        return

    files_complete, files_skipped, files_failed = parse_log_file(log_file)

    if None in (files_complete, files_skipped, files_failed):
        print(f"Incomplete log file: {log_file}")
        return

    current_time = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    message = f"Downloaded: {files_complete}\nSkipped: {files_skipped}\nFailed: {files_failed}\nCompleted as of: {current_time}"

    status_code = send_discord_webhook(webhook_url, message)
    print(f"Discord webhook status code: {status_code}")
    print(message)


if __name__ == "__main__":
    main()
