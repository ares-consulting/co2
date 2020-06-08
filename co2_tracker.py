# http://eleparts.co.kr/data/design/product_file/SENSOR/gas/MH-Z19_CO2%20Manual
# http://qiita.com/UedaTakeyuki/items/c5226960a7328155635f
# https://amzn.to/37SRFFF

import serial
import time
import requests

def mh_z19():

    ser = serial.Serial(
        '/dev/ttyAMA0',
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=1.0)

    while 1:
        #result=ser.write("\xff\x01\x86\x00\x00\x00\x00\x00\x79")
        s=ser.read(9)
        if s[0] == "\xff" and s[1] == "\x86":
            return {'co2': ord(s[2])*256 + ord(s[3])}
            break

    if __name__ == '__main__':
        value = mh_z19()
        #print "co2=", value["co2"]

    r = requests.post(
        url = "https://",
        data = {'co2': value["co2"]})
    #print("Response:%s"%r.text)
