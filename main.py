import webbrowser
import pyautogui

def open_browser(url):
    # Open the web browser
    webbrowser.open(url)

    # Wait for the browser to open
    pyautogui.sleep(2)

    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Maximize the browser window
    pyautogui.keyDown('win')
    pyautogui.press('up')
    pyautogui.keyUp('win')
    pyautogui.press('F11')


# Specify the web address you want to open
url = "https://www.vishnuxkrazy.netlify.app/display"

# Call the function to open the browser and make it full screen
open_browser(url)
