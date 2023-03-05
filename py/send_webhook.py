import re
import pathlib
from datetime import datetime


def check_dependencies(packages):
    import importlib
    import subprocess

    for package in packages:
        try:
            importlib.import_module(package)
            print(f"{package} is already installed.")
        except ImportError:
            print(f"{package} is not installed. Installing...")
            subprocess.check_call(["pip", "install", package])


def set_timetaken(t_seconds):
    t_seconds = int(t_seconds)
    if t_seconds >= 3600:
        hours = t_seconds // 3600
        minutes = (t_seconds % 3600) // 60
        seconds = t_seconds % 60
        hours, minutes, seconds = str(hours), str(minutes), str(seconds)
        output = f"Scrape took: {hours}h {minutes}m {seconds}s"
    elif t_seconds >= 60 and t_seconds < 3600:
        minutes = t_seconds // 60
        seconds = t_seconds % 60
        minutes, seconds = str(minutes), str(seconds)
        output = f"Scrape took: {minutes} minutes and {seconds} seconds"
    else:
        t_seconds = str(t_seconds)
        output = f"Scrape took: {t_seconds} seconds"
    return output


def calculate_timetaken(log_file):
    try:
        pattern = r"^(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}):"
        with open(log_file, "r") as f:
            first_timestamp = None
            last_timestamp = None
            for line in f:
                match = re.match(pattern, line)
                if match:
                    timestamp = match.group(1)
                    if not first_timestamp:
                        first_timestamp = timestamp
                    last_timestamp = timestamp
        if first_timestamp and last_timestamp:
            fmt = "%Y-%m-%d %H:%M:%S,%f"
            first_dt = datetime.strptime(first_timestamp, fmt)
            last_dt = datetime.strptime(last_timestamp, fmt)
            time_diff = (last_dt - first_dt).total_seconds()
            return int(time_diff)
    except Exception as e:
        print(f"Error calculating timetaken: {e}")
        return None


def send_discord_embed(webhook_url, downloaded, failed, skipped, total_time):
    import random
    from discord_webhook import DiscordWebhook, DiscordEmbed

    webhook = DiscordWebhook(url=webhook_url)
    color_choice = random.choice(["B29DD9", "FDFD98", "FE6B64", "77DD77", "779ECB"])
    embed = DiscordEmbed(
        title="Cyberdrop-DL Stats",
        color=color_choice,
        rate_limit_retry=True,
    )
    embed.set_footer(text=set_timetaken(int(total_time)))
    embed.set_timestamp()
    embed.add_embed_field(name="Downloaded", value=f"{str(downloaded)}", inline=True)
    embed.add_embed_field(name="Failed", value=f"{str(failed)}", inline=True)
    embed.add_embed_field(name="Skipped", value=f"{str(skipped)}", inline=True)
    webhook.add_embed(embed)
    webhook.execute()


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
            check_dependencies(["discord_webhook"])
        except Exception as e:
            print(f"Error checking dependencies: {e}")
            return
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

    if files_complete >= 1:
        send_discord_embed(
            webhook_url,
            files_complete,
            files_failed,
            files_skipped,
            calculate_timetaken(log_file),
        )
    else:
        print("Nothing downloaded, not sending webhook message.")


if __name__ == "__main__":
    main()
