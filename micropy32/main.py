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
    btn= bt1.CheckStatusSync()
    
    if not btn:
        print("Encendido")
    else:
        print("Apagado")
    time.sleep(1)
    