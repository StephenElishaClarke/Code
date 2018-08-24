//#include "C/FlyCapture2_C.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <termios.h>
#include <time.h>
#include <errno.h>   

#define DEV_NAME "/dev/ttyS0"
#define BAUD_RATE B9600

int port = open( "/dev/ttyS0", O_RDWR| O_NONBLOCK | O_NDELAY );

//struct termios tty;
//memset (&tty, 0, sizeof tty);

/* Set Baud Rate */
//cfsetospeed (&tty, B9600);
//cfsetispeed (&tty, B9600);

//tcflush( USB, TCIFLUSH );

/*
void serial_init(int fd) {
  struct termios tio;
  memset(&tio, 0, sizeof(tio));
  tio.c_cflag = CS8 | CLOCAL | CREAD;
  tio.c_cc[VTIME] = 100;
  cfsetispeed(&tio, BAUD_RATE);
  cfsetospeed(&tio, BAUD_RATE);
  tcsetattr(fd, TCSANOW, &tio);
}

int main(int argc, char **argv) {
  int fd;
  int i,j;
  int len;
  unsigned char buffer[BUFF_SIZE], in_data[BUFF_SIZE];

  printf("start serial port read example..\n");

  fd = open(DEV_NAME, O_RDWR | O_NONBLOCK );
  if(fd<0) {
    printf("ERROR on device open\n");
    exit(1);
  }

  printf("init serial port\n");
  serial_init(fd); 

  printf("start main loop...\n");
  j=0;
 
  while(1) {
    len = read(fd, buffer, BUFF_SIZE); 
    if(len==0) {
      continue;
    }

    if(len<0) {
      printf("%s: ERROR\n", argv[0]);
      perror("");
      exit(2);
    }

    for(i=0; i<len; i++) {
      printf("%02X", buffer[i]); 
      i++;
      in_data[i] = buffer[i];
    }
    if((in_data[j - 1] == 0x0a) || (in_data[j - 1] == 0)) {
      in_data[j - 1] = 0x0a;
      in_data[j] = 0;
      printf("\n read-data=%s\n",&in_data[0]);
      write(fd,&in_data[0],strlen(&in_data[0]));
      j = 0;
    }
  }
}
*/ 
