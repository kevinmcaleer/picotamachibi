import framebuf
from machine import Pin

class Icon():
    
    __image = None
    __x = 0
    __y = 0
    __invert = False
    __width = 16
    __height = 16
    __name = "Empty"

    def __init__(self, filename:None, width=None, height=None, x=None, y=None, name=None):
        if width:
            self.__width = width
        if height:
            self.__height = height
        if name:
            self.__name = name
        if x:
            self.__x = x
        if y:
            self.__y = y
        if filename is not None:
            self.__image = self.loadicons(filename)

    @property
    def image(self):
        """ gets the icon image """
        return self.__image

    @image.setter
    def image(self, buf):
        """ Sets the icon image """
        self.__image = buf
    
    @property
    def x(self)->int:
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def width(self)->int:
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the icon width """
        self.__width = value

    @property
    def height(self):
        """ Returns height """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        """ Sets the icon name """
        self.__name = value

    @property
    def y(self)->int:
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def invert(self)->bool:
        print("Invert is", self.__invert)
        return self.__invert

    @invert.setter
    def invert(self, value:bool):
        """ Inverts the icon colour """
        
        image = self.__image
        for x in range(0,self.width):
            for y in range(0, self.height):
                pxl = image.pixel(x,y)
                if pxl == 0:
                    image.pixel(x,y,1)
                else:
                    image.pixel(x,y,0)
                
        self.__image = image
        self.__invert = value
        # print("Invert is", self.__invert)

    def loadicons(self, file):
        with open(file, 'rb') as f:
            f.readline() # magic number
            f.readline() # creator comment
            f.readline() # dimensions
            data = bytearray(f.read())
        fbuf = framebuf.FrameBuffer(data, self.__width,self.__height, framebuf.MONO_HLSB)
        # print(self.__name, self.__width, self.__height)
        return fbuf

class Toolbar():
    __icon_array = []
    __framebuf = framebuf.FrameBuffer(bytearray(160*64*1), 160, 16, framebuf.MONO_HLSB)
    __spacer = 1
    __selected_item = None
    __selected_index = -1 # -1 means no item selected

    def __init__(self):
        # print("building toolbar")
        self.__framebuf = framebuf.FrameBuffer(bytearray(160*64*8), 160, 16, framebuf.MONO_HLSB)

    def additem(self, icon:Icon):
        self.__icon_array.append(icon)

    @property
    def data(self):
        """ Returns the toolbar array as a buffer"""
        x = 0
        count = 0
        for icon in self.__icon_array:
            # print("x:",x)
            count += 1
            self.__framebuf.blit(icon.image, x, 0) 
            fb = self.__framebuf
            x += icon.width + self.spacer
        return fb

    @property
    def spacer(self):
        """ returns the spacer value"""
        return self.__spacer

    @spacer.setter
    def spacer(self, value):
        """ Sets the spacer value"""
        self.__spacer = value

    def show(self, oled):
        oled.blit(self.data, 0,0)
        # oled.show()
    
    def select(self, index, oled):
        """ Set the item in the index to inverted """
        # for item in self.__icon_array:
        #     item.invert = False
        self.__icon_array[index].invert = True
        self.__selected_index = index
        self.show(oled)

    def unselect(self, index, oled):
        self.__icon_array[index].invert = False
        self.__selected_index = -1
        self.show(oled)

    @property
    def selected_item(self):
        """ Returns the name of the currently selected icon """
        self.__selected_item = self.__icon_array[self.__selected_index].name
        return self.__selected_item

class Animate():
    __frames = []
    __current_frame = 0
    # __speed = 0.1
    __done = False # Has the animation completed

    def __init__(self, frames):
       """ setup the animation""" 
       self.__current_frame = 0
       self.__frames = frames
       self.__done = False

    def animate(self, oled):
        cf = self.__current_frame # Current Frame number - used to index the frames array
        frame = self.__frames[cf]

        oled.blit(frame.image, frame.x, frame.y)
        self.__current_frame +=1
        if self.__current_frame > len(self.__frames)-1:
            self.__current_frame = 0
            self.__done = True
        # print("frame", self.__current_frame)
    
    @property
    def done(self):
        """ Has the animation completed """
        print("Done?",self.__done)
        if self.__done:
            self.__done = False
            return True
        else:
            return False

class Button():
    __pressed = False
    __pin = 0
    __button_down = False

    def __init__(self, pin:int):
        self.__pin = Pin(pin, Pin.IN, Pin.PULL_DOWN)
        self.__pressed = False

    @property
    def is_pressed(self)->bool:
        """ Returns the current state of the button """
        if self.__pin.value() == 0:
            self.__button_down = False
            return False
        if self.__pin.value() == 1:
            if not self.__button_down:
                # print("button pressed")
                self.__button_down = True
                return True
            else:
                return False