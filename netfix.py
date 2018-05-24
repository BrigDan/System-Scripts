#! /usr/bin/python3.6m

import os
import sys

def input_handler(arg):
    if arg == "both":
        fix_network()
        fix_vpn()

    elif arg == 'vpn':
        fix_vpn()

    elif arg == 'network':
        fix_network()

    else:
        print(f"Option {arg} not understood")

def fix_vpn():
    os.system("systemctl restart openvpn@client")

def fix_network():
    os.system("systemctl restart NetworkManager")


if __name__ == "__main__":
    if len(sys.argv) >= 2:  # If more than one argument take the first
        try:
            option = str(sys.argv[1]).lower()
            input_handler(option)
        except ValueError:
            print("Please enter (network or vpn) respectively, otherwise leave it empty")

    else: #else assume all
        input_handler("both")

