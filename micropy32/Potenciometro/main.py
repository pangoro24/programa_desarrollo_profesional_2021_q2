from machine import ADC
import time
#import logging

lectura= 0
entrada = ADC(0)
while  True:
    lectura = entrada.read()
    print(lectura)
    time.sleep(1)