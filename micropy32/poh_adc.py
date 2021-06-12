from machine import ADC as Adc
class Adc:
    def _init_ (self,Adc ):
        self.ADC = Adc
        self.ADC = Adc(self.ADC,Adc.IN)
        print("Adc inicializado")
    def CheckStatusSync(self ):
        return self.Adc.read() 
        