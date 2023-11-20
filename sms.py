import  serial, time
from time import sleep
from curses import ascii

ser = serial.Serial()
ser.port = '/dev/ttyUSB0'

ser.baudrate = 115200
ser.timeout = 1
ser.open()
ser.write(str.encode('AT+CMGF=1\r\n'))
ser.write(str.encode('AT+CPMS="ME","SM","ME"\r\n'))

def sendsms(smsdata):
    ser.write(str.encode('AT+CMGF=1\r\n'))
    sleep(2)
    ser.write(str.encode('AT+CMGS="%s"\r\n' % smsdata['phone']))
    sleep(2)
    ser.write(str.encode('%s' % smsdata['message']))
    sleep(2)
    ser.write(str.encode(ascii.ctrl('z')))

print(sendsms({"phone":"+998972557191","message":"Assalomu aleykum"}))