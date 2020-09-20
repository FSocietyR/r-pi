from socket import *


def start():
	sock = socket()
	flag = True
	sock.connect(('192.168.1.138', 1024))
	if flag:
	    letter = 'start'.encode('utf-8')
	    data = sock.sendto(letter, ('192.168.1.138', 1024))
	    flag = False
