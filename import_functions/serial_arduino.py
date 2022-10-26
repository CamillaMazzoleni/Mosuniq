import serial
import time

ArduinoSerial = serial.Serial('COM3',9600, timeout=1)
ArduinoSerial.close()
ArduinoSerial.open()
time.sleep(5)

x='helloworld'
#read from Arduino
#write to arduino
#ArduinoSerial.close()
#time.sleep(1)
#ArduinoSerial.open()
#time.sleep(1)
#while (True):
    #if ArduinoSerial.isOpen():
ArduinoSerial.write(x.encode());
time.sleep(2)
ard=ArduinoSerial.readline()
print(ard.decode())
