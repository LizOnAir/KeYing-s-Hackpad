print("Starting")

import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.display import Display, DisplayText
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP2, board.GP1, board.GP0, board.GP28)
keyboard.row_pins = (board.GP0, board.GP4, board.GP3,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
i2c = busio.I2C(scl=board.GP6, sda=board.GP5)
rgb = RGB(pixel_pin=board.GP6, num_pixels=12)

oled_text = DisplayText()
oled = Display(
    display=SSD1306(
        i2c=i2c,
        device_address=0x3C,
        width=128,
        height=32,

encoder = EncoderHandler()
holdtap = HoldTap()
keyboard.modules.append(holdtap)
keyboard.modules.append(Layers())
keyboard.modules.append(encoder)
keyboard.modules.append(MediaKeys())
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(rgb)

encoder.pins = ((board.GPIO26, board.GPIO27, None),)
RAISE = KC.HT(KC.TAP, KC.HOLD, prefer_hold=True, tap_interrupted=False, tap_time=2000, repeat=HoldTapRepeat.NONE)
TRANS = KC.TRANS
BASE = KC.DF(0)

keyboard.keymap = [#layer 0
                    [RAISE,
                    KC.LSHIFT,  KC.N1, KC.N2, KC.N3,
                    KC.KP_ENTER, KC.N4,  KC.N5,  KC.N6,
                    KC.TAB,  KC.N7,  KC.N8,  KC.N9
                  ],
                  [#layer 1
                    [TRANS,
                    KC.MUTE,  KC.MRWD, KC.MPLY, KC.MFFD,
                    KC.KP_ENTER, KC.UP,  TRANS,  TRANS,
                    KC.LEFT,  KC.DOWN,  KC.RIGHT,  TRANS
                  ],
]
encoder.map = [
                ((KC.VOLD, KC.VOLU),),
                ((KC.MW_DN,KC.MW_UP),),

]

def before_matrix_scan():
    if keyboard.active_layers[0] == 0:
        oled_text.text = "Mode:\nNumber Pad"
    else:
        oled_text.text = "Mode:\nNavigate"

keyboard.before_matrix_scan.append(before_matrix_scan)
KC.RGB_MODE_BREATHE()
    
if __name__ == '__main__':
    keyboard.go()
