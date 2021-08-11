from machine import ADC
class Adc:
    def init(self, pin):
        self.pin = pin
        self.ac = ADC(self.pin)
        print("Adc inicializado")
