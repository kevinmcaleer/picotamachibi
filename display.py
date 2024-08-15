from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
import framebuf
from time import sleep

sda = Pin(0)
scl = Pin(1)
id = 0

i2c = I2C(id=id, sda=sda, scl=scl)
print(f"i2c scan: {i2c.scan()}")
oled = SSD1306_I2C(width=128, height=64, i2c=i2c)
oled.init_display()


oled.text("test", 1, 1)
oled.show()
sleep(1)

images = []
for n in range (1,5):
    with open('poop0%s.pbm' % n, 'rb') as f:
        f.readline() # magic number
        f.readline() # creator comment
        f.readline() # dimensions
        data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, 128,64, framebuf.MONO_HLSB)
    images.append(fbuf)

while True:
    for i in images:
        oled.invert(1)
        oled.blit(i,0,0)
        oled.show()
        sleep(0.1)
    sleep(0.4)
    for i in reversed(images):
        oled.invert(1)
        oled.blit(i,0,0)
        oled.show()
        sleep(0.1)
