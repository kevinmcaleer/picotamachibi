# Picotamachibi
## A Raspberry Pi Pico Powered Virtual Pet

By Kevin McAleer, September 2021

---

This is the code repository that accompanies this video:

[![PicoTamachibi](https://img.youtube.com/vi/c6D1JRDddkE/0.jpg)](https://youtu.be/c6D1JRDddkE)

---

## About this code
To use the code, upload all the `.pbm` files to the pico, along with the ssd1306 driver (`ssd1306.py`), `icon.py` library and the main program `picotamachibi.py`.

## Wiring
1. Pin 0 is connected to the screen SDA
2. Pin 1 is connected to the screen SCL
3. Pin 2 is connected to the cancel button (button X)
4. Pin 3 is connected to the B button
5. Pin 4 is connected to the A button

Press the A button to move the toolbar selector across the different options, Press button X to cancel the selection or Button B to select the menu option.

