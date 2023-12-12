## cyberdrop-dl_looper

### This has only been developed to work if you use the V5 start file(s).

This environment assumes a few things:
- You are **not** using macOS.
  - Currently only supports windows + linux.
- You are using the new v5 start file.
- You are using the Default profile.
  - If not the Default profile:
    - You have set your profile as the default profile in cyberdrop's UI.
    - You replace "Default" with your profile name in `looper_mods`.
- Python can be run by entering "python" in your cmd/terminal.
  - "python3" if on linux.

### Updating and Installation Instructions

Follow these steps to update to the latest release:

* [Download the repo](https://github.com/n30liberal/cyberdrop-dl_looper/archive/refs/heads/main.zip) as a .zip file.
* Extract the contents of the .zip file and ensure that the files are placed in the same directory as your v5 start file.
* Place the 'mods' folder in the same directory as your start file.

---

Although you don't need everything from this repo. Only the `mods/` directory, along with the `.py` scripts, and your preferred looper script.
Your final directory structure should look similar to the following:

## Windows
```
├─ AppData/
├─ Downloads/
├─ mods/
│  ├─ file_management.py
│  └─ send_webhook_results.py
├─ Old Files/
├─ venv/
├─ config.txt
├─ looper.bat
├─ looper_mods.bat
└─ start.bat
```

## Linux
```
├─ AppData/
├─ Downloads/
├─ mods/
│  ├─ file_management.py
│  └─ send_webhook_results.py
├─ Old Files/
├─ venv/
├─ config.txt
├─ looper.sh
├─ looper_mods.sh
└─ start.sh
```

---

## To run the program

- Within `config.txt` ensure `loop_count=20` is set to an amount you are happy with.
- Execute `looper` for normal looping.
- Execute `looper_mods` for looping with the option to backup your logs directory and urls file after each run, and send run results via discord webhook.

## To Archive Logs each run
- Within `config.txt` ensure `backup_logs=true` is indeed true.
- Be careful with this, as depending on your log size, this can quickly eat up storage space. I recommend regularly cleaning some out.

## To send run results via Discord Webhook
- Within `config.txt` ensure `send_webhook=true` is indeed true
- Within `mods\send_webhook_results.py` find line 8 and replace `YOUR_WEBHOOK_URL` with your unique webhook_url.
- If you are running multiple instances of this project, and would like to differentiate your webhooks
  - Within `config.txt` ensure `machine_name=Default` is changed for each machine.
