from pynput.mouse import Listener, Button, Controller as MouseController;
from pynput.keyboard import Key, Controller as KeyboardController;
from logger import log;
from menu_dict import inventory, prayer;
from menu_enum import MenuEnum;
import json;
import time;

class MenuHandler():

    def __init__(self):
        self.calibration_click = None;

        # Add menu maps here
        self.menu_to_cords = {};
        self.menu_to_cords[MenuEnum.INVENTORY] = inventory;
        self.menu_to_cords[MenuEnum.PRAYER] = prayer;

        # Add menu key maps here
        self.menu_to_keys = {};
        self.menu_to_keys[MenuEnum.INVENTORY] = Key.esc;
        self.menu_to_keys[MenuEnum.PRAYER] = Key.f5;

        # Init controllers
        self.mouse_controller = MouseController();
        self.keyboard_controller = KeyboardController();

        log("Input first click on the corner of minimized the inventory.");

        # A bit silly, but only listen for one click and die, for calibration
        def on_click(x, y, button, pressed):
            # Ignore mouse release events
            if(not pressed):
                return;

            self.calibration_click = {
                'x': x,
                'y': y
            };

            log("Calibrated click to: " + str(self.calibration_click));

            self.mouse_listener.stop();
            return;

        self.mouse_listener = Listener(on_click=on_click);
        self.mouse_listener.start();

    def move_to_menu_item(self, menu_enum, menu_index):
        index_cords = self.get_menu(menu_enum)[menu_index];

        move_to_x = self.calibration_click['x'] + index_cords['x'];
        move_to_y = self.calibration_click['y'] + index_cords['y'];

        self.mouse_controller.position = (move_to_x, move_to_y);

        log(
            "Moving mouse to "
            + str(menu_enum)
            + "-"
            + str(menu_index)
            + " -> ("
            + str(move_to_x)
            + ","
            + str(move_to_y)
            + ")"
        );

    def click_menu_item(self, menu_enum, menu_index, mouse_button):
        self.move_to_menu_item(menu_enum, menu_index);
        time.sleep(0.05);
        self.click(mouse_button);
        log(
            "Clicking mouse at "
            + str(menu_enum)
            + "-"
            + str(menu_index)
            + " -> "
            + str(mouse_button)
        );

    def open_menu(self, menu_enum):
        self.press_key(
            self.get_menu_key(menu_enum)
        );
        time.sleep(0.05);

    def press_key(self, key):
        self.keyboard_controller.press(key);
        self.keyboard_controller.release(key);

    def get_menu_key(self, menu_enum):
        return self.menu_to_keys[menu_enum];

    def menu_indexes(self, menu_enum):
        return dict.keys(
            self.get_menu(menu_enum)
        );

    def click(self, mouse_button):
        self.mouse_controller.click(mouse_button);

    def get_menu(self, menu_enum):
        return self.menu_to_cords[menu_enum];

    def is_calibrated(self):
        if(self.calibration_click):
            return True;

        return False;

