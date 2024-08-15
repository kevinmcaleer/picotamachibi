from gfx_pack import GfxPack
from picographics import PicoGraphics

gp = GfxPack()
display = gp.display
sprite = [ 0x81, 0x42, 0x24, 0x18, 0x81, 0x42, 0x24, 0x18]

def add_sprite(framebuf, sprite, locationx , locationy):
    for index in range(len(sprite)):
        framebuf[locationx + ((index + locationy) *16)] = sprite[index]
    
    
frame = bytearray(int((128*64)/8))

add_sprite(frame, sprite, 0, 0)


display.set_framebuffer(frame)
display.update()