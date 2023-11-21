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
    time.sleep(1)
    s.write(b'AT+CMGF=1\r\n')
    time.sleep(1)
    s.write(b'AT+CSCA="+998901850488"\r\n')#FOr beeline
    time.sleep(1)
    # s.write(b'AT+CSCA="+998930190007"\r\n')
    # time.sleep(1)
    s.write('AT+CMGS="+998970517191"\r\n'.encode())
    time.sleep(1)
    s.write('Bizni modem HSDPA ekan Al-Xorazmiydagi modem HSUPA ekan.Farqi bor ekan!'.encode())
    time.sleep(1)
    s.write(str.encode(ascii.ctrl('z')))
    
    w = s.read_all()
    print(w)
    print("finished")
    s.close()

send_sms()
time.sleep(1)
send_sms()

