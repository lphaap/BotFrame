from menu_handler import MenuHandler;
from state_handler import StateHandler;
from menu_enum import MenuEnum;
from pynput.mouse import Button;
from logger import log;
import time;

log("-- Init --");
log("Press alt + q to start");
log("Press alt + w to pause");
log("Press alt + e to stop");

state_handler = StateHandler();

# Wait for start
while(not state_handler.is_running()):
    time.sleep(1);

# Wait for calibration click
log("-- Start --");

menu_handler = MenuHandler();
while(not menu_handler.is_calibrated()):
    time.sleep(1);

# Main script loop
while(state_handler.is_running()):

    # Only sleep when paused
    if state_handler.is_paused():
        time.sleep(1);
        continue;

    # Sleep one game tick
    time.sleep(0.6);

    # -- Script here --

    # Shouldnt use loops in scripts but this is a demo
    indexes = menu_handler.menu_indexes(MenuEnum.INVENTORY);
    menu_handler.open_menu(MenuEnum.INVENTORY);
    for index in indexes:
        menu_handler.click_menu_item(
            MenuEnum.INVENTORY,
            index,
            Button.right
        );
        time.sleep(0.5);
        menu_handler.click(Button.left);

    indexes = menu_handler.menu_indexes(MenuEnum.PRAYER);
    menu_handler.open_menu(MenuEnum.PRAYER);
    for index in indexes:
        menu_handler.click_menu_item(
            MenuEnum.PRAYER,
            index,
            Button.right
        );
        time.sleep(0.5);
        menu_handler.click(Button.left);
