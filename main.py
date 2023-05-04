import serial
import time

# # make sure the 'COM#' is set according the Windows Device Manager
# ser = serial.Serial('COM3', 9800, timeout=1)
# time.sleep(2)
#
# for i in range(50):
#     line = ser.readline()   # read a byte
#     if line:
#         string = line.rstrip()
#         string = line.decode()  # convert the byte string to a unicode string
#         #num = int(string) # convert the unicode string to an int
#         print(string)
#
# ser.close()

def read() :
    ser = serial.Serial('COM3', 9800, timeout=1)
    while True :
        line = ser.readline()
        data = line.decode()
        print(data)
    ser.close()



if __name__ == '__main__' :
    read()