# Sfevy
Sockets for everyone - Easy sockets within python, no stress networking.

### What is Sfevy?
Sfevy is an simple wrapper for the python sockets library. Sfevy was created so that anyone can simply create a networking application in python.
Although it is a 

### Requirements
- Python 3.x.x

### Features
- Made for quick and easy usage
- Threaded networking
- Made for beginners, but scaleable for more advanced users

### Setting up Sfevy
Start by cloning Sfevy from github

[Clone Sfevy](https://github.com/TheVoxcraft/Sfevy)

Then continue by importing Sfevy into your project
```python
import Sfevy
```


### Documentation

Start by initializing Sfevy
```python
sf = Sfevy.sockets
```
If you have the the proper parameters, initialize this way
```python
sf = Sfevy.sockets(HOST, PORT, IP)
```
- Host being the server or what you'll be trying to connect to
- IP being your ip, either local or external
- Port being the port you want to communicate through
These parameters can be later changed at any point, manually or through the Sfevy methods
```python
sf.HOST = '1.2.3.4'
sf.PORT = 1234
sf.IP = '127.0.0.1'
```
Or
```python
sf.setHost('1.2.3.4', 1234)    # changing the host you'll communicate out from and the port
sf.setAddress('1.2.3.4', 1234) # changing the ip you'll communicate back through and the port
```


You can easily send data through Sfevy using the `sendData()` function. This is threaded
Call this with the proper parameters: `data` and `protocol`. Also some optional parameters `buffer` and `raw`
- Data is what you want to send to the host ip, this could be for exampel text or binary.
- Protocol is what internet protocol you would like to use, either `UDP` or `TCP`. Example: `Protocol.TCP`

  - If you don't know which to use - use this as referance:
[Learn more about TCP and UDP](http://www.diffen.com/difference/TCP_vs_UDP)
- Buffer is how much data you want to send. Buffer is set to `1024` by default.
- Raw is a boolean, for if you want to send text, or raw data with no encoding. Raw is set to `False` by default.

Example:
```python
sf.sendData('Hello Server!', Protocol.UDP) # or ('Hello Server!', Protocol.UDP, buffer=1024, raw=False)
```

You can quickly also set up python to listen for traffic heading it's way
This is done by using the `startListening` method which starts listening for data. This is also threaded
You can call this with the following parameters: `dataHandler` and `protocol`.This also has the optional parameters `buffer` and `raw`.
For the listening function you need a function that handles the data when it comes.
- The Data Handler is the name of your function that handles the data when it comes in. Your function must have two parameters `data` for the incoming data, and `addr` for the address the data is coming from.
```python
myDataFunc(data, addr):
    print( "Data is %s, coming from %s" % (str(data), str(addr)) ) # assuming the data isn't raw

sf.startListening('myDataFunc', Sfevy.Protocol.UDP)
```
- Protocol is what internet protocol you would like to use, either `UDP` or `TCP`. Example: `Protocol.UDP`
  - If you don't know which to use - use this as referance:
[Learn more about TCP and UDP](http://www.diffen.com/difference/TCP_vs_UDP)
- Buffer is how much data you want to send. Buffer is set to `1024` by default.
- Raw is a boolean, for if you want to send text, or raw data with no encoding. Raw is set to `False` by default.
Example:
```python
sf.startListening('myDataFunc', Protocol.UDP) # extended: ('myDataFunc', Sfevy.Protocol.UDP, buffer=1024, raw=False)
```

#### UDP Echo Client/Server Example:
- Client:
```python
import Sfevy
import random
import time

Protocol = Sfevy.Protocol
sf = Sfevy.sockets('1.2.3.4', 1234) # 1.2.3.4 being the server ip

def reciveDataFunc(data, addr):
    print(data)

sf.startListening('reciveDataFunc', Protocol.UDP)

while 1:
    time.sleep(2)
    dataToSend = str( random.randint(0,10000) )
    sf.sendData(dataToSend, Protocol.UDP) # sends random number to server
```
- Server:
```python
import Sfevy
import time

Protocol = Sfevy.Protocol
sf = Sfevy.sockets('0.0.0.0', 1234, '127.0.0.1') # host ip doesn't matter on the server since it's not going to connect

def echoFunc(data, addr):
    sf.sendData(data, addr) # send same data back

sf.startListening('echoFunc', Protocol.UDP)
while 1:
    time.sleep(5)
    print('waiting for data...')
```
