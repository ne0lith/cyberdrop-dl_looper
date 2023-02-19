import shutil
import datetime
import pathlib


def main():
    current_dir = pathlib.Path(__file__).parent.absolute()
    parent_dir = current_dir.parent
    logs_dir = parent_dir / "logs"
    archive_dir = logs_dir / "archives"

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
        shutil.copy(source, dest)
        print(f"Copied {source} to {dest}")


if __name__ == "__main__":
    main()
