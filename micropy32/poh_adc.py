from machine import ADC
class Adc:
    def _init_ (self,pin ):
        self.pin = pin
        self.reader = ADC(self.pin)
        print("Adc inicializado")
    def CheckStatusSync(self ):
        return self.reader.read() 
        