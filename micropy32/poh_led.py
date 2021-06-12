#import logging
from machine  import Pin as DO

class Light:
    def __init__(self, pin):
        """Inicializacion de un led
        Parameters
        ----------
        pin : int
            gpio, not board
        """
        self.pin = pin
        self.light = DO(self.pin,DO.OUT)
        print("Led was initialized")
        #logging.debug("Led was set at pin# " + str(self.pin))

    async def TurnOn(self):
        self.light.on()
        print("Led was turned on")
        #logging.debug("Led_{} turned on".format(self.pin))

    async def TurnOff(self):
        self.light.off()
        #logging.debug("Led_{} turned off".format(self.pin))
        
    async def CheckStatus(self):
        #return self.light.is_active
        return 0

    def TurnOnSync(self):
        self.light.on()
        print("Led was turned on")
        #logging.debug("Led_{} turned on".format(self.pin))

    def TurnOffSync(self):
        self.light.off()
        print("Led was turned off")
        #logging.debug("Led_{} turned off".format(self.pin))
    
    def ToggleSync(self):
        v = self.light.value() 
        if v == 1:
            self.TurnOffSync()
        else:
            self.TurnOnSync()
        return self.light.value() 
    
    def CheckStatusSync(self):
        return self.light.value() 