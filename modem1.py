import serial
import time

def send_sms(a="+998972557191", b="modemni ishlatayapman"):
    s = serial.Serial()
    s.port = '/dev/ttyUSB1'  # Replace with your actual serial port
    s.baudrate = 115200
    s.bytesize = 8
    s.write_timeout = 1
    s.timeout = 1

    try:
        s.open()
        print('opened...')
        time.sleep(1)
        
        s.write(b'ATZ\r\n')
        time.sleep(2)
        
        s.write(b'AT+CMGF=1\r')
        time.sleep(2)
        
        s.write(b'AT+CSCA="+998930190007"\r')
        time.sleep(2)
        
        s.write(f'AT+CMGS="{a}"\r'.encode())
        time.sleep(2)
        
        s.write(f'{b}\r'.encode())  # Include '\r' at the end
        time.sleep(1)
        
        s.write(chr(26).encode())
        time.sleep(1)
        
        response = s.read_all()
        print(response)
        print("finished")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        s.close()

# Test the function
send_sms()
time.sleep(3)
send_sms()
