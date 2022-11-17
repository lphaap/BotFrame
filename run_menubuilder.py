from pynput.mouse import Listener, Button;
from logger import log;
import json;
import time;

class MenuBuilder():

    def __init__(self):
        self.calibration_click = None;
        self.calibrated_menu = {};
        self.kill = False;

        log("Input first click on the corner of minimized the inventory.");

        def on_click(x, y, button, pressed):

            # Ignore mouse release events
            if(not pressed):
                return;

            # On first click set calibration_click
            if(not self.calibration_click):
                self.calibration_click = {
                    'x': x,
                    'y': y
                };
                log("Calibrated click to: " + str(self.calibration_click));
                return;

            # Print result and die on right click
            if(button == Button.right):
                log("PARSED MENU:\n\nmenu = " + json.dumps(self.calibrated_menu, indent=4));
                self.kill = True;
                return;

            log(
                "MouseHandler clicked at: "
                + str(x - self.calibration_click["x"])
                + ", "
                + str(y - self.calibration_click["y"])
            );

            self.calibrated_menu[((len(self.calibrated_menu) + 1))] = {
                'x': x - self.calibration_click["x"],
                'y': y - self.calibration_click["y"]
            };

        self.listener = Listener(on_click=on_click);

    def start(self):
        self.listener.start();

    def stop(self):
        self.listener.stop();


builder = MenuBuilder();

builder.start();
while(not builder.kill):
    time.sleep(1);

builder.stop();