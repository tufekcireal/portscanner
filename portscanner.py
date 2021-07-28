#!/usr/bin/env python3
# Coder By TufekciReal
# 
#############################
# Gereksinimler:
# apt install python3-pip
# pip3 install IPy
import socket
from IPy import IP
print("""
     ############################    
    #         TUFEKCİREAL       #
    #          ^port tarama^   #
    ###########################
      """)

def scan(target):
    converted_ip = check_host(target)
    print('\n' + '[*] Bir Dakika... Portlar Taranıyor...]: ' + str(target))
    for port in range(1,500):    
        scan_ports(converted_ip, port)

def check_host(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_ports(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))

        try:
            banner = get_banner(sock)
            print ('[+] AÇIK PORT: ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print ('[+] AÇIK PORT: ' + str(port))
    except:
        pass

if __name__ == "__main__":
    targets = input('[+] Taranacak hedefi girin:  ')
    if ',' in targets:
        for ip_address in targets.split(','):
            scan(ip_address.strip(' '))
    else:
        scan(targets)

