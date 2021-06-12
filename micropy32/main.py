from poh_led import Light
import time
#import logging

led1 = Light(5)
led1.TurnOnSync()
print(led1.CheckStatusSync())
time.sleep(1)
led1.ToggleSync()
print("Done")
