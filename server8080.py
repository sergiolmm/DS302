import struct
import socket
import sys 
import _thread
import xml.etree.ElementTree as ET
import envio as sd
import respostas as rp
import util as ut
import uuid


def on_new_client(clientesocket, addr):
    while True:
        msg = clientesocket.recv(1024)
        if msg:
            print (str(addr) + ' >> \n' + msg.decode().replace('\r\n','\n') )
            break;
        else:
            break;

    msg1 = msg.decode()
    
    if msg1.__contains__('/index.html') | msg1.__contains__('/ ') :
        msg = sd.sendHTTP(rp.sendIndex())
    else:
        msg = ( 'HTTP/1.1 404 Not Found\r\n'
                'Date: Sun, 18 Oct 2009 10:36:20 GMT\r\n'
                'Server: Wemo\r\n'
                'Content-Type: text/html; charset=iso-8859-1\r\n'
                'Connection: close\r\n'  
                '\r\n'
                '\r\n'
                '<!DOCTYPE HTML>\r\n'
                '<html><head><title>404 Not Found</title></head><body>\r\n'
                '<h1>Pagina nao encontrada neste site</h1><p>The requested URL /t.html was not found on this server.</p></body>\r\n'
                '</html>\r\n')
    clientesocket.send(msg.encode())
    clientesocket.close()

# http part - thread para servir como webserver local

https = ut.get_ip()
hport = 8080

sockH = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sockH.bind((https,hport))
    print("bind Servidor http" + https)
except socket.error:
    sockH.bind(('', hport))
    print("bind Servidor http")

sockH.listen(1)
print('Listiong HTTP on '+https+' port : '+ str(hport)+ '\n')
while True:
    try:
        c, addr = sockH.accept()
        print('aberto um socket')
        _thread.start_new_thread(on_new_client,(c,addr))
    except KeyboardInterrupt:
        break    
    
sockH.close()    
print('\nFinalizando o servidor http')
