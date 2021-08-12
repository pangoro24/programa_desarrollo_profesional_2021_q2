#Librerias
import time
from machine import Pin
import network
import socket

#Configuración inicial de WiFi
ssid = ''  #Nombre de la Red
password = '' #Contraseña de la red
wlan = network.WLAN(network.STA_IF)

wlan.active(True) #Activa el Wifi
wlan.connect(ssid, password) #Hace la conexión

while wlan.isconnected() == False: #Espera a que se conecte a la red
    pass

print('Conexion con el WiFi %s establecida' % ssid)
print(wlan.ifconfig()) #Muestra la IP y otros datos del Wi-Fi

#Salidas
led1 = Pin(4, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(15, Pin.OUT)

#Pagina web
def web_page():  
    html = '''<html>
    <head>
    <title>ESP Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" href="data:," />
    <style>
    html {
        font-family: Helvetica;
        display: inline-block;
        margin: 0px auto;
        text-align: center;
    }
    h1 {
        color: #0f3376;
        padding: 2vh;
    }
    p {
        font-size: 1.5rem;
    }
    .button {
        display: inline-block;
        background-color: #e7bd3b;
        border: none;
        border-radius: 4px;
        color: white;
        padding: 16px 40px;
        text-decoration: none;
        font-size: 30px;
        margin: 2px;
        cursor: pointer;
    }
    .button2 {
        background-color: #4286f4;
    }
    </style>
    </head>
    <body>
    <h1>ESP Web Server</h1>
    <p>GPIO_state: <strong>""" + gpio_state + """</strong></p>
    <p>
    <a href="/?led=on"><button class="button">ON</button></a>
    </p>
    <p>
    <a href="/?led=off"><button class="button button2">OFF</button></a>
    </p>
    </body>
    </html>'''
    return html

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('', 80))
tcp_socket.listen(6)

while True:
    conn, addr = tcp_socket.accept()
    print('Nueva conexion desde:  %s' % str(addr))
    request = conn.recv(1024)
    print('Solicitud = %s' % str(request))
    request = str(request)
    if request.find('/?led1=on' ) == 6:
        print('Led ON')
        led1.value(1)
    if request.find('/?led2=on' ) == 6:
        print('Led ON')
        led2.value(1)
    if request.find('/?led3=on' ) == 6:
        print('Led ON')
        led3.value(1)
    if request.find('/?led1=off') == 6:
        print('Led OFF') 
        led1.value(0)
    if request.find('/?led2=off') == 6:
        print('Led OFF') 
        led2.value(0)
    if request.find('/?led3=off') == 6:
        print('Led OFF') 
        led3.value(0)

    #Mostrar Página
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()