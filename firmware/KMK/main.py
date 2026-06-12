import board
import busio
import displayio
import adafruit_ssd1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import Pins
from kmk.modules.layers import LayersModule
import time

keyboard = KMKKeyboard()


keyboard.matrix = Pins([board.D8, board.D9, board.D10], value_when_pressed=False)

layers = LayersModule()
keyboard.modules.append(layers)


displayio.release_displays()
i2c = busio.I2C(board.D5, board.D4)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

def update_display(line1, line2="READY"):
    display.fill(0)
    display.text(line1, 0, 4, 1)
    display.text(line2, 0, 20, 1)
    display.show()


keyboard.keymap = [
    [KC.MUTE, KC.MPRV, KC.MNXT], 
    [KC.LSHIFT(KC.F), KC.S, KC.E],
    [KC.LCTRL(KC.Z), KC.LCTRL(KC.X), KC.LCTRL(KC.V)],
]


menu_mode = False
current_idx = 0
layer_names = ["1. MEDIA", "2. FUSION", "3. PROD"]
press_start_time = 0
is_holding = False

def menu_logic():
    global menu_mode, current_idx, press_start_time, is_holding
    
   
    btn1 = keyboard.matrix.scanners[0].get_key_state(0) 
    btn2 = keyboard.matrix.scanners[0].get_key_state(1)
    btn3 = keyboard.matrix.scanners[0].get_key_state(2)

    
    if btn1:
        if not is_holding:
            press_start_time = time.monotonic()
            is_holding = True
        elif time.monotonic() - press_start_time >= 3.0:
            menu_mode = not menu_mode
            update_display("[MENU]" if menu_mode else layer_names[current_idx])
            is_holding = False
            time.sleep(0.5) 
    else:
        is_holding = False

    if menu_mode:
        if btn2: 
            current_idx = (current_idx - 1) % 3
            update_display("SELECT LAYER:", layer_names[current_idx])
            time.sleep(0.2)
        if btn3: 
            current_idx = (current_idx + 1) % 3
            update_display("SELECT LAYER:", layer_names[current_idx])
            time.sleep(0.2)
        if btn1 and not is_holding: 
            layers.activate_layer(current_idx)
            menu_mode = False
            update_display("ACTIVE:", layer_names[current_idx])
            time.sleep(0.5)

keyboard.before_matrix_scan = menu_logic

if __name__ == '__main__':
    keyboard.go()
