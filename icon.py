import framebuf

class Icon():
    
    __image = None
    __x = 0
    __y = 0
    __invert = False
    __width = 16
    __height = 16
    __name = "Empty"

    def __init__(self, filename:None, width=None, height=None, name=None):
        if filename is not None:
            self.__image = self.loadicons(filename)
        if width:
            self.__width = width
        if height:
            self.__height = height
        if name:
            self.__name = name

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
        image = self.__image
        for item in image:
            item = item & 'x\FF'
        self.__image = image
        return self.__invert

    @invert.setter
    def invert(self, value):
        self.__invert - value

    @staticmethod
    def loadicons(file):
        with open(file, 'rb') as f:
            f.readline() # magic number
            f.readline() # creator comment
            f.readline() # dimensions
            data = bytearray(f.read())
        fbuf = framebuf.FrameBuffer(data, 16,16, framebuf.MONO_HLSB)
        return fbuf

class Toolbar():
    __icon_array = []
    __framebuf = framebuf.FrameBuffer(bytearray(20*64), 16, 16, framebuf.MONO_HLSB)
    __spacer = 1

    def __init__(self):
        print("building toolbar")
        self.__framebuf = framebuf.FrameBuffer(bytearray(20*64), 16, 16, framebuf.MONO_HLSB)

    def additem(self, icon:Icon):
        self.__icon_array.append(icon)

    @property
    def data(self):
        """ Returns the toolbar array as a buffer"""
        x = 0
        count = 1
        for icon in self.__icon_array:
            self.__framebuf.blit(icon.image, x, 0, framebuf.MONO_HLSB) 
            # x += self.__spacer + (icon.width * count) + self.__spacer
            x = icon.width * count
            print("x:",x)
            count += 1
            print("icon", icon.name)
        return self.__framebuf 

    @property
    def spacer(self):
        """ returns the spacer value"""
        return self.__spacer

    @spacer.setter
    def spacer(self, value):
        """ Sets the spacer value"""
        self.__spacer = value