import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.macros import Macros, Press, Release, Tap, Delay

print('Starting')

keyboard = KMKKeyboard()

layers = Layers()
macros = Macros()
encoder = EncoderHandler()

keyboard.modules.append(layers)
keyboard.modules.append(macros)
keyboard.modules.append(encoder)
keyboard.modules.append(MediaKeys())
keyboard.modules.append(MouseKeys())

# DISPLAY
i2c_bus = busio.I2C(board.D5, board.D4)

display_driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    display=display_driver,
    width=128,
    height=32,
    flip=False,
    flip_left=False,
    flip_right=False,
    powersave_off_time=-1,
    entries=[
        TextEntry(text='Number Pad', x=64, y=16, x_anchor="M", y_anchor="M",layer=0),
        TextEntry(text='Shortcut Keys', x=64, y=16, x_anchor="M", y_anchor="M",layer=1),
    ],
)

keyboard.extensions.append(display)

keyboard.col_pins = (board.D2, board.D6, board.D7, board.D8)
keyboard.row_pins = (board.D3, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder.pins = ((board.D0, board.D1, None),)
encoder.map = [
    ((KC.VOLD, KC.VOLU),),
    ((KC.VOLD, KC.VOLU),),
]

# MACROS
def make_url_macro(url):
    return KC.MACRO(
        # Open Spotlight
        Press(KC.LGUI), Tap(KC.SPACE), Release(KC.LGUI),
        Delay(300),
        # Launch / focus Safari
        "Safari",
        Tap(KC.ENTER),
        Delay(1000),  # wait for Safari to open/focus
        # New tab -> focuses address bar
        Press(KC.LGUI), Tap(KC.T), Release(KC.LGUI),
        Delay(300),
        # Type URL and go
        url,
        Tap(KC.ENTER),
    )


KC_GITHUB = make_url_macro("https://github.com")
KC_SLACK = make_url_macro("https://slack.com")
KC_YOUTUBE = make_url_macro("https://www.youtube.com")

# KEYMAP
RAISE = KC.TG(1)

keyboard.keymap = [
    [  # layer 0
        KC.N1, KC.N2, KC.N3, RAISE,
        KC.N4, KC.N5, KC.N6, KC.KP_ENTER,
        KC.N7, KC.N8, KC.N9, KC.N0,
    ],
    [  # layer 1
        KC_GITHUB, KC_SLACK, KC_YOUTUBE, RAISE,
        KC.TAB, KC.UP, KC.E, KC.R,
        KC.LEFT, KC.DOWN, KC.RIGHT, KC.KP_ENTER,
    ],
]

if __name__ == '__main__':
    keyboard.go()# Write your code here :-)
