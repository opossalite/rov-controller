import serial

with serial.Serial('COM3', 9600) as ser:
    x = ser.readline()
    print(x)

    ser.write("this is my arduino message\n".encode("utf-8"))

    y = ser.readline()
    y.decode("utf-8")
    print(y)

    #ser.close()