import socket

host = '127.0.0.1'
port= 50001

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

message=input(">>")

while message.lower().strip()!="quit":
    if(message!=""): #mesaj bos degilse
        client_socket.send(message.encode()) #mesaji bite array olarak gonderebilir
        data=client_socket.recv(1024).decode()#gelen bite array mesaji stringe cevirir
        print("response from server:"+str(data))
        message = input(">>")
client_socket.close()