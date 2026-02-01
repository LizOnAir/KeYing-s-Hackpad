# Hackpad

This hackpad is a 12 key macropad with a rotary encoder, an OLED Display. It also has 12 SK6812 MINI-E LEDs, and uses KMK firmware.

## Features:
- Upper black layer with transparent bottom acrylic case
- 128x32 OLED Display
- EC11 Rotary encoder
- 12 SK6812 MINI-E LEDs (to produce underglow effect)
- 12 Keys

## CAD Model:
The black upper case and transparent bottom case fits together with 4 M3x5mx4mm heatset inserts and 4 M3x16mm screws.
It has 3 separate printed pieces. The base where the PCB sits, the top cover and also a case for the rotary encoder.

<img width="622" height="565" alt="Screenshot 2026-02-01 at 9 26 06 PM" src="https://github.com/user-attachments/assets/9757e1ce-e716-4e35-8774-657c70df9173" />
<img width="622" height="565" alt="Screenshot 2026-02-01 at 9 26 20 PM" src="https://github.com/user-attachments/assets/568280d8-5abb-44a0-bd28-1804169289b5" />


Made in Fusion360.Liz

## PCB
Here's my PCB! It was made in KiCad. 
Schematic
<img width="415" height="203" alt="Screenshot 2026-01-26 at 8 29 48 AM" src="https://github.com/user-attachments/assets/00ce3c77-728b-42fe-b1c0-dff4e132f134" />

PCB
<img width="514" height="500" alt="Screenshot 2026-01-26 at 12 03 23 PM" src="https://github.com/user-attachments/assets/cbb5fe79-8735-4911-9c38-9d7e036f8e40" />
I used MX_V2 for the keyswitch footprints.
The unicorn silkscreen image was imported from [FLATICON](https://www.flaticon.com/).

## Firmware Overview
This hackpad uses KMK firmware.

- the rotary encoder changes volume and able to act as mousewheel to scroll
- The 12 keys currently act as number pad and arrows key (I'm gonna modify the macros soon to suit my needs)
- The OLED display layers (maybe some cute gif in the future?)

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
