import argparse
import sys
import shutil
import datetime
from pathlib import Path


def backup_logs(profile_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d__%I_%M_%S_%p")

    logs_dir = "Logs"
    archived_logs_dir = "Archived_Logs"

    current_dir = Path(__file__).resolve().parent
    profile_dir = current_dir.parent / "AppData" / "Configs" / profile_name

    logs_path = profile_dir / logs_dir

    archived_logs_path = profile_dir / archived_logs_dir
    archived_logs_path.mkdir(parents=True, exist_ok=True)

    backup_logs_path = archived_logs_path / timestamp
    shutil.copytree(logs_path, backup_logs_path)

    urls_file = profile_dir / "URLS.txt"
    shutil.copy(urls_file, backup_logs_path / "URLS.txt")

    print(f"Logs backed up successfully to {backup_logs_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Backup and archive Logs for a given profile."
    )
    parser.add_argument("profile_name", help="Name of the profile")

    args = parser.parse_args()

    if not args.profile_name:
        print("Error: Missing profile_name argument.")
        parser.print_help()
        input("Press Enter to exit...")
        sys.exit(1)

    backup_logs(args.profile_name)


if __name__ == "__main__":
    main()
