# Raspberry Pi Web Browser Auto-Launch

This basg script is designed to automatically open a web browser and display a specific webpage on a Raspberry Pi upon boot.
# Background
- I tried this in python
- It will generate a lot of errors and take lot of time
- It will also give you lot of library errors
- So, avoid in python
- So, use .bash shell it is neater
## Prerequisites
- chromium-browser has to be installed 
    + which is on default on most of default builds
## Usage

1. Edit the `website_url` variable in the script to specify the webpage you want to open.
2. Save your changes.
3. Ensure the script is set to run upon boot.

### Setting up Auto-Execution on Boot

To automatically execute the script upon boot, you can add it to the crontab:

1. Open the crontab file for editing:

```bash
crontab -e
```

2. Add the following line to the crontab file to run the script on boot:

```bash
@reboot bash -m -l /home/<user-name>/announcements-rpi-automation/file.sh
```

Replace `/path/to/file.sh` with the actual path to your script.

3. Save and exit the crontab file.

## Script Explanation

The script `file.sh` consists of the following functions:

- `open_browser(url)`: This function takes a URL as input and opens it in a web browser. It then waits for the browser to open, gets the screen dimensions, and maximizes the browser window to full screen using keyboard shortcuts.

## Fastest way
``` bash
  git clone https://github.com/krazykarthik2/announcements-rpi-automation
  crontab -e
```
First time,
- it will ask 1.sudo nano-->easiest
              2.sudo n...
  + click 1
- then write this
```
@reboot bash -l -m /path/to/script.sh
```
which is generally speaking...
```
@reboot bash -l -m /home/<user-name>/announcements-rpi-automation/file.sh
```
Sucessfully finished
### Check
reboot your system by
```
sudo reboot
```
and then after 30seconds 
browser will open

check background tasks by using 
```
ps aux | grep website_url
```

## Customization

You can customize the script further based on your requirements. For example, you may want to add error handling, set a different delay before maximizing the window, or modify the behavior based on different screen resolutions.

## Disclaimer

This script is provided as-is and may require adjustments to work in your specific environment. Use it at your own risk.

## Author

This script was originally designed for use on a Raspberry Pi.

If you have any questions or suggestions, feel free to reach out.
