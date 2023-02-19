## cyberdrop-dl_looper

This environment assumes a few things:
- Python can be run by entering "python" in your cmd/terminal.
- Pip can be run by entering "pip" in your cmd/terminal.
- Cyberdrop-dl can be run by entering "cyberdrop-dl" in your cmd/terminal.

If so, you can move on! If not, sorry!
- Update the config.yaml with your preferences. (we're using what I found most convenient.)
```
Do not edit these lines unless you modify lines 76, and, 77 of latest_thread_to_urls.py to accomodate.

input_file: logs/urls.txt
output_last_forum_post_file: logs/latest_forum_post.txt
```
- Add your urls to logs/urls.txt
- Run looper.bat

On my list of things to do

- [ ] Create a looper.py for that use case.
- [ ] Create a looper.ps1 for that use case.
