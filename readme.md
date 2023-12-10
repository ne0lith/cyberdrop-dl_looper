## cyberdrop-dl_looper

### This has only been developed to work if you use the V5 start file(s).

This environment assumes a few things:
- You are **not** using macOS.
- You are using the new v5 start file.
- You are using the Default profile.
  - If not the Default profile:
    - You have set your profile as the default profile in cyberdrop's UI.
    - You replace "Default" with your profile name in `looper_mods.bat`.
- Python can be run by entering "python" in your cmd/terminal.
  - "python3" if on linux.

### Updating and Installation Instructions

Follow these steps to update to the latest release:

* [Download the repo](https://github.com/n30liberal/cyberdrop-dl_looper/archive/refs/heads/main.zip) as a .zip file.
* Extract the contents of the .zip file and ensure that the files are placed in the same directory as your v5 start file.
* Place the 'mods' folder in the same directory as your start file.

Your final directory structure should look similar to the following:

```
├─ AppData/
├─ Downloads/
├─ mods/
│  ├─ file_management.py
│  └─ send_webhook_results.py
├─ Old Files/
├─ venv/
├─ looper.bat
├─ looper_mods.bat
├─ readme.md (can delete)
├─ start.bat
└─ Start Windows.bat
```

## To run the program

- Execute `looper.bat|sh` for normal looping. The default loop count is 20. `set "loop_count=20"`
- Execute `looper_mods.bat|sh` for looping with the option to backup your logs directory and urls file after each run, and send run results via discord webhook. The default loop count is 20. `set "loop_count=20"`

Be sure to edit `looper_mods.bat|sh`, as it requires the name of the specific profile you are looping with.

## To Archive Logs each run
- Within `looper_mods.bat|sh` ensure `set "backup_logs=true"` is indeed true.
- Be careful with this, as depending on your log size, this can quickly eat up storage space. I recommend regularly cleaning some out.

## To send run results via Discord Webhook
- Within `looper_mods.bat|sh` ensure `set "send_webhook=true"` is indeed true
- Within `mods\send_webhook_results.py` find line 8 and replace `YOUR_WEBHOOK_URL_HERE` with your unique webhook_url.
