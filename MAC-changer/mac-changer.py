import subprocess as sb
import optparse
import re


def mac_changer(interface, new_mac):
    sb.call(["ifconfig", interface, "down"])
    sb.call(["ifconfig", interface, "hw", "ether", new_mac])
    sb.call(["ifconfig", interface, "up"])


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change the mac address")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help="add new mac address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error(
            "[-] Specify an Interface use python macchanger --help for more details")
    elif not options.new_mac:
        parser.error(
            "[-] Specify an MacAddr use python macchanger --help for more details")

    return options


def current_mac(interface):
    ifconfig_result = sb.check_output(["ifconfig", interface])
    return re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result)).group(0)


options = get_argument()
mac_changer(options.interface, options.new_mac)
print(
    f"[+] Changing Mac Address of Interface {options.interface} to {options.new_mac}")
final_mac = current_mac(options.interface)
print(
    f"[+] MAC-address successfully chaged to {options.new_mac}" if options.new_mac == final_mac else "Error Occured Fix It")
