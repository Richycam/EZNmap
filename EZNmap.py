import sys 
import time
import os


class ip_inpt:
    def __init__(self,ip_add):
        self.ip_add = ip_add
    


Banner = """
\|\|\|\|        https://github.com/Richycam        \|\|\|\|
"""

art1 = """
 | |   EZNmap    | |
 | |             | |
 | |  RichyCam   | |
 | |             | |
 | |             | |
"""
art2 = """
 | |   EZNmap    | |
 | |             | |
 | |  RichyCam   | |
 | |             | |
 | | Github.com  | |
"""


def flow_cntrl():
    back = input("\n go back? Y/N? \n ").lower
    if back == "y":
        clear()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def start_nmap():
    for i in range(4):
        clear()
        print(f"starting nmap{'.' * i}")
        time.sleep(0.5)
def exit():
    sys.exit

def get_ip():
    ip_inpt.ip_add = input("Ip address or URL? \n")

def menu():
    print(""" 
     ___________   _   __                    
   / ____/__  /  / | / /___ ___  ____ _____ 
  / __/    / /  /  |/ / __ `__ \/ __ `/ __  |
 / /___   / /__/ /|  / / / / / / /_/ / /_/ /
/_____/  /____/_/ |_/_/ /_/ /_/\__,_/ .___/ 
                                   /_/                   
    ------------------------------------------------
    scan type?
    1) Simple scan
    2) Version Detctor
    3) Vulnrability Scan
    4) Stealth Scan
    5) Scan for all hosts on subnet
    7) start a listener port (expermintal)
    8) Other tools (expermintal)
    ------------------------------------------------
    """)


def opt_1():
    clear()
    start_nmap()
    get_ip()
    simple_cmd = "nmap {0}".format(ip_inpt.ip_add)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    flow_cntrl()
    clear()

def opt_2(): 
    clear()
    start_nmap()
    get_ip()
    simple_cmd = "nmap {0} -A".format(ip_inpt.ip_add)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    flow_cntrl
    clear()
def opt_3():
    clear()
    start_nmap()
    get_ip()
    simple_cmd = "nmap {0} -A".format(ip_inpt.ip_add)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    flow_cntrl()
    clear()
def opt_4():
    clear()
    start_nmap()
    get_ip()
    simple_cmd = "nmap {0} -A --script=vuln ".format(ip_inpt.ip_add)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    flow_cntrl()
    clear()
def opt_5():
    start_nmap()
    get_ip()
    simple_cmd = "sudo nmap {0} -sS ".format(ip_inpt.ip_add)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    flow_cntrl()
    clear()
def opt_6():
    start_nmap()
    get_ip()
    simple_cmd = "nmap {0}/24 -n -sP ".format(ip_inpt.ip_add)  
    output_simple = os.system(simple_cmd)
    print(output_simple)
    flow_cntrl()
    clear()
   
def opt_7():
    clear()
    get_ip()
    port = input("port to run listner on? \n") 
    cmd_nc = "nc -lvnp {0} {1}".format(ip_inpt.ip_add,port)
    clear()
    cmd_nc1 = os.system(cmd_nc)
    print(cmd_nc1)
    flow_cntrl()
    clear()
def opt_8():
    print("1) start Metasploit")
    print("2) run a web crawler")
    tools = input("Choose tool \n EZNMAP> ")
    clear()
    if tools == "1":
        clear()
        os.system("msfconsole")
    elif tools == "2":
        clear()
        get_ip()
        wordlist = input("Wordlist file location? \n EZNMAP> ")
        word_list_cmd = "dirb {0} {1}".format(ip_inpt.ip_add,wordlist)
        os.system(word_list_cmd)
    else: 
        flow_cntrl()
        clear()

list = [art1, art2,]
for art in list:
    print(art)
    time.sleep(0.7)
    clear()

def main():
    
    menu()
    choose = input("EZNMAP> ")
    match choose:
        case "1":
            opt_1()
        case "2":
            opt_2()
        case "3":
            opt_3()
        case "4":
            opt_4()
        case "5":
            opt_5()
        case "6":
            opt_6()
        case "7":
            opt_7()
        case "8":
            opt_8()


runtime_loop = True
while runtime_loop:
    print(Banner)
    main()
