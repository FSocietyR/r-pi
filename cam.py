from socket import *
import os 
def start(name):
	sock = socket()
	flag = True
	sock.connect(('192.168.1.139', 1024))
	if flag:
            try:
                letter = 'start'.encode('utf-8')
                data = sock.sendto(letter, ('192.168.1.139', 1024))
                print('image: {}...Send'.format(name))
            except TimeoutError:
                print('image: {} was not received \n the server closed the connection'.format(name))
            """conn= sock.recv(1024)
            r_data = os.system(conn.decode('utf-8'))
            if r_data == 'finish':
                print('image has been received')"""
            flag = False

