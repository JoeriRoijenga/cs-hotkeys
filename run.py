import time
import threading
from pynput.mouse import Button
from pynput.keyboard import Listener, Key, Controller, KeyCode

delay = 10
button = Button.left
start_key = Key.f1
stop_key = Key.f2
exit_key = Key.f3

class HotkeyClick(threading.Thread):
    
    def __init__(self, delay):
        super(HotkeyClick, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True

    def start_pressing(self):
        self.running = True

    def stop_pressing(self):
        self.running = False

    def exit(self):
        self.stop_pressing()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                keyboard.press(Key.cmd)
                keyboard.press("\\")
                time.sleep(self.delay)
            time.sleep(0.1)


keyboard = Controller()
press_thread = HotkeyClick(delay)
press_thread.start()


def on_press(key):
    if key == start_key:
        print("pressed")
        if not press_thread.running:
            print("start")
            press_thread.start_pressing()
    elif key == stop_key:
        print("stop")
        press_thread.stop_pressing()
    elif key == exit_key:
        print("exit")
        press_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()