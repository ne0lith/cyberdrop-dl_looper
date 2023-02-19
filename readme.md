## cyberdrop-dl_looper

This environment assumes a few things:
- Python can be run by entering "python" in your cmd/terminal.
- Pip can be run by entering "pip" in your cmd/terminal.
- Cyberdrop-dl can be run by entering "cyberdrop-dl" in your cmd/terminal.

If so, you can move on! If not, sorry!
- Update the config.yaml with your preferences. (we're using what I found most convenient.)
```
Don't edit the path of the input_file, or output_last_forum_post_file;
Unless you modify lines 73-74 of py/latest_thread_to_urls.py to accomodate.

Also, leave these paths alone if you're using archive_logs.py
errored_urls_file, unsupported_urls_file, log_file
```
- Add your urls to logs/urls.txt
- Run looper.bat

On my list of things to do

- [ ] Create a looper.py for that use case.
- [ ] Create a looper.ps1 for that use case.
