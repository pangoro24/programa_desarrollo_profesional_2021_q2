from machine import Pin
import time

button=Pin(15,Pin.IN, Pin.PULL_UP)
ledd=Pin(4,Pin.OUT)

while True:
    state=button.value()
    if not state:
        ledd.value(1)
    else:
        ledd.value(0)
    print(state)
    time.sleep(1)