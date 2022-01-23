import scapy.all as scapy
import argparse


def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="ip_address",
                        help="Specify an IP Address or a range of IP Addres")
    options = parser.parse_args()

    if not options.ip_address:
        parser.error(
            "[-] Specify an IP Address or a range of IP Address --help for more details")
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast,
                              timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_ip_mac(clients_list):
    print("   IP\t\t\t   MAC-address\n-----------------------------------------")
    for element in clients_list:
        print(element["ip"], element["mac"], sep='\t\t')


ip = get_argument()
scan_result = scan(ip.ip_address)
print_ip_mac(scan_result)
