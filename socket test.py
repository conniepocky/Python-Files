#socket test may not work use this is the link to a tutorial
#https://www.youtube.com/watch?v=wzrGwor2veQ
#Program
import socket
#connects
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
#who we are communicating with
server = "pythonprogramming.net"
port = 80
request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
s.connect((server,port))
s.send(request.encode())
result = s.recv(4096)
print(result)
