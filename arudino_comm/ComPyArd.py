import serial
import time
from mosaic.quantization.return_name import color_nr

def Arduino_read(arduino_port):
    arduino_bytes= arduino_port.readline()
    arduino_string= arduino_bytes.decode()
    arduino_string= arduino_string.rstrip()
    return arduino_string


#read from Arduino

def Arduino_write_pos(arduino_port, arduino_offset, color_used, COLORTABLE):
    if arduino_offset<len(color_used):
        next_move = color_nr(color_used[arduino_offset], COLORTABLE)
        arduino_port.write(next_move.encode())
        return 0


#main
def Arduino_comunicate(arduino_port, arduino_offset, color_used, COLORTABLE):
    while(True):
        if arduino_port.isOpen():
            monitor=Arduino_read(arduino_port)
            if (monitor=="o" ):
                Arduino_write_pos(arduino_port, arduino_offset, color_used, COLORTABLE)
                arduino_offset += 1
            else:
                print(monitor)

