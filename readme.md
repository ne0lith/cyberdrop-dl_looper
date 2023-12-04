## cyberdrop-dl_looper

### This has only been developed to work if you use the V5 start file.

This environment assumes a few things:
- You are using the new v5 start file.
- You are using the Default profile.
- Python can be run by entering "python" in your cmd/terminal.

### Updating and Installation Instructions

Follow these steps to update to the latest release:

* Download the new release as a .zip file.
* Extract the contents of the .zip file and ensure that the files are placed in the same directory as your v5 start file.
* Place the 'mods' folder in the same directory as your start file.

Your directory structure should resemble the following:

```
/AppData
/Downloads
/mods
/venv (will only be there if you have ran v5 from the start file at least once)
looper.bat
looper_mods.bat
Start.bat
```

To run the program:

- Execute `looper.bat` for normal looping.
- Execute `looper_mods.bat` for looping with the option to backup your logs directory and urls file after each run.

Be sure to edit either .bat file for any user configurables. i.e. `looper_mods.bat` requires the name of the specific profile you need archived.

## To Do
Will be adding back discord webhook support asap.
