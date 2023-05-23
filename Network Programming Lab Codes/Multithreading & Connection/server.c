#include <arpa/inet.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

// the function for handling client in multithreading
void *todo_client(void *);

int main() {
    int socket_server, socket_client, sizeaddr;
    struct sockaddr_in server_addr, client_addr;

    // socket creation
    socket_server = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_server == -1) {
        printf("Socket could not be created");
    }
    puts("Socket created");

    // fill the sockaddr_in structure
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(8888);

    // bind the server socket
    if (bind(socket_server, (struct sockaddr *)&server_addr,
             sizeof(server_addr)) < 0) {
        // print the error meassage
        perror("Bind failed, Error");
        return 1;
    }
    puts("binding has been completed");

    // listen
    listen(socket_server, 3);

    // accept the incoming connection
    puts("waiting for incoming coinnection..");
    sizeaddr = sizeof(struct sockaddr_in);

    pthread_t thread_id;

    while (
        (socket_client = accept(socket_server, (struct sockaddr *)&client_addr,
                                (socklen_t *)&sizeaddr))) {
        puts("Connection accepted");

        if (pthread_create(&thread_id, NULL, todo_client,
                           (void *)&socket_client) < 0) {
            perror("thread could not be created");
            return 1;
        }

        // now join the thread
        pthread_join(thread_id, NULL);
        puts("handler assigned");
    }

    if (socket_client < 0) {
        perror("Accept failed");
        return 1;
    }

    return 0;
}

// the definition of function for handling client in multithreading

void *todo_client(void *socket_descriptor) {
    // get the socket descriptor
    int socket_desc = *(int *)socket_descriptor;
    int read_size;
    char *message, client_message[2000];

    // send seome message to the client
    message = "Greetings! I am your connection handler\n";
    write(socket_desc, message, strlen(message));

    message = "type message\n";
    write(socket_desc, message, strlen(message));

    // receive a message from client
    while ((read_size = recv(socket_desc, client_message, 200, 0)) > 0) {
        // end of string marker
        client_message[read_size] = '\0';

        // send the message back to client
        write(socket_desc, client_message, strlen(client_message));

        // clear the message buffer
        memset(client_message, 0, 200);
    }

    if (read_size == 0) {
        puts("Client disconnected");
        fflush(stdout);
    } else if (read_size == -1) {
        perror("recv failed");
    }

    return 0;
}
