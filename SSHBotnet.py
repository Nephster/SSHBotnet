import paramiko
from paramiko.ssh_exception import BadHostKeyException, AuthenticationException, SSHException
import socket
import ipaddress
import validators
from getpass import getpass

host = "192.168.0.236"
username = "luigi"
password = "luigi"
port = 22

Botnet = []

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} is valid. The object returned is {}".format(address, ip))
        return ip
    except ValueError:
        print("IP address {} is not valid".format(address))
        return 0

class Client:
    def __init__(self,addr,port,username,passw):
        self.addr = addr
        self.port = port
        self.username=username
        self.passw = passw
        self.session = self.connect()
    def connect(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.addr, self.port, self.username, self.passw)
            #ssh.exec_command("ls")
            return ssh
        except (BadHostKeyException, AuthenticationException, SSHException, socket.error) as e:
            print (e)
    def send_command(self, command):
        #print(command)
        stdin, stdout, stderr = self.session.exec_command(command)
        self.std_out = stdout.readlines()
        self.std_err = stderr.readlines()
        #print(self.lines)

def invalid():
   print ("INVALID CHOICE!")

def my_quit_fn():
   raise SystemExit

def add_bot():
    hostname = input("Add a SSH ipaddr or domainname: ")
    if validate_ip_address(hostname) or validators.domain(hostname):
        print()
        #Botnet.append(bot)
    else:
        print("Wrong IP address or domain name")
    username = input("Set username credential: ")
    if not username:
        print("No username set")
    passw = getpass("Set password credential: ")
    print("Connecting...")
    if Client(hostname,port,username,passw):
        print("Connected")
        Botnet.append(Client(hostname,port,username,passw))
    else:
        print("Couldnt connect")

def list_bot():
    if not Botnet:
        print("No bot in the list")
    else:
        for bot in Botnet:
            print(bot.addr,bot.username)
def send_command():
    cmd = input(">")
    for s in Botnet:
        s.send_command(cmd)              #Sending commands
        print("".join(s.std_out))        #Print from std out from command
        print("\n")
def main():
    ans=True
    while ans:
        print("""
        1.Add bot to my list
        2.List of bots in the botnet
        3.Send command to all bots and see output
        4.Exit/Quit
        """)
        ans= input("What would you like to do? ") 
        if ans=="1": 
            add_bot() 
        elif ans=="2":
            list_bot()
        elif ans=="3":
            print("\n Send command")
            send_command()
        elif ans=="4":
            print("\n Goodbye")
            my_quit_fn() 
        elif ans !="":
            invalid()

    """
    Bots.append(Client(host,port,username,password))
    Bots.append(Client(host,port,username,password))
    Bots.append(Client(host,port,username,password))
    Bots.append(Client(host,port,username,password))

    
    for s in Bots:
        s.send_command("ls")              #Sending commands
        print(" ".join(s.std_out))        #Print from std out from command
    """

if __name__ == "__main__":
    main()