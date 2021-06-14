import socket
import random
from datetime import datetime

max_score = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 4483))
    s.listen(5)
    while True:
        try:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                conn.sendall(str(max_score).encode())  # send the biggest score
                while True:
                    data = conn.recv(128).decode()

                    if not data:
                        break

                    elif int(data) > max_score:
                        max_score = int(data)  # change score
        except:
            s.close()
