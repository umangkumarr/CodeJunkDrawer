#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main(){
	// create scoket
	int network_socket;
	network_socket = socket(AF_INET, SOCK_STREAM, 0);
	
	// specify address for socket
	struct sockaddr_in server_address;
	server_address.sin_family = AF_INET;
	server_address.sin_port = htons(9002);
	server_address.sin_addr.s_addr = INADDR_ANY;
	
	int connection_status = connect(network_socket, (struct sockaddr*)&server_address, sizeof(server_address));

	// check error in connection
	if(connection_status == -1){
		printf("\nError in connection");
	}

	// receive data from server
	char server_response[256];
	recv(network_socket, &server_response, sizeof(server_response), 0);

	//print server response
	printf("\n The server sent: %s", server_response);

	// close socket
	pclose(network_socket);

	return 0;

}
