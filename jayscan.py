import socket                                    #Help Us to Connect to the webpage and get the reports
from IPy import IP                               #Converter web url in to ip

def check_ip(ip):                                #Converter web url in to ip
    try:
        IP(ip)
        return(ip)
    except ValueError:                           # It (h)elp Us To Store The Address and Help To Convert The link To Ip
        return socket.gethostbyname(ip)

def scan_port(ipaddress, port):
    try:
        jay = socket.socket()
        jay.settimeout(0.5)                      #Main Line It Help To Speedup The Time Of Scan But It Reduce The Accurace
        jay.connect((ipaddress, port))
        print('[+] Port' + str(port) + ' is Open')
    except:
        print('[+] Port' + str(port) + ' Is Closed')


ipaddress = input('[+] Enter Target To Scan: ')
converted_ip = check_ip(ipaddress)               # Convert The address to the ip

for port in range(75, 85):                       # Range Of the Port to scan
    scan_port(converted_ip, port)                # Converted address to ip command
