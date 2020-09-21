from socket import *
import os 
def start():
	sock = socket()
	flag = True
	sock.connect(('192.168.1.139', 1024))
	if flag:
            try:
                letter = 'start'.encode('utf-8')
                data = sock.sendto(letter, ('192.168.1.139', 1024))
            except TimeoutError:
                while not True:
                    letter = 'start'.encode('utf-8')
                    data = sock.sendto(letter, ('192.168.1.139', 1024))
            """conn= sock.recv(1024)
            r_data = os.system(conn.decode('utf-8'))
            if r_data == 'finish':
                print('image has been received')"""
            flag = False
