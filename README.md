# Raspberry Pi Web Browser Auto-Launch

This Python script is designed to automatically open a web browser and display a specific webpage on a Raspberry Pi upon boot. It utilizes the `webbrowser` and `pyautogui` libraries to achieve this functionality.

## Prerequisites
no prerequisites

## Usage

1. Edit the `url` variable in the script to specify the webpage you want to open.
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

## Customization

You can customize the script further based on your requirements. For example, you may want to add error handling, set a different delay before maximizing the window, or modify the behavior based on different screen resolutions.

## Disclaimer

This script is provided as-is and may require adjustments to work in your specific environment. Use it at your own risk.

## Author

This script was originally designed for use on a Raspberry Pi.

If you have any questions or suggestions, feel free to reach out.
