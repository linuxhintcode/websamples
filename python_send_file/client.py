#!/usr/bin/env python3

# Importing libraries
import socket
import sys

# Lets catch the 1st argument as server ip
if (len(sys.argv) > 1):
    ServerIp = sys.argv[1]
else:
    print("\n\n Run like \n python3 client.py < serverip address > \n\n")
    exit(1)


# Now we can create socket object
s = socket.socket()

# Lets choose one port and connect to that port
PORT = 9898

# Lets connect to that port where server may be running
s.connect((ServerIp, PORT))

# We can send file sample.txt
file = open("sample.txt", "rb")
SendData = file.read(1024)


while SendData:
    # Now we can receive data from server
    print("\n\n################## Below message is received from server ################## \n\n ", s.recv(1024).decode("utf-8"))
    #Now send the content of sample.txt to server
    s.send(SendData)
    SendData = file.read(1024)      

# Close the connection from client side
s.close()


