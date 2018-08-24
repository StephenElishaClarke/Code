#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

/*
typedef struct TimeStamp
{
    int array[0][2];
}   TimeStamp;
*/


struct TimeStamp
{   
     int sec;
     int pixels[3][3];
     int *ptr;
};

void populate(struct TimeStamp *ptr) 
{       
     ptr->sec = 5;
     int a[3][3] = {
          {1, 2, 3},
          {4, 5, 6},
          { 7, 8, 9}
          }; 
     ptr->pixels[0][0] = a[0][0]; //= a;
     //TimeStamp *ptr = &TS;
     //&TS = a;  
}

/*

void foo(int count, float** array, int size)
{
    int ii,jj;
    for (ii=0;ii<count;ii++){
       for (jj=0;jj<size;jj++)
          array[ii][jj] *= 2;
    }
 
}

*/


//==============================================================================


/*

struct TimeStamp
{
    int sec;
    int *ptr;
};

//struct TimeStamp TS;

//struct TimeStamp *ptr;

//struct TimeStamp *ptr = &TS; 

//int n = 5;

void populate(struct TimeStamp *ptr) //(struct TimeStamp TS) (..., int n)
{
    //TS.sec = 5;
    ptr->sec = 5;    // ptr->sec = n;
    // printf("%p/n",ptr);
}

//struct TimeStamp * pass_pointer()   //TS was *ptr, null like void
//{
//     //struct TimeStamp *ptr = &TS;
//     return ptr;   // &TS  Either works, which is preferred?
//}

*/

//==============================================================================

/*
   
int frame = 2;

int* ptr = &frame;
 
int* pass_pointer()
{  
    return ptr;
}

*/
