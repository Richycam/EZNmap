import sys
import time
import os
import socket

# //     NOTICE  Update: 1.1 added experimental features   
# //     NOTICE  Added : net socket sending, listener, and other tools
# //     NOTICE  Requirements for other tools : Metasploit-framework, dirb, 

# //     TODO    Add more features ideally built into Python not from cmd line
# //     TODO    a way to check if the user has dependencies?
# //     TODO    make code look neater maybe?  

Banner = """
############                EZNmap                     ############
############           --for lazy hackers--            ############
############        https://github.com/Richycam        ############
"""

art1 = """
 ___________________
 | _______________ |
 | |  EZNmap 1.1 | |
 | |             | |
 | |x           x| |
 | |             | |
 | |             | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []| 
L___________________J 

"""
art2 = """
 ___________________
 | _______________ |
 | |  EZNmap 1.1 | |
 | |             | |
 | |X  X     X  X| |
 | |             | |
 | |             | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []| 
L___________________J 

"""

art3 = """
 ___________________
 | _______________ |
 | |  EZNmap 1.1 | |
 | |             | |
 | |  RichyCam   | |
 | |             | |
 | |             | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []| 
L___________________J 

"""

art4 = """
 ___________________
 | _______________ |
 | |  EZNmap 1.1 | |
 | |             | |
 | |  RichyCam   | |
 | |             | |
 | | Github.com  | |
 |_________________|
     _[_______]_
 ___[___________]___
|         [_____] []|
|         [_____] []|
L___________________J    
"""

def clear():
    os.system("clear")

def start_nmap():
    for i in range(4):
        clear()
        print(f"starting nmap{'.' * i}")
        time.sleep(0.5)

def exit():
    sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sock_connect(host, port): 
    sock.connect((host, int(port)))
    time.sleep(3)

clear()
time.sleep(1)
for art in [art1, art2, art3, art4]:
    print(art)
    time.sleep(1)
    clear()
print(Banner)

ip = input("IP Address to scan? \n")
clear()
print("scan type?")
print("1) Simple scan")
print("2) Version Detector")
print("3) Vulnerability Scan")
print("4) Stealth Scan")
print("5) Scan for all hosts on subnet")
print("6) Send a net socket (experimental)")
print("7) Start a listener port (experimental)")
print("8) Other tools (experimental, Linux only)")

choose = input("Choose scan type \n")

match choose:
    case "1":
        start_nmap()
        simple_cmd = f"nmap {ip}"   
        output_simple = os.system(simple_cmd)
        print(output_simple)
        exit()
    case "2":
        start_nmap()
        simple_cmd = f"nmap {ip} -A"
        output_simple = os.system(simple_cmd)
        print(output_simple)
        exit()
    case "3":
        start_nmap()
        simple_cmd = f"nmap {ip} -A --script=vuln"
        output_simple = os.system(simple_cmd)
        print(output_simple)
        exit()
    case "4":
        start_nmap()
        simple_cmd = f"sudo nmap {ip} -sS"
        output_simple = os.system(simple_cmd)
        print(output_simple)
        exit()
    case "5":
        start_nmap()
        simple_cmd = f"nmap {ip}/24 -n -sP"
        output_simple = os.system(simple_cmd)
        print(output_simple)
        exit()
    case "6":
        clear()
        port = input("What port? \n")
        sock_connect(ip, port)
    case "7":
        clear()
        port = input("Port to run listener on? \n")
        cmd_nc = f"nc -lvnp {ip} {port}"
        clear()
        cmd_nc1 = os.system(cmd_nc)
        print(cmd_nc1)
    case "8":
        print("1) Start Metasploit")
        print("2) Run a web crawler")
        tools = input("Choose tool \n")
        clear()    
        if tools == "1":
            clear()
            os.system("msfconsole")
        elif tools == "2":
            clear()
            wordlist = input("Wordlist file location? \n")
            word_list_cmd = f"dirb {ip} {wordlist}"
            os.system(word_list_cmd)
