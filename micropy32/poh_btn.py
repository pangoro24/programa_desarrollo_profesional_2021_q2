from machine import Pin

def bouton(npin):
    '''Indicar pin del boton'''
    button=Pin(npin,Pin.IN, Pin.PULL_UP)
    state=button.value()