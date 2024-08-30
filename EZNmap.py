import sys 
import time
import os

Banner = """
############                EZNmap                     ############
############           --for lazy hackers--            ############
############        https://github.com/Richycam        ############
"""

def clear():
    os.system("clear")


def start_nmap():
    clear()
    print("Starting Nmap")
    time.sleep(0.5)
    clear()
    print("Starting Nmap.")
    time.sleep(0.5)
    clear()
    print("Starting Nmap..")
    time.sleep(0.5)
    clear()
    print("Starting Nmap...")
    time.sleep(0.5)

def exit():
    sys.exit


print(Banner)

ip = input("IP Address to scan? \n")

clear()
print("scan type?")
print("1) Simple scan")
print("2) Version Detctor")
print("3) Vulnrabillity Scan")
print("4) Stealth Scan")
choose = input("Choose scan type \n")
if choose == "1":
    start_nmap()
    simple_cmd = "nmap {0} ".format(ip)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    exit()
if choose == "2":
    start_nmap()
    simple_cmd = "nmap {0} -A".format(ip)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    exit()
if choose == "3":
    start_nmap()
    simple_cmd = "nmap {0} -A --script=vuln ".format(ip)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    exit()
if choose == "4":
    start_nmap()
    simple_cmd = "nmap {0} -sS ".format(ip)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    exit()


