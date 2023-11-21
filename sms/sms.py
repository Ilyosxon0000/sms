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

def send_sms(smsdata):
    send_command('ATZ')
    send_command('AT+CMGF=1')
    send_command('AT+CPMS="ME","SM","ME"')
    send_command('AT+CSCA="+998901850488"')
    send_command('AT+CMGS="%s"' % smsdata['phone'])
    send_command(smsdata['message'] + chr(26))
    time.sleep(1)  # Adjust as needed

while True:
    import random
    number=random.choice([0,1])
    data={"phone": "+998972557191", "message": "Assalomu aleykum1"}
    if number:
        send_sms(data)
    time.sleep(3)

print("finished...")
ser.close()
