import logging
from gpiozero import LED as DO

class Light:
    def __init__(self, pin):
        """Inicializacion de un led
        Parameters
        ----------
        pin : int
            gpio, not board
        """
        self.pin = pin
        self.light = DO(self.pin)
        logging.debug("Led was set at pin# " + str(self.pin))

    async def TurnOn(self):
        self.light.on()
        logging.debug("Led_{} turned on".format(self.pin))

    async def TurnOff(self):
        self.light.off()
        logging.debug("Led_{} turned off".format(self.pin))
        
    async def CheckStatus(self):
        return self.light.is_active

    def TurnOnSync(self):
        self.light.on()
        logging.debug("Led_{} turned on".format(self.pin))

    def TurnOffSync(self):
        self.light.off()
        logging.debug("Led_{} turned off".format(self.pin))
    
    def ToggleSync(self):
        self.light.toggle()
        return self.light.is_active
    
    def CheckStatusSync(self):
        return self.light.is_active