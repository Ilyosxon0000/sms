import serial
import time
from curses import ascii

def read_response(s):
    response = b""
    while True:
        char = s.read()
        if not char:
            break
        response += char
        if response.endswith(b'\r\nOK\r\n'):
            break
        elif response.endswith(b'\r\nERROR\r\n'):
            break
        elif response.endswith(b'\r\n> '):
            break
    return response.decode('utf-8')

def send_sms(a="+998972557191", b="modemni ishlatayapman"):
    s = serial.Serial()
    s.port = '/dev/ttyUSB1'
    s.baudrate = 115200
    s.bytesize = serial.EIGHTBITS
    s.timeout = 1
    s.write_timeout = 1

    try:
        s.open()
        print('Opened...')
        time.sleep(1)

        # Send ATZ command
        s.write(b'ATZ\r\n')
        response = read_response(s)
        print(response)
        time.sleep(2)

        # Set SMS mode
        s.write(b'AT+CMGF=1\r\n')
        response = read_response(s)
        print(response)
        time.sleep(2)

        # Set SMS center number
        s.write(b'AT+CSCA="+998930190007"\r\n')
        response = read_response(s)
        print(response)
        time.sleep(2)

        # Set the recipient phone number
        s.write(f'AT+CMGS="{a}"\r\n'.encode())
        response = read_response(s)
        print(response)
        time.sleep(2)

        # Send SMS message
        s.write(f'{b}\r\n'.encode())
        response = read_response(s)
        print(response)
        time.sleep(1)

        # Send CTRL+Z to terminate the message
        s.write(chr(26).encode())
        time.sleep(2)

        # Read the final response
        response = read_response(s)
        print(response)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Finished")
        s.close()

# Send SMS
send_sms()
time.sleep(3)
send_sms()
