import socket

sock = socket.socket()

sock.bind(('', 5656))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1111)
    conn.send(b"HTTP/1.1 \r\n")
    conn.send(b"Server: simplehttp\r\n\r\n")
    conn.send(addr[0].encode("utf-8"))
    conn.close()
