#create client for ssh connection with paramiko. destination is metasploitable2 
from sys import stdin, stdout, stderr, exception
import paramiko

ssh =  paramiko.SSHClient() #client nesnesi olusturduk
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#host ip not found in known_host hata almamak icin ustteki set edildi

#metasloitable2 bilgileri
ip = "192.168.8.103" 
port = 22
username ="msfadmin"
password = "msfadmin"

#metada command calistirmak
def sendCommand(command):
    stdin,stdout,stderr= ssh.exec_command(command)
    cmd_output=(stdout.read())
    print(f">>{cmd_output.decode()}")
    
#hata kontrol
try:
    print("Connecting...")
    ssh.connect(ip, port=port, username=username, password=password, timeout=3)
    print("Connection Successful!")
except paramiko.AuthenticationException:
    print("Authentication failed, please verify your credentials")
except paramiko.SSHException as sshException:
    print(f"Unable to establish SSH connection: {sshException}")
except paramiko.BadHostKeyException as badHostKeyException:
    print(f"Unable to verify server's host key: {badHostKeyException}")
except Exception as e:
    print(f"Exception occurred: {e}")


#stdind stderr stdout olarak 3 ciktisi vardir exec command icin
command = ""
while command.lower().strip() !='quit':
    if command != "":
        sendCommand(command)
    command=input(">>")