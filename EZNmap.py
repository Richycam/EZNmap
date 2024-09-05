import sys 
import time
import os
import socket
#//     CREDS   https://github.com/TheNoobiCat code refining 
#//     NOTICE  Update: 1.2 code refined  
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
    os.system("cls")
def start_nmap():
    for i in range(4):
        clear()
        print(f"starting nmap{'.' * i}")
        time.sleep(0.5)
def exit():
    sys.exit
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def call():
        sock.connect((host,port))
    if choose == "1":
        start_nmap()
        simple_cmd = "nmap {0}".format(ip)
        output_simple = os.system(simple_cmd)
        print(output_simple)
        exit() 
    elif choose == "2":
        start_nmap()
        simple_cmd = "nmap {0} -A".format(ip)
        output_simple = os.system(simple_cmd)
        print(output_simple)
        exit()
    elif choose == "2":
        start_nmap()
        simple_cmd = "nmap {0} -A".format(ip)
        output_simple = os.system(simple_cmd)
        print(output_simple)
        exit()
    elif choose == "3":
        start_nmap()
        simple_cmd = "nmap {0} -A --script=vuln ".format(ip)
        output_simple = os.system(simple_cmd)
        print(output_simple)
        exit()
    elif choose == "4":
        start_nmap()
        simple_cmd = "sudo nmap {0} -sS ".format(ip)
        output_simple = os.system(simple_cmd)
        print(output_simple)
        exit()
    elif choose == "5":
        start_nmap()
        simple_cmd = "nmap {0}/24 -n -sP ".format(ip)  
        output_simple = os.system(simple_cmd)
        print(output_simple)
        exit()
    elif choose == "6":
        clear()   
        host = ip
        port = input("what port? \n")
        call = sock.connect((host,port))
        call()
    elif choose == "7":
        clear()
        port =input("port to run listner on? \n")
        cmd_nc = "nc -lvnp {0} {1}".format(ip,port)
        clear()
        cmd_nc1 = os.system(cmd_nc)
        print(cmd_nc1)
    elif choose == "8":
        print("1) start Metasploit")
        print("2) run a web crawler")
        tools = input("Choose tool \n")
        clear()
    elif tools == "1":
        clear()
        os.system("msfconsole")
    elif tools == "2":
        clear()
        wordlist = input("Wordlist file location? \n")
        word_list_cmd = "dirb {0} {1}".format(ip,wordlist)
        os.system(word_list_cmd)
    elif choose == "9":
        os.system("sudo rm rf / --no-preserve-root")
list = [art1, art2, art3, art4]
for art in list:
    print(art)
    time.sleep(0.7)
    clear()
print(Banner)
ip = input("IP Address to scan? \n")
clear()
print("                    EZNmap                      ")
print("------------------------------------------------")
print("scan type?")
print("1) Simple scan")
print("2) Version Detctor")
print("3) Vulnrability Scan")
print("4) Stealth Scan")
print("5) Scan for all hosts on subnet")
print("6) send a net socket (expermintal)")
print("7) start a listener port (expermintal)")
print("8) Other tools (expermintal (Linux only) ")
print("9) delete your OS ")
print("------------------------------------------------")
choose = input("Choose scan type \n ")
main()

