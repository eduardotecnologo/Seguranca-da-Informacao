#!/usr/bin/python3
#Fazer arping de conexao

import sys
from datetime import datetime
from scapy.all import *

try:
    interface = input ("\n[*] Set interface: ")
    ips = input("[*] Set IP RANGE or Network: ")
except KeyboardInterrupt:
    print("\n user aborted")
    sys.exit()

print("Scanning...")
start_time = datetime.now()

conf.verb = 0

ans,unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2, iface = interface ,inter= 0.1)

print("\n\tMAC\t\tIP\n")

for snd,rcv in ans:
    print(rcv.sprintf("%Ether.src% - %ARP.psrc%"))

stop_time = datetime.now()
total_time = stop_time - start_time
print("\n[*] Scan Completed")
print("[*] Scan Duration: %s" %(total_time))









