/*
 ** Author: Carlos Taffernaberry <ctaffer@unsl.edu.ar> 
 **
 ** This program is free software; you can redistribute it and/or modify it
 ** under the terms of the GNU General Public License as published by the
 ** Free Software Foundation; either version 2 of the License, or (at your
 ** option) any later version.  See <http://www.fsf.org/copyleft/gpl.txt>.
 **
 ** This program is distributed in the hope that it will be useful, but
 ** WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 ** or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 ** for more details.
 **/
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int glob = 200;

void *hilo_suma()
{
    printf("Hello World! .... soy yo , el hilo_suma \n");
    int i;
    for (i = 0; i < 100000; i++) {
		glob++;
    }
    pthread_exit(NULL);
}

void *hilo_resta()
{
    printf("Hello World! .... soy yo , el hilo_resta \n");
    int i;
    for (i = 0; i < 100000; i++) {
		glob--;
    }
    pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
    pthread_t hilo_s,hilo_r;
    int rc;
    printf("El main ... creando los threads\n");
    rc = pthread_create(&hilo_s, NULL, hilo_suma, NULL);
    if (rc) {
	printf("ERROR; pthread_create() = %d\n", rc);
	exit(-1);
    }
    rc = pthread_create(&hilo_r, NULL, hilo_resta, NULL);
    if (rc) {
	printf("ERROR; pthread_create() = %d\n", rc);
	exit(-1);
    }
   /* espera por finalizacio'n de TODOS*/
    pthread_join(hilo_s, NULL);
    pthread_join(hilo_r, NULL);
    printf ("valor global %d\n", glob);
    pthread_exit(NULL);
    return (0);
}
