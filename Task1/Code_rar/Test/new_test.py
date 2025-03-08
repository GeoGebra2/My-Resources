import serial

portx = "/dev/ttyUSB0"
bps = 115200
ser = serial.Serial(portx,bps)

while True:
    data = input("get: ")
    # print(data)
    ser.write(str(data) + '\n')
    # print(ser.read(20).decode())
