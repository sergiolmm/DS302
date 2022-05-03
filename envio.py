
def sendXML(msg):
   resp = ('HTTP/1.1 200 OK\r\n'
           'Content-Type: text/xml\r\n'
           'CONTENT-LENGTH: '+str(len(msg.encode("utf8")))+'\r\n'
           'Connection: close\r\n'  
           '\r\n' + msg)
   return resp 

def sendHTTP(msg):
   resp = ('HTTP/1.1 200 OK\r\n'
           'Content-Type: text/html\r\n'
           'CONTENT-LENGTH: '+str(len(msg.encode("utf8")))+'\r\n'
           'Connection: close\r\n'  
           '\r\n' + msg + '\r\n\r\n')
   return resp 

def sendHTTPBadRequest(msg):
   resp = ('HTTP/1.1 400 Bad request\r\n'
           'Content-Type: text/html\r\n'
           'CONTENT-LENGTH: '+str(len(msg.encode("utf8")))+'\r\n'
           'Connection: close\r\n'  
           '\r\n' + msg + '\r\n\r\n')
   return resp 

if __name__ == '__main__':
    print('Testando sendHTTP() -> ')
    import respostas as rep
    print(sendXML(rep.sendIndex()))
    print('Testando sendHTTPBadRequest() -> ')
    print(sendHTTPBadRequest(rep.sendIndex()))    