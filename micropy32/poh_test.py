from poh_adc import Adc
import time
#import logging

reader1 = Adc(27)
while  True:
    print(reader1.CheckStatusSync())
    time.sleep(1)
