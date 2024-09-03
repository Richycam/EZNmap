import sys 
import time
import os
import socket


#//     NOTICE  Update: 1.1 added expermintal features   
#//     NOTICE  Added : net socket sending, listener and other tools
#//     NOTICE  Requirements for other tools : Metasploit-framework, dirb, 

#//     TODO    Add more features ideally bulit into python not from cmd line
#//     TODO    a way to check if the user has dependanices ?
#//     TODO    make code look more neat maybe?  



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
    clear()
    print("starting nmap")
    time.sleep(0.5)
    clear()
    print("starting nmap.")
    time.sleep(0.5)
    clear()
    print("starting nmap..")
    time.sleep(0.5)
    clear()
    print("starting nmap...")
    time.sleep(0.5)

def exit():
    sys.exit

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def sock_connect(): 
    sock
    time.sleep(3)
    call
clear()
time.sleep(1)
print(art1)
time.sleep(1)
clear()
print(art2)
time.sleep(1)
clear()
print(art3)
time.sleep(1)
clear()
print(art4)
time.sleep(2)
clear()
print(Banner)
ip = input("IP Address to scan? \n")
clear()
print("scan type?")
print("1) Simple scan")
print("2) Version Detctor")
print("3) Vulnrabillity Scan")
print("4) Stealth Scan")
print("5) Scan for all hosts on subnet")
print("6) send a net socket (expermintal)")
print("7) start a listener port (expermintal)")
print("8) Other tools (expermintal (Linux only) ")
choose = input("Choose scan type \n")
if choose == "1":
    start_nmap()
    simple_cmd = "nmap {0}".format(ip)   
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
    simple_cmd = "sudo nmap {0} -sS ".format(ip)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    exit()
if choose == "5":
    start_nmap()
    simple_cmd = "nmap {0}/24 -n -sP ".format(ip)  
    output_simple = os.system(simple_cmd)
    print(output_simple)
    exit()
if choose == "6":
    clear()   
    host = ip
    port = input("what port? \n")
    call = sock.connect((host,port))
    sock_connect()
if choose == "7":
    clear()
    port =input("port to run listner on? \n")
    cmd_nc = "nc -lvnp {0} {1}".format(ip,port)
    clear()
    cmd_nc1 = os.system(cmd_nc)
    print(cmd_nc1)
if choose == "8":
    print("1) start Metasploit")
    print("2) run a web crawler")
    tools = input("Choose tool \n")
    clear()    
    if tools == "1":
        clear()
        os.system("msfconsole")
    if tools == "2":
        clear()
        wordlist = input("Wordlist file location? \n")
        word_list_cmd = "dirb {0} {1}".format(ip,wordlist)
        os.system(word_list_cmd)



