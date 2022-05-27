import serial #untuk komunikasi serial
import time #untuk delay/sleep
import struct #untuk mengubah integer ke string byte

ser=serial.Serial('/dev/ttyUSB0', 2000000) #komunikasi ke arduino dengan baudrate 2000000

time.sleep(5) #delay lima detik (untuk menyiapkan arduino)

for i in range(0,100):
    time.sleep(0.1) #supaya gak langsung berhenti motornya (tiap 0.1 detik ganti kecepatan)
    # mengirimkan perintah untuk menggerakan roda kiri ('l') dengan kecepatan i
    ser.write(b'l'+struct.pack("B", i))

for i in range(99,59,-1):
    time.sleep(0.1) #supaya gak langsung berhenti motornya (tiap 0.1 detik ganti kecepatan)
    # mengirimkan perintah untuk menggerakan roda kiri ('l') dengan kecepatan i
    ser.write(b'l'+struct.pack("B", i))

ser.write(b'k')

