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
1. GPIO 0 is connected to the screen SDA
2. GPIO 1 is connected to the screen SCL
3. GPIO 2 is connected to the cancel button (button X)
4. GPIO 3 is connected to the B button
5. GPIO 4 is connected to the A button

Press the A button to move the toolbar selector across the different options, Press button X to cancel the selection or Button B to select the menu option.

## Getting help
If you have any questions about this, [join our discord](https://action.smarsfan.com/join-discord) server and ask away : )
