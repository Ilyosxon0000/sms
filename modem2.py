import serial
import time

def send_sms(a="+998972557191", b="modemni ishlatayapman"):
    try:
        with serial.Serial('/dev/ttyUSB1', baudrate=115200, bytesize=8, timeout=5) as s:
            print('Opened...')
            time.sleep(1)
            
            print(s.read_all())  # Print initial response
            
            s.write(b'ATZ\r\n')
            time.sleep(2)
            print(s.read_all())  # Print response after ATZ
            
            s.write(b'AT+CMGF=1\r')
            time.sleep(2)
            print(s.read_all())  # Print response after AT+CMGF=1
            
            s.write(b'AT+CSCA="+998930190007"\r')
            time.sleep(2)
            print(s.read_all())  # Print response after AT+CSCA
            
            s.write(f'AT+CMGS="{a}"\r'.encode())
            time.sleep(2)
            print(s.read_all())  # Print response after AT+CMGS
            
            s.write(f'{b}\r'.encode())
            time.sleep(1)
            
            s.write(chr(26).encode())
            time.sleep(1)
            
            print("error:",s.read_all())  # Print final response
            print("Finished")

    except serial.SerialException as e:
        print(f"Serial Exception: {e}")

    except Exception as e:
        print(f"Error: {e}")

# Test the function
send_sms()
time.sleep(3)
send_sms()
# 8600303605626576