print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GPIO2, board.GPIO1, board.GPIO0, board.GPIO28)
keyboard.row_pins = (board.GPIO0, board.GPIO4, board.GPIO3,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.LSHIFT,  KC.N1, KC.N2, KC.N3,
    KC.KP_ENTER, KC.N4,  KC.N5,  KC.N6,
    KC.TAB,  KC.N7,  KC.N8,  KC.N9
  ]
]

if __name__ == '__main__':
    keyboard.go()
