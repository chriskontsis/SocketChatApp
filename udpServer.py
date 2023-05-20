import socket

MAX_SIZE_BYTES = 65535
#IvP4 address DGRAM is UDP STREAM is TCP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3000
hostname = '127.0.0.1'
s.bind((hostname, port)) #bind socket to a port and IP address
print('Listening at {}'.format(s.getsockname())) 


while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    upperCaseMessage = message.upper()
    print('The client at {} says {!r}'.format(clientAddress, message))
    data = upperCaseMessage.encode('ascii')
    s.sendto(data, clientAddress)