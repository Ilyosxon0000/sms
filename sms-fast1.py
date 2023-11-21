import serial
import time

print("started...")

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

def send_command(command):
    ser.write((command + '\r\n').encode('utf-8'))
    time.sleep(1)
    response = ser.read_all().decode('utf-8')
    print(f"Command: {command}\nResponse: {response}")
    return response

# Send initialization commands
send_command('AT')
send_command('AT+CMGF=1')
send_command('AT+CPMS="ME","SM","ME"')

def send_sms(smsdata):
    send_command('AT+CMGF=1')
    send_command('AT+CMGS="%s"' % smsdata['phone'])
    send_command(smsdata['message'] + chr(26))
data=[
    {"phone": "+998972557191", "message": "Assalomu aleykum1"},
    {"phone": "+998972557191", "message": "Assalomu aleykum2"},
    {"phone": "+998972557191", "message": "Assalomu aleykum3"},
    {"phone": "+998972557191", "message": "Assalomu aleykum4"},
    {"phone": "+998972557191", "message": "Assalomu aleykum5"},
    {"phone": "+998972557191", "message": "Assalomu aleykum6"},
    {"phone": "+998972557191", "message": "Assalomu aleykum7"},
    {"phone": "+998972557191", "message": "Assalomu aleykum8"},
]
# sms_data = {"phone": "+998972557191", "message": "Assalomu aleykum"}
for item in data:
    send_sms(item)
    time.sleep(1)
print("finished...")
ser.close()
