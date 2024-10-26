import sys 
import time
import os

Banner = """
############                EZNmap                     ############
############           --for lazy hackers--            ############
############        https://github.com/Richycam        ############
"""
art1 = """
 | |   EZNmap    | |
 | |             | |
 | |x           x| |
 | |             | |
 | |             | |
"""
art2 = """
 | |   EZNmap    | |
 | |             | |
 | |X  X     X  X| |
 | |             | |
 | |             | |
"""

art3 = """
 | |   EZNmap    | |
 | |             | |
 | |  RichyCam   | |
 | |             | |
 | |             | |
"""
art4 = """
 | |  EZNmap 1.1 | |
 | |             | |
 | |  RichyCam   | |
 | |             | |
 | | Github.com  | |
"""
def clear():
    os.system("clear")
def start_nmap():
    for i in range(4):
        clear()
        print(f"starting nmap{'.' * i}")
        time.sleep(0.5)
def exit():
    sys.exit




def menu():
    print(""" 
                    EZNmap                      
    ------------------------------------------------
    scan type?
    1) Simple scan
    2) Version Detctor
    3) Vulnrability Scan
    4) Stealth Scan
    5) Scan for all hosts on subnet
    7) start a listener port (expermintal)
    8) Other tools (expermintal )
    ------------------------------------------------
    """)



def opt_1():
    clear()
    start_nmap()
    simple_cmd = "nmap {0}".format(ip)
    output_simple = os.system(simple_cmd)
    print(output_simple)



def opt_2(): 
    clear()
    start_nmap()
    simple_cmd = "nmap {0} -A".format(ip)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    
def opt_3():
    clear()
    start_nmap()
    simple_cmd = "nmap {0} -A".format(ip)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    
def opt_4():
    clear()
    start_nmap()
    simple_cmd = "nmap {0} -A --script=vuln ".format(ip)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    
def opt_5():
    start_nmap()
    simple_cmd = "sudo nmap {0} -sS ".format(ip)
    output_simple = os.system(simple_cmd)
    print(output_simple)
    
def opt_6():
    start_nmap()
    simple_cmd = "nmap {0}/24 -n -sP ".format(ip)  
    output_simple = os.system(simple_cmd)
    print(output_simple)

   
def opt_7():
    clear()
    port = input("port to run listner on? \n") 
    cmd_nc = "nc -lvnp {0} {1}".format(ip,port)
    clear()
    cmd_nc1 = os.system(cmd_nc)
    print(cmd_nc1)
    
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
        wordlist = input("Wordlist file location? \n EZNMAP> ")
        word_list_cmd = "dirb {0} {1}".format(ip,wordlist)
        os.system(word_list_cmd)


list = [art1, art2, art3, art4]
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
