from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
Voltaje= 0
while True:
    pot_value = pot.read()
    Voltaje= (pot_value * 3.3)/4095

    print(Voltaje)
    sleep(0.5)