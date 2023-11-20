import serial
import time
from curses import ascii

def send_sms(a="+998972557191", b="modemni ishlatayapman"):
    s = serial.Serial()
    s.port = '/dev/ttyUSB0'
    s.baudrate = 115200
    s.bytesize=8
    s.write_timeout=1
    # s.inter_byte_timeout = 1
    s.timeout = 1
    s.open()
    print('opened...')
    time.sleep(1)
    s.write(b'ATZ\r\n')
    time.sleep(2)
    s.write(b'AT+CMGF=1\r\n')
    time.sleep(2)
    # s.write(b'AT+CSMP=17,129,0,0\r\n')
    # time.sleep(1)
    s.write(b'AT+CSCA="+998930190007"\r\n')
    time.sleep(2)
    s.write('AT+CMGS="+998972557191"\r\n'.encode())
    time.sleep(2)
    s.write('salom'.encode())
    time.sleep(1)
    s.write(str.encode(ascii.ctrl('z')))
    # s.write(chr(26).encode())
    # time.sleep(1)
    
    w = s.read_all()
    print(w)
    print("finished")
    s.close()

send_sms()
time.sleep(3)
send_sms()

