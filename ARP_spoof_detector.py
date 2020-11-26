import scapy.all as scapy

from getMac import get_mac


def spoof_detector(interface):
    packet = scapy.ARP(op=2, pdst="10.0.2.1", hwdst="28:56:5a:90:4d:f5", psrc="10.0.2.7")
    scapy.sniff(iface=interface, store=False,
                prn=process_sniffed_packet(packet))  # sniffing the packets on given Iface


'''
    this method track the change on victim ARP and change ARP
'''


def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc

            if real_mac != response_mac:
                print("[+] You are under attack!!")
        except IndexError:
            pass


if __name__ == "__main__":
    spoof_detector("eth0")
