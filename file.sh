#!/bin/bash

webbrowser="https://vishnuxkrazy.netlify.app/display"

export DISPLAY=:0
sleep 30
chromium-browser --kiosk --full-screen "$webbrowser"

