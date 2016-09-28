import serial
from serial.tools.list_ports import comports

ports = comports()
print("Available ports:")
for index in range(0, len(ports)):
    print("{0}: {1}".format(index, ports[index].device))

num = int(input("Choose serial port: "))
port = serial.Serial(ports[num].device, 9600)

while True:
    inputString = input()
    port.write(inputString)
    print(port.read(1))
