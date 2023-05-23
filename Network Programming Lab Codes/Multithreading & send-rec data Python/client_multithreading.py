import socket

#create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the server
host = '127.0.0.1'
port = 8000
client_socket.connect((host, port))

#recieve the welcome message from the server
data = client_socket.recv(1024)
print(data.decode())

while True:
	#get the user input to send to the server
	message = input("Enter Message: ")

	#send the message to the server
	client_socket.send(message.encode())

	#receive data from the server
	data = client_socket.recv(1024)
	print(f"Received from the server: {data.decode()}")

	if message == "End Connection":
		break


# close the connection
client_socket.close()