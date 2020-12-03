import time
import threading
from pynput.mouse import Button
from pynput.keyboard import Listener, Key, Controller, KeyCode, HotKey, GlobalHotKeys

delay = 5

class HotkeyClick(threading.Thread):
    
    def __init__(self, delay):
        super(HotkeyClick, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True

    def start_pressing(self):
        print("start pressing")
        self.running = True

    def stop_pressing(self):
        print("stop pressing")
        self.running = False

    def exit(self):
        self.stop_pressing()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                time.sleep(self.delay)
                keyboard.press(Key.cmd)
                keyboard.press("\\")
                keyboard.release(Key.cmd)
                keyboard.release("\\")
            time.sleep(0.1)


keyboard = Controller()
press_thread = HotkeyClick(delay)
press_thread.start()

# start: option + shift + ]
# stop: option + shift + [
with GlobalHotKeys({
        '’': press_thread.start_pressing,
        '”': press_thread.stop_pressing}) as h:
    h.join()