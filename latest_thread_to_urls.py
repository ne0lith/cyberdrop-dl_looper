import os

current_dir = os.path.dirname(os.path.realpath(__file__))
os.cwd(current_dir)


def update_urls_file(all_urls_path, latest_forum_posts_path):
    try:
        with open(all_urls_path, "r") as all_urls_file:
            all_urls = all_urls_file.read().splitlines()
    except FileNotFoundError:
        print(f"Could not find {all_urls_path}")
        return

    try:
        with open(latest_forum_posts_path, "r") as latest_forum_posts_file:
            latest_forum_posts = latest_forum_posts_file.read().splitlines()
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
        with open(all_urls_path, "w") as all_urls_file:
            all_urls_file.write("\n".join(updated_all_urls))
    except Exception as e:
        print(f"Could not write to {all_urls_path}: {e}")
        return


def run_it_up(urls_file_path=None, latest_forum_posts_path=None):
    all_urls_path = urls_file_path
    latest_forum_posts_path = latest_forum_posts_path
    confirmation_file_path = os.path.join(current_dir, ".confirmation")

    if os.path.exists(confirmation_file_path):
        update_urls_file(all_urls_path, latest_forum_posts_path)
    else:
        file_name = os.path.basename(all_urls_path)
        response = input(
            f"Are you sure you want to irreversibly alter the {file_name} file? This action cannot be undone. Type 'yes' to continue. You will not be asked again as long as .confirmation exists: "
        )
        if response.lower() == "yes":
            with open(confirmation_file_path, "w") as f:
                f.write("Confirmed")
            update_urls_file(all_urls_path, latest_forum_posts_path)
        else:
            print("Operation cancelled.")


def main():
    run_it_up(
        urls_file_path="urls.txt", latest_forum_posts_path="latest_forum_posts.txt"
    )


if __name__ == "__main__":
    main()
