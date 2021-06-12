from ownlibs.poh_led import Light
import time
#import logging
#import uos
from MicroWebSrv2.MicroWebSrv2  import *                         
from time          import sleep
from _thread       import allocate_lock
import json

led1 = Light(5)
led1.TurnOnSync()
print(led1.CheckStatusSync())
time.sleep(1)
led1.ToggleSync()
print("Done")
def _httpHandlerLEDPost(httpClient, httpResponse):
    content = httpClient.ReadRequestContent()  # Read JSON color data
    colors = json.loads(content)
    blue, green, red = [colors[k] for k in sorted(colors.keys())]
    np[0] = (green, red, blue)
    #np.write()
    httpResponse.WriteResponseJSONOk()

routeHandlers = [ ( "/led", "POST",  _httpHandlerLEDPost ) ]
srv = MicroWebSrv2(routeHandlers=routeHandlers, webPath='/www/')
srv.Start(threaded=False)

# Instanciates the MicroWebSrv2 class,
mws2 = MicroWebSrv2()

# SSL is not correctly supported on MicroPython.
# But you can uncomment the following for standard Python.
# mws2.EnableSSL( certFile = 'SSL-Cert/openhc2.crt',
#                 keyFile  = 'SSL-Cert/openhc2.key' )

# For embedded MicroPython, use a very light configuration,
mws2.SetEmbeddedConfig()

# All pages not found will be redirected to the home '/',
mws2.NotFoundURL = '/'

# Starts the server as easily as possible in managed mode,
mws2.StartManaged()

# Main program loop until keyboard interrupt,
try :
    while mws2.IsRunning :
        sleep(1)
except KeyboardInterrupt :
    pass

# End,
print()
mws2.Stop()
print('Bye')
print()