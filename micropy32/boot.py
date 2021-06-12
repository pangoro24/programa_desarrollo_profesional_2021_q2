# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

import machine
from machine import Pin
import network
import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'router'
password = '12342424'
"""
station = ""
if machine.reset_cause() != machine.SOFT_RESET:
    station = network.WLAN(network.STA_IF)
    # configuration below MUST match your home router settings!!
    station.ifconfig('192.168.1.202','255.255.255.0','192.168.1.1','8.8.8.8')
    station.active(True)

if not station.isconnected():
    # change the line below to match your network ssid, security and password
    station.connect(ssid, auth=(network.WLAN.WPA2, password), timeout=5000)
    while not station.isconnected():
        machine.idle() # save power while waiting

"""
station = network.WLAN(network.STA_IF)
station.ifconfig(('192.168.1.202', '255.255.255.0', '192.168.1.1', '8.8.8.8'))
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

#led = Pin(25, Pin.OUT)