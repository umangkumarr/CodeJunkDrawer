import socket
import threading

def handle_client(conn, addr):
	print(f'connected to {addr}')
	conn.send(b"Welcome to the server")

	while True:
		data = conn.recv(1024)

		print('client sent data:', data)
		conn.send(data)

		if data == b"End Connection":
			print(f'disconnected from {addr}')
			break


def main():
	host = '127.0.0.1'
	port = 8000

	# server a socket object
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#bind the socket to a host ans port
	server_socket.bind((host, port))

	# listen for client connections
	server_socket.listen()

	print(f"Server listening on {host}:{port}")

	if True:
		#accept a client connection
		conn, addr = server_socket.accept()

		# start a new thread to handle the client request
		client_thread = threading.Thread(target=handle_client, args=(conn, addr))
		client_thread.start()

if __name__ == "__main__":
	main()


