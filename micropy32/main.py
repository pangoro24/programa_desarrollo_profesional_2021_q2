from poh_led import Light
from poh_btn import Bouton
import time
#import logging
bt1= Bouton(4)

led1 = Light(5)
led1.TurnOnSync()
print(led1.CheckStatusSync())
time.sleep(1)
led1.ToggleSync()
print("Done")

while True:
    bt1=bouton.value()
    if not bt1:
        led1.value(1)
    else:
        led1.value(0)
    print(bt1)
    time.sleep(1)