import serial
from time import sleep
from curses import ascii

ser = serial.Serial()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 115200
ser.timeout = 1

try:
    ser.open()
except serial.SerialException as e:
    print("Error opening the serial port:", str(e))
    exit()

def send_command(command):
    ser.write(str.encode(command + '\r\n'))
    sleep(1)  # Allow some time for the module to respond
    response = ser.read_all().decode('utf-8')
    print(f"Command: {command}\nResponse: {response}")

# Send initialization commands
send_command('AT')
send_command('AT+CMGF=1')
send_command('AT+CPMS="ME","SM","ME"')

def send_sms(smsdata):
    send_command('AT+CMGF=1')
    sleep(2)
    send_command('AT+CMGS="%s"' % smsdata['phone'])
    sleep(2)
    send_command(smsdata['message'])
    sleep(2)
    send_command(ascii.ctrl('z'))

sms_data = {"phone": "+998972557191", "message": "Assalomu aleykum"}
send_sms(sms_data)

ser.close()

