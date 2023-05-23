#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>

int main() {
    char server_message[256] = "You have reached the Umang's server";
    // create socket
    int server_socket;
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    // define server address;
    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(64000);
    server_address.sin_addr.s_addr = INADDR_ANY;
    // bind socket with ip and port
    bind(server_socket, (struct sockaddr*)&server_address,
         sizeof(server_address));
    listen(server_socket, 5);
    int client_socket;
    client_socket = accept(server_socket, NULL, NULL);
    // send message
    send(client_socket, server_message, sizeof(server_message), 0);
    // close socket
    pclose(server_socket);
    return 0;
}
