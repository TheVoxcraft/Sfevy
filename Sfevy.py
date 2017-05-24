# Sfevy - Sockets for everyone
# by Vox

# Copyright (c) 2017 VOX
#      MIT LICENSE

import socket
import threading

class Protocol(Enum):
    TCP = 1
    UDP = 2

class Client:
    def __init__(self, ip, port):
        self.IP = ip
        self.PORT = port
    def setAddress(ip, port):
        IP = ip
        PORT = port
    def sendData(self, data, pcol, raw=False):
        if pcol == Protocol.TCP:
            threading.Thread(target=_sendTCPThread, args=(data, raw)).start()
        elif pcol == Protocol.UDP:
            threading.Thread(target=_sendUDPThread, args=(data, raw)).start()
        else:
            print("error: Not avaliable protocol.")
    def _sendUDPThread(self, data, raw):
        if raw == False:
            sData = bytes(data, "utf-8")
        else:
            sData = data
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(, (self.IP, self.PORT))
        sock.close()
    def _sendTCPThread(self, data, raw):
        if raw == False:
            sData = bytes(data, "utf-8")
        else:
            sData = data
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        sock.connect((self.IP, self.PORT))
        sock.sendall(sData)
        sock.close()
        
class Server:
    
    def __init__(self, ip, port):
        self.listening = False
        self.IP = ip
        self.PORT = port
    def setAddress(self, ip, port):
        IP = ip
        PORT = port
    def StartListening(self, dataHandler, pcol, buffer=1024)
        if(self.listening == False && pcol == Protocol.UDP):
            threading.Thread(target=_listenUDP, args=(dataHandler, buffer)).start()
        elif(self.listening == False && pcol == Protocol.TCP):
            threading.Thread(target=_listenTCP, args=(dataHandler)).start()
        else:
            print("error: Already listening.")
    def  _listenUDP(dataHandler, buffer):
        while 1:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((self.IP, self.PORT))
            data, addr = sock.recvfrom(buffer)
            gData = data.decode()
            gAddr = addr[0]
            threading.Thread(target=gotData, args=(gData,gAddr)).start()
            sock.close()
    def _listenTCP(dataHandler, buffer): ## fix
        while 1:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.IP, self.PORT))
            sock.listen(5)
            
            gData = data.decode()
            gAddr = addr[0]
            threading.Thread(target=gotData, args=(gData,gAddr)).start()
            sock.close()
    def gotData(data, addr):
        ## Call user function here
