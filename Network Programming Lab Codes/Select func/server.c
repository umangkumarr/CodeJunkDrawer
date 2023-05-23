#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 64000

int main(void)
{
    fd_set master;
    fd_set read_fds;
    struct sockaddr_in serverAddr;
    struct sockaddr_in clientAddr;
    int fdMax;
    int listener;
    int newfd;
    char buf[128];
    int nbytes;
    int allow = 1;
    socklen_t addrlen;
    int i, j;

    FD_ZERO(&master);
    FD_ZERO(&read_fds);

    if ((listener = socket(PF_INET, SOCK_STREAM, 0)) == -1)
    {
        perror("Socket");
        exit(1);
    }

    if (setsockopt(listener, SOL_SOCKET, SO_REUSEADDR, &allow, sizeof(int)) == -1)
    {
        perror("setsockopt");
        exit(1);
    }

    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_port = htons(PORT);
    memset(&(serverAddr.sin_zero), '\0', 8);
    if (bind(listener, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) == -1)
    {
        perror("Bind");
        exit(1);
    }
    printf("\n server is bound at port %d", PORT);
    if (listen(listener, 5) == -1)
    {
        perror("listen");
        exit(1);
    }
    printf("\n server started listening at port %d", PORT);

    FD_SET(listener, &master);

    fdMax = listener;

    while (1)
    {
        read_fds = master;
        if (select(fdMax + 1, &read_fds, NULL, NULL, NULL) == -1)
        {
            perror("Select");
            exit(1);
        }

        for (i = 0; i <= fdMax; i++)
        {
            if (FD_ISSET(i, &read_fds))
            {
                if (i == listener)
                {
                    addrlen = sizeof(clientAddr);
                    if ((newfd = accept(listener, (struct sockaddr *)&clientAddr, &addrlen)) == -1)
                    {
                        perror("accept");
                    }
                    else
                    {
                        FD_SET(newfd, &master);
                        if (newfd > fdMax)
                        {
                            fdMax = newfd;
                        }
                        printf("\n server select : new connection from %s on socket %d\n", inet_ntoa(clientAddr.sin_addr), newfd);
                        char welcome[50] = "Welcome from server Mohit kumar\n";
                        send(fdMax, welcome, sizeof(welcome), 0);
                    }
                }
                else
                {
                    memset(buf, 0, sizeof(buf));
                    if ((nbytes = recv(i, buf, sizeof(buf), 0)) <= 0)
                    {
                        if (nbytes == 0)
                        {
                            printf("\n select server : socket %d hung up \n", i);
                        }
                        else
                        {
                            perror("recv");
                        }
                        close(i);
                        FD_CLR(i, &master);
                    }
                    else
                    {
                        for (j = 0; j <= fdMax; j++)
                        {
                            if (FD_ISSET(j, &master))
                            {
                                if (j != listener && j != i)
                                {
                                    if (send(j, buf, nbytes, 0) == -1)
                                    {
                                        perror("send");
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return 0;
}
