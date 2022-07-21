import socket
#for communication
TCP_IP= '127.0.0.1'
TCP_PORT=6969 #change this value

def send_to(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    message = bytes(message, 'utf-8')
    s.send(message)
    s.close()
