import scapy.all as scapy


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc  # return mac address of given IP address


if __name__ == "__main__":
    try:
        mac = get_mac("192.168.43.170")
    except IndexError:
        print("Does't find any Mac address")
    else:
        print("Mac address = ", mac)
