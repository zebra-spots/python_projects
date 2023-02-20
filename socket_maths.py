#! /usr/bin/python

from socket import *

# Create a socket connection, read what is recieved, action it and then send it back to the server
# Define server IP address and TCP port
HOST = '10.16.0.250' # Change this
PORT = 9092 # Change this

# Create TCP socket handle
s = socket(AF_INET, SOCK_STREAM)

# Connect to server
s.connect((HOST, PORT))

# Print returned message
print(s.recv(1024))


def calc(s):
    if '+' in s:
        y = s.split('+')
        x = int(y[0])+int(y[1])

    elif '-' in s:
        y = s.split('-')
        x = int(y[0])-int(y[1])

    elif '*' in s:
        y = s.split('*')
        x = int(y[0])*int(y[1])

    elif '/' in s:
        y = s.split('/')
        x = int(y[0])/int(y[1])

    return x


ans = bytes(calc(s), 'utf-8')

# Write the bites back to the server
s.send(ans)

# Collect the flag
flag = s.recv(1024)

# Print the flag
print("Flag returned: %s" % (flag))

# Close the socket connection
s.close()
