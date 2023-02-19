import datetime
import pathlib
import shutil

current_dir = pathlib.Path(__file__).parent.absolute()
parent_dir = current_dir.parent
logs_dir = parent_dir / "logs"
archive_dir = logs_dir / "archives"
archive_file = current_dir / ".archive"


def ask_to_archive():
    response = input(
        "No confirmation file found.\nWould you like to start archiving ('errored_urls.csv', 'unsupported_urls.csv', 'downloader.log') now? (y/n) "
    )
    response = response.strip().lower()
    if response == "y":
        with open(archive_file, "w") as f:
            f.write(response)
    return response == "y"


def main():
    if archive_file.exists():
        with open(archive_file, "r") as f:
            should_archive = f.read().strip() == "y"
    else:
        should_archive = ask_to_archive()

    if should_archive:
        print("Archiving files...")
        archive_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        files_to_backup = [
            ("errored_urls.csv", f"errored_urls.{timestamp}.csv"),
            ("unsupported_urls.csv", f"unsupported_urls.{timestamp}.csv"),
            ("downloader.log", f"downloader.{timestamp}.log"),
        ]

        for old_name, new_name in files_to_backup:
            source = logs_dir / old_name
            dest = archive_dir / new_name
            try:
                shutil.copy(source, dest)
                print(f"Copied {source} to {dest}")
            except FileNotFoundError:
                print(f"File not found: {source}. May be your first run. Skipping...")

        print("Archiving complete.")
    else:
        print("Not archiving files.")


if __name__ == "__main__":
    print("Running archive_logs.py")
    main()
