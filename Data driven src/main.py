import serial
import time
import csv


def read():
    counter = 0
    global data_list
    global time_list
    global javad
    data_list = list()
    time_list = list()
    ser = serial.Serial('COM3', 9800, timeout=2)
    for i in range(1, 5):
        line = ser.readline()
        data1 = line.strip()
        data = data1.decode()
        data_list.append(data)
        time1 = time.ctime()
        time_list.append(time1)
        print(data, time1)
        # counter =+ 1
        # print(counter)
    ser.close()
    javad = zip(data_list, time_list)
    return javad


def write():
    header = ['humidity', 'time']
    with open("humidity_data.csv", 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(javad)


if __name__ == '__main__':
    read()
    write()
