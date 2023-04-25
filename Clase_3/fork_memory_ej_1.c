#include <stdio.h>
#include <unistd.h>

int var = 100;

int main() {
    int pid;

    printf("PADRE: Soy el proceso padre y mi pid es: %d\n", getpid());

    pid = fork();

    // En cuanto llamamos a fork se crea un nuevo proceso. En el proceso
    // padre 'pid' contendrá el pid del proceso hijo. En el proceso hijo
    // 'pid' valdrá 0. Eso es lo que usamos para distinguir si el código
    // que se está ejecutando pertenece al padre o al hijo.
    for( int i=0; i<10; i++){
      if (pid) // Este es el proceso padre
      {
          //printf("PADRE: Soy el proceso padre y mi pid sigue siendo: %d\n", getpid());
          var++;
          printf("PADRE var: %d\n", var);
          sleep(1);
      }
      else // Proceso hijo
      {
          //printf("HIJO: Soy el proceso hijo y mi pid es: %d\n", getpid());
          var--;
          printf("HIJO var: %d\n", var);
          sleep(1);
      }
    }
}
