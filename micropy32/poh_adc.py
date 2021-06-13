from machine import Pin,ADC
class Adc:
    def __init__(self, pin):
        self.pin = pin
        self.r = ADC(self.pin)
        print("Adc inicializado")
    def CheckStatusSync(self):
        return self.r.read() 
        