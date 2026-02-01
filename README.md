# Hackpad

This hackpad is a 12 key macropad with a rotary encoder, an OLED Display. It also has 12 SK6812 MINI-E LEDs, and uses KMK firmware.

## Features:
- Upper black layer with transparent bottom acrylic case
- 128x32 OLED Display
- EC11 Rotary encoder
- 12 SK6812 MINI-E LEDs (to produce underglow effect)
- 12 Keys

## CAD Model:
The upper case and bottom case fits together with snap fit design.

It has 3 separate printed pieces. The base where the PCB sits, the top cover and also a case for the rotary encoder.
<img src=assets/cad.png alt="Schematic" width="500"/>

Made in Fusion360. Liz

## PCB
Here's my PCB! It was made in KiCad. The silkscreen was imported from [FLATICON](https://www.flaticon.com/)
Schematic
<img src=assets/schematic.png alt="Schematic" width="300"/>

PCB
<img src=assets/pcb.png alt="Schematic" width="300"/>

I used MX_V2 for the keyswitch footprints.

## Firmware Overview
This hackpad uses KMK firmware.

- the rotary encoder changes volume and able to act as mousewheel to scroll
- The 12 keys currently act as number pad and arrows key (I'm gonna modify the macros soon to suit my needs)
- The OLED display layers (maybe some cute gif in the future?)

<img src=assets/bongocat.png alt="Bongo Cat" width="300"/>

I'm definitely gonna edit the features soon ahhaha

## BOM:
Here should be everything you need to make this hackpad

- 12x Cherry MX Switches
- 12x DSA Keycaps
- 13x 1N4148 DO-35 Diodes.
- 12x SK6812 MINI-E LEDs
- 1x 0.91" 128x32 OLED Display
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
- 1x Case (3 printed parts）

## PS
It was my very first time from designing PCB in kicad to modelling in Fusion 360 and also doing firmware stuff.
Although it took longer time than I expected but I still have enthusiasm and hope to be doing more in the future!
