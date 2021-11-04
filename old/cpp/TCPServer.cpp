//Hej jojhnny
#include <iostream>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <strings.h>
#include <unistd.h>
#include <arpa/inet.h>
using namespace std;

#define PORTNO 8080
#define IP "192.168.0.100"

 
int main(int argc, char *argv[]){
    std::cout << "Starting TCP Server" << std::endl;

    //Variables
    int newsockfd;
    socklen_t clilen;
    char buffer[256];
    struct sockaddr_in serv_addr, cli_addr;
    int n;

    //Create socket
    int sockfd = socket(AF_INET, SOCK_STREAM, 0); //AF_INET = IPv4 Protocol, SOCK_STREAM: TCP

    if (sockfd < 0){
        cout <<"ERROR opening socket" << endl;
    }

    //Create server address
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET; //IPv4
    serv_addr.sin_port = htons(PORTNO); //Port
    //serv_addr.sin_addr.s_addr = INADDR_ANY; //Automatically finds IP Address
    inet_aton(IP, &serv_addr.sin_addr); //Manually input IP Address

    //Print port & ip address
    cout << "Portno: " << PORTNO << endl; 
    //some_addr = inet_ntoa(antelope.sin_addr); // return the IP
    printf("IP Address: %s\n", inet_ntoa(serv_addr.sin_addr)); // prints the servers IP Address

    //Bind socket to IP Address and port number
    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) //Associate a socket with an IP address and port number
        cout << "ERROR on binding" << endl;;


    
    //Listen for incoming connections
    listen(sockfd,5); //Tell a socket to listen for incoming connections

    while (1)
    { 
    //Wait for client to connect
    clilen = sizeof(cli_addr); //Placeholder variable
    newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
    printf("Client has connected with IP Address: %s\n", inet_ntoa(cli_addr.sin_addr)); // Prints the client's IP Address


    
    //Receives data from the client
    if (newsockfd < 0) std::cout << "ERROR on accept" << std::endl;
        bzero(buffer,256);
    n = read(newsockfd,buffer,255);
    if (n < 0) cout << "ERROR reading from socket" << endl;
        printf("Here is the message: %s\n",buffer);
    n = write(newsockfd,"I got your message",18);
    if (n < 0) cout << "ERROR writing to socket" << endl;
        close(newsockfd);
    close(sockfd);
    }
    return 0;
}






























