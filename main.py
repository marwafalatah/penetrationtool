import sys

from ARP_spoof_detector import spoof_detector
from ArpSpoof import spoof
from DownloadData import download_data
from Keylogger import key_logging
from LoginPassword import login_password
from NetworkScanner import scan, print_result
from PostRequest import post_request
from ReadWriteFile import read_write
from getMac import get_mac
from sniffing import sniff

_username = ''
_password = ''
iface = "eht0"

'''
    This method show the user Menu about application
'''


def Menu():
    print("\n\n\t1.Port Scanning        \t6.Login password")
    print("\t2.Network Scanning     \t7.Read/Write files")
    print("\t3.ARP Spoofing         \t8.Send post request")
    print("\t4.Sniffing             \t9. ARP spoof detector")
    print("\t5.Keylogger            \t10. Download Data")
    print("\t11.exit")
    print("\t******************************************")


'''
    This method call the relative option selected by user:
'''


def menu_cases(c):
    global iface
    global _username
    global _password
    if c == 1:
        try:
            mac = get_mac(input('Enter IP address: '))
        except IndexError:
            print("Does't find any Mac address")
        else:
            print("Mac address = ", mac)
    elif c == 2:
        scan_result = scan(input('Enter Subnet address: '))
        print_result(scan_result)
    elif c == 3:
        spoof(input('Enter Victim IP address: '), input('Enter Source IP address: '))
    elif c == 4:
        sniff("eth0")
    elif c == 5:
        key_logging()
    elif c == 6:
        _username, _password = login_password(_username, _password)
    elif c == 7:
        read_write()
    elif c == 8:
        try:
            post_request(_username, _password)
        except ConnectionError:
            print("service is not running")
        except:
            print("service is not running")
    elif c == 9:
        spoof_detector("eth0")
    elif c == 10:
        id = int(input("Enter the postID between 0-499 you want to download : "))
        download_data(str(id))
    elif c == 11:
        sys.exit()

    print("\n\n\n")
    Menu()
    z = int(input('Enter Your Choice: '))
    menu_cases(z)
    # 1: get_mac(input('Enter IP address: ')),
    # 2: scan_network(input('Enter subnet address: ')),
    # 3: ARP_Spoof(input('Enter victim and source IP address: ')),
    # 4: network_sniff(input('Enter .....: ')),
    # 5: Bypassing(input('Enter : ')),
    # 6: Keylogger(input('Enter :')),
    # 7: Login_password(input('Enter :')),
    # 8: Read_Write_files(input('Enter :')),
    # 9: Download_files(input('Enter :')),
    # 10: Send_post_request(input('Enter :')),
    # 11: ARP_spoof_detdctor(input('Enter :')),
    # 12: Exit(input('Enter :')),
    # default: print('invalid choice')
    pass


# define 11 functions including:


# while True:
#     if input('Enter Username: ') != _username or input('Enter password: ') != _password:
#         print("Wrong username or password")
#     else:
#         break


def main():
    global iface
    print('\t\t****************************')
    print('\t\tWelcome to Pen '
          'Testing Tools')
    print('\t\t****************************')
    print('\n\t\tDefault interface is set to eth0\n')
    choise = input("Do you want to change the interface? [y/n]").lower()
    if choise == 'y':
        iface = input("\n\nEnter new Interface Name:")

    Menu()
    z = int(input('Enter Your Choice: '))
    menu_cases(z)


if __name__ == "__main__":
    print("-------------Please Login to continue using Penetrating Tool--------------\n")
    _username = input("Enter username =")
    _password = input("Enter password =")
    print("successfully login ")
    main()
