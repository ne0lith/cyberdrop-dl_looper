from pathlib import Path

current_dir = Path(__file__).resolve().parent


def update_urls_file(all_urls_path, latest_forum_posts_path):
    try:
        all_urls = all_urls_path.read_text().splitlines()
    except FileNotFoundError:
        print(f"Could not find {all_urls_path}")
        return

    try:
        latest_forum_posts = latest_forum_posts_path.read_text().splitlines()
    except FileNotFoundError:
        print(f"Could not find {latest_forum_posts_path}")
        return

    all_urls = [url for url in all_urls if url]
    latest_forum_posts = [url for url in latest_forum_posts if url]

    try:
        thread_title_to_url = {}
        for thread_url in latest_forum_posts:
            thread_title = thread_url.split("/")[-2]
            thread_title_to_url[thread_title] = thread_url
    except IndexError:
        print("Could not parse thread title from thread URL.")
        return

    updated_all_urls = []
    for url in all_urls:
        thread_title = url.split("/")[-2]
        if thread_title in thread_title_to_url:
            latest_url = thread_title_to_url[thread_title]
            updated_all_urls.append(latest_url)
        else:
            updated_all_urls.append(url)

    print("Updated URLs:")
    for url in updated_all_urls:
        print(url)

    try:
        all_urls_path.write_text("\n".join(updated_all_urls))
    except Exception as e:
        print(f"Could not write to {all_urls_path}: {e}")
        return


def run_it_up(urls_file_path=None, latest_forum_posts_path=None):
    all_urls_path = Path(urls_file_path)
    latest_forum_posts_path = Path(latest_forum_posts_path)
    confirmation_file_path = current_dir / ".confirmation"

    if confirmation_file_path.exists():
        update_urls_file(all_urls_path, latest_forum_posts_path)
    else:
        file_name = all_urls_path.name
        response = input(
            f"Are you sure you want to irreversibly alter the {file_name} file?\nThis action cannot be undone.\nType 'y' to continue.\nYou will not be asked again as long as .confirmation exists: "
        )
        if response.lower() == "y":
            confirmation_file_path.touch()
            update_urls_file(all_urls_path, latest_forum_posts_path)
        else:
            print("Operation cancelled.")


def main():
    current_dir = Path(__file__).resolve().parent
    logs_dir = current_dir.parent / "logs"
    urls_txt = logs_dir / "urls.txt"
    latest_forum_post_txt = logs_dir / "latest_forum_post.txt"

    run_it_up(urls_file_path=urls_txt, latest_forum_posts_path=latest_forum_post_txt)


if __name__ == "__main__":
    print("Running latest_thread_to_urls.py")
    main()
