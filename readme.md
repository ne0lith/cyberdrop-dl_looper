## cyberdrop-dl_looper

### This has only been developed to work if you use the V5 start file.

This environment assumes a few things:
- You are using the new v5 start file.
- You are using the Default profile. (if not, just rename all instances of "Default", in the looper_mods.bat)
- - You have set your profile as the default profile in cyberdrop's UI.
- Python can be run by entering "python" in your cmd/terminal.

### Updating and Installation Instructions

Follow these steps to update to the latest release:

* [Download the new release](https://github.com/n30liberal/cyberdrop-dl_looper/archive/refs/heads/main.zip) as a .zip file.
* Extract the contents of the .zip file and ensure that the files are placed in the same directory as your v5 start file.
* Place the 'mods' folder in the same directory as your start file.

Your final directory structure should resemble the following:

```
- /
  - AppData
  - Downloads
  - mods
    - file_management.py
  - Old Files
  - venv
  - looper.bat
  - looper_mods.bat
  - start.bat
  - Start Windows.bat

```

To run the program:

- Execute `looper.bat` for normal looping.
- Execute `looper_mods.bat` for looping with the option to backup your logs directory and urls file after each run.

Be sure to edit either .bat file for any user configurables. i.e. `looper_mods.bat` requires the name of the specific profile you need archived.

## To Do
Will be adding back discord webhook support asap.
