# Convert PBM to Text
# Converts gimp pbm files into python byte array
# import framebuf
import yaml

sprite_name = ""

def loadicons(file:str, variable_name:str):
    # print(file)
    variable_filename = variable_name + '.py'
    print(f'writing file "{variable_filename}"')
    with open(variable_filename, 'a') as output:
    
        with open(file, 'rb') as f:
            f.readline() # magic number
            f.readline() # creator comment
            dimensions = f.readline() # dimensions
            d = dimensions.decode('utf-8').split()
    #         print(f'd:{d}')
            width = int(d[0])
            height = int(d[1])
            
    #         print(f'dimensions: {d}, width: {width}, height: {height}')
           
            data = bytearray(f.read())
            
        
            print(f'data: {data}')
        # frame_buffer = framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)
        # print(self.__name, self.__width, self.__height)
        fn = file.split('.pbm')[0]
        line = f"{fn} = {{ \n"
        print(f'line: "{line}"')
        output.write(line)
        for col in range(width):
            line = "    b'"
            print(line, end='')
            output.write(line)
            for row in range(height):
                # pixel = frame_buffer.pixel(row,col)
                pixel_index = row + (col * width)
                print(f'pixel_index: {pixel_index}, size: {len(data)}, row: {row}, col: {col}')
                print(data[row], end='')
                pixel = data[(row + col) // width]
                print(f'pixel: {pixel}')
                if pixel == 1:
                    line = '1'
                    print(line, end='')
                    output.write(line)
                else:
                    line = '0'
                    print(line, end='')
                    output.write(line)
            line = f"', \\" + '\n'
            print(f'{line}', end="")
            output.write(line)
        line = "}\n"
        print(line)
        output.write(line)
 
def convert_files(data):
    for item in data:
        print(item)
        sprite_name = item['name']
        print(f'Sprite name is: {sprite_name}')
        for file in item['files']:
            print(f'filename is {file}')
            loadicons(file, sprite_name)
        # file = item
        # variable_name = item.split('.pbm')[0]
        # loadicons(None, file, variable_name)

sprites = 'sprites.yml'
with open(sprites, 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

    import os
    for file in data:
        print(file)
        f = file['name'] + '.py'
        if os.path.exists(f):
            print('file found')
            os.remove(f)
        else:
            print('file not found')
            
    convert_files(data)