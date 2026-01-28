print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GPIO2, board.GPIO1, board.GPIO0, board.GPIO28)
keyboard.row_pins = (board.GPIO0, board.GPIO4, board.GPIO3,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder = EncoderHandler()
keyboard.modules.append(encoder)
keyboard.modules.append(MediaKeys)
keyboard.modules.append(MouseKeys)

encoder.pins = ((board.GPIO26, board.GPIO27, None),)
RAISE = KC.LT(1,KC.ESC)
TRANS = KC.TRANS

keyboard.keymap = [
                    [RAISE,
                    KC.LSHIFT,  KC.N1, KC.N2, KC.N3,
                    KC.KP_ENTER, KC.N4,  KC.N5,  KC.N6,
                    KC.TAB,  KC.N7,  KC.N8,  KC.N9
                  ],
                [
                    [TRANS,
                    KC.MUTE,  KC.MRWD, KC.MPLY, KC.MFFD,
                    KC.KP_ENTER, KC.N4,  KC.N5,  KC.N6,
                    KC.TAB,  KC.N7,  KC.N8,  KC.N9
                  ],
]
encoder.keymap = [
                    ((KC.VOLD, KC.VOLU),),
                    ((KC.MW_DN,KC.MW_UP),),

]

if __name__ == '__main__':
    keyboard.go()
