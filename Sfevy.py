# Sfevy - Sockets for everyone
# by Vox

# Copyright (c) 2017 VOX
#      MIT LICENSE

import socket
import threading

class Protocol():
    TCP = 1
    UDP = 2

class sockets:
    def __init__(self, host, port, ip=socket.gethostname()):
        self.listening = False
        self.IP = ip
        self.HOST = host
        self.PORT = port
    def setHost(host, port):
        self.HOST = host
        self.PORT = port
    def setAddress(self, ip, port):
        self.IP = ip
        self.PORT = port
    def sendData(self, data, pcol, raw=False):
        if raw == False:
            data = bytes(data, "utf-8")
        
        if pcol == Protocol.TCP:
            threading.Thread(target=sockets._sendTCPThread, args=(self, data)).start()
        elif pcol == Protocol.UDP:
            threading.Thread(target=sockets._sendUDPThread, args=(self, data)).start()
        else:
            print("error: Not avaliable protocol.")
    def _sendUDPThread(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(data, (self.HOST, self.PORT))
        sock.close()
    def _sendTCPThread(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        sock.connect((self.HOST, self.PORT))
        sock.sendall(data)
        sock.close()
    def startListening(self, dataHandler, pcol, buffer=1024, raw=False):
        if(self.listening == False and pcol == Protocol.UDP):
            threading.Thread(target=sockets._listenUDP, args=(self, dataHandler, buffer, raw)).start()
        elif(self.listening == False and pcol == Protocol.TCP):
            threading.Thread(target=sockets._listenTCP, args=(self, dataHandler, buffer, raw)).start()
        else:
            print("error: Already listening.")
    def  _listenUDP(self, dataHandler, buffer, raw):
        while 1:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((self.IP, self.PORT))
            data, addr = sock.recvfrom(buffer)
            if not raw:
                gData = data.decode()
            gAddr = addr[0]
            threading.Thread(target=sockets._gotData, args=(gData,gAddr,dataHandler)).start()
            sock.close()
    def _listenTCP(self, dataHandler, buffer, raw):
        while 1:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.IP, self.PORT))
            sock.listen(5)
            connection, client_address = sock.accept()
            while True:
                data = connection.recv(buffer)
                if data:
                    if not raw:
                        data = data.decode()
                    threading.Thread(target=sockets._gotData, args=(data,client_address,dataHandler)).start()
                else:
                    break
                connection.close()
                sock.close()
    def _gotData(data, addr, callTarget):
        ## Call user function here
        main_module = __import__('__main__')
        callFunc = getattr(main_module, callTarget)
        callFunc(data, addr)
