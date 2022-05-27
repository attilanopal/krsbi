import serial
import time
import struct

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)
for i in range (1,10):
    ser.write(b''+struct.pack("B", 300))
    a = ser.readline()
    print(a)
    print(a[0:4])
    b = ser.readline()
    print(b)
