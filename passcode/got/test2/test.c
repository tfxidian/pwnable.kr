/*************************************************************************
	> File Name: test.c
	> Author: 
	> Mail: 
	> Created Time: Fri 29 Nov 2019 09:44:29 AM UTC
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[1]){
    if(argc <2){
        printf("argv[1] required!\n");
        exit(0);
    }
    printf("you input:");
    printf(argv[1]);
    printf("Down\n");
    return 0;
}


