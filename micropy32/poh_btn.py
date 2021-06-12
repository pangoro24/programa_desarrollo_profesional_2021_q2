from machine import Pin as BT
class Bouton:
    def __init__(self, pin):
        """Inicializacion de un led
        Parameters
        ----------
        pin : int
            gpio, not board
        """
        self.pin = pin
        self.bouton = BT(self.pin,BT.IN,BT.PULL_UP)
        print("Bouton was initialized")
        #logging.debug("Led was set at pin# " + str(self.pin))

    def CheckStatusSync(self):
        return self.bouton.value()
