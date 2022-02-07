import paramiko
from paramiko.ssh_exception import BadHostKeyException, AuthenticationException, SSHException
import socket

host = "192.168.0.236"
username = "luigi"
password = "luigi"
port = 22

Bots = []

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

def main():
    Bots.append(Client(host,port,username,password))
    Bots.append(Client(host,port,username,password))
    Bots.append(Client(host,port,username,password))
    Bots.append(Client(host,port,username,password))

    for s in Bots:
        s.send_command("ls")              #Sending commands
        print(" ".join(s.std_out))        #Print from std out from command

if __name__ == "__main__":
    main()