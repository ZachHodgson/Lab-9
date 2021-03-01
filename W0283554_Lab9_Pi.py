import serial
from guizero import *
from time import sleep

#serial setup
ArduinoSerial = serial.Serial('/dev/ttyACM0', 9600)
ArduinoSerial.flush()
sleep(3)

Servo1Save = []
Servo2Save = []

def slider_angle(slider_num):
    ArduinoSerial.write(str('M1').encode('utf-8'))
    ArduinoSerial.write(str('\n').encode('utf-8'))
    ArduinoSerial.flush()
    data = int(slider_num)
    ArduinoSerial.write(str(data).encode('utf-8'))
    ArduinoSerial.write(str('\n').encode('utf-8'))
    print(data)
    sleep(.05)
    ArduinoSerial.flush()


def slider2_angle(slider_num2):
    ArduinoSerial.write(str('M2').encode('utf-8'))
    ArduinoSerial.write(str('\n').encode('utf-8'))
    ArduinoSerial.flush()
    data2 = int(slider_num2)
    ArduinoSerial.write(str(data2).encode('utf-8'))
    ArduinoSerial.write(str('\n').encode('utf-8'))
    print(data2)
    sleep(.05)
    ArduinoSerial.flush()


def RecordButton():
    Servo1Save.append(slider1.value)
    Servo2Save.append(slider2.value)


def RepeatButton():
    for i in range (len(Servo1Save)):
        ArduinoSerial.write(str('M1').encode('utf-8'))
        ArduinoSerial.write(str('\n').encode('utf-8'))
        ArduinoSerial.flush()
        data = int(Servo1Save[i])
        ArduinoSerial.write(str(data).encode('utf-8'))
        ArduinoSerial.write(str('\n').encode('utf-8'))
        print(data)
        ArduinoSerial.flush()

        ArduinoSerial.write(str('M2').encode('utf-8'))
        ArduinoSerial.write(str('\n').encode('utf-8'))
        ArduinoSerial.flush()
        data2 = int(Servo2Save[i])
        ArduinoSerial.write(str(data2).encode('utf-8'))
        ArduinoSerial.write(str('\n').encode('utf-8'))
        print(data2)
        ArduinoSerial.flush()

        sleep(2)



app = App("RC servo controlPos", height = 200)
slider1 = Slider(app, width = "fill", start = (-90), end = 90, command = slider_angle)
slider2 = Slider(app, width = "fill", start = (-90), end = 90, command = slider2_angle)
Record = PushButton(app, text = "Record", command = RecordButton)
Repeat = PushButton(app, text = "Repeat", command = RepeatButton)

app.display()
ArduinoSerial.close()