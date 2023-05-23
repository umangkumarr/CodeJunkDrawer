#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main()
{
    int network_socket;
    network_socket=socket(AF_INET,SOCK_STREAM,0);
    struct sockaddr_in server_address;
    server_address.sin_family=AF_INET;
    server_address.sin_port=htons(64000);
    server_address.sin_addr.s_addr=INADDR_ANY;
    int connection_status=connect(network_socket,(struct sockaddr*)&server_address,sizeof(server_address));
    //check error in connection
    if(connection_status==-1)
    {
        printf("\n Error in connection");
    }
    //receive data from server
    char server_response[256];
    recv(network_socket,&server_response,sizeof(server_response),0);

    //print server respons
    printf("\n The server sent : %s",server_response);

    //close socket
    close(network_socket);
    return 0;
}
