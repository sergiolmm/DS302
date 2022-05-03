
def sendIndex():
    msg = ( '<!DOCTYPE HTML>\r\n'
            '<html><head><title>Hello</title></head>\r\n'
            '<body><h1>Alo mundo virtual Wemo</h1>'
            '<p>Vamos iniciar no mundo Iot...</p></body></html>\r\n')
    return msg

if __name__ == '__main__':
    print('Testando  -> ')
    print(sendIndex())

