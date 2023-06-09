import serial
import time
import schedule



ser = serial.Serial('COM4', 115200,parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
    timeout=5)


def tryout(test):
    
    data = ser.readline()
    while True:
        while ser.in_waiting:
            data = ser.readline()
            decoded_values = str(data[0:len(data)].decode("utf-8"))
            print (decoded_values)
            return(decoded_values)
            
        print(type(test))
        ser.write(test.encode('utf-8'))
        
    
