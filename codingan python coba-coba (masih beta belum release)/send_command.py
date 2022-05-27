import serial

arduino = serial.Serial('/dev/ttyUSB0',9600)

def ledController():
	cmd = input('type on/off/dc : ')
	cmd = str.lower(cmd)
	if(cmd == "f"):
		arduino.write('F'.encode())
		print("Forward")
	elif(cmd == "b"):
		arduino.write('B'.encode())
		print("Mundur")
	elif ( cmd == "c"):
		arduino.close()
	else:
		print("Ngetik yang bener pilih on / off / dc")

try:
	while (True):
		ledController()
except KeyboardInterrupt:
	arduino.close()
print('has disconnected')