#!/usr/bin/env python3


# file encoding 
# -*- coding: utf-8 -*-

"""

Date: 6/1/2025

Author: E. Gomez

Title: Ping Sweeper Script

Description: This script is a ping sweeper application. It will prompt the user for an IPv4 address and a subnet. Then it will ping each IPv4 address
once within the specified subnet and report if the host is up (responsive) or not. I plan to flush it out further as I would like to add the functionality
to use custom IPv4 addresses and subnets. Currently I've only coded for default class a, b, and c subnets...



NOTES:

Although the code is my own I did reference ChatGPT for advice and google searches whenever I got stuck and couldn't figure things out...

ARIN non-routable IPv4 addresses:
Source: https://www.arin.net/reference/research/statistics/address_filters/
Class A = 10.0.0.0 - 10.255.255.255  or /8  
Class B = 172.16.0.0 - 172.31.255.255 or /12  
Class C = 192.168.0.0 - 192.168.255.255 or /16 

"""

import subprocess
import platform


# main function
def main():
    print("Welcome to my Ping Sweeper Script")

    system = platform.system()
    print(f"The system's OS is {system}")

    prompt = input("Do you want to scan a default private IPv4 Class address or a custom private IPv4 Class address? (default/custom): ").lower()

    if prompt == 'default':
        if system == 'Windows' or system == 'Linux':
            scan_default(system)
        else:
            print("Unsupported OS.")
    elif prompt == 'custom':
        print("Custom scanning not yet implemented.")
    else:
        print("Invalid input. Please enter 'default' or 'custom'.")


# functions 
def scan_default(system):
    select_class = input("Please select whether you would like to scan a Class A, Class B, or Class C default IPv4 range (a/b/c): ").lower()

    if select_class == 'a':
        base = '10'
        for i in range(0, 255):
            for j in range(0, 255):
                for k in range(1, 255):
                    ip = f"{base}.{i}.{j}.{k}"
                    ping_and_report(ip, system)

    elif select_class == 'b':
        base = '172'
        for i in range(16, 32):
            for j in range(0, 255):
                for k in range(1, 255):
                    ip = f"{base}.{i}.{j}.{k}"
                    ping_and_report(ip, system)

    elif select_class == 'c':
        base = '192.168'
        for i in range(0, 255):
            for j in range(1, 255):
                ip = f"{base}.{i}.{j}"
                ping_and_report(ip, system)

    else:
        print("Invalid class selection.")


def ping_and_report(ip, system):
    if system == 'Linux':
        cmd = ['ping', '-c', '1', ip]
    elif system == 'Windows':
        cmd = ['ping', '-n', '1', ip]
    else:
        print(f"Unsupported OS for pinging: {system}")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if "1 received" in result.stdout or "1 packets received" in result.stdout or "bytes=32" in result.stdout:
        print(f"{ip} is up")
    else:
        print(f"{ip} is unreachable")


if __name__ == "__main__":
    main()

