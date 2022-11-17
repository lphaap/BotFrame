from pynput import keyboard;
from logger import log;

class StateHandler():

    def __init__(self):
        self.paused = False;
        self.running = False;

        self.keyboard_handler = keyboard.GlobalHotKeys({
            '<alt>+q': self.start,
            '<alt>+w': self.toggle_pause,
            '<alt>+e': self.stop,
        });

        self.keyboard_handler.start();


    def pause(self):
        log("-- Paused --");
        self.paused = True;

    def unpause(self):
        log("-- Unpaused --");
        self.paused = False;

    def toggle_pause(self):
        log("-- Toggled Pause --");
        self.paused = not self.paused;

    def start(self):
        log("-- Started --");
        self.running = True;

    def stop(self):
        log("-- Stoped --");
        self.running = False;
        self.stop_listener(); # This can be moved elsewhere

    def is_running(self):
        return self.running;

    def is_paused(self):
        return self.paused;

    def stop_listener(self):
        self.keyboard_handler.stop();
