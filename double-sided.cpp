#include <cstdio>
#include <stdlib.h>

int main (int argc, char *argv[]) {
  if (argc != 3) {
  	printf("Expected two arguments: vector_length, num_acceses. Instead got %d arguments.\n", argc-1);
  	return -1;
  }
  
  const int N = atoi(argv[1]);
  const int M = atoi(argv[2]); 
  int X[N];

  for (int i = 1; i < N-1; ++i)
      X[i] = 1000;

  // Calculate original sum
  long int sum = 0;
  for (int i = 1; i < N-1; ++i)
    sum += X[i];
  printf("Original sum: %ld\n", sum);

  // Perform attack
  int value1 = X[N/2-1];
  int value2 = X[N/2+1]; 
  for (int i = 0; i < M; i++) {
    X[N/2-1] = 1000;
    X[N/2+1] = 1000;
  }
  X[N/2-1] = value1;
  X[N/2+1] = value2;

  // Check new sum
  long int new_sum = 0;
  for (int i = 1; i < N-1; ++i)
    new_sum += X[i];
  printf("Sum after attack: %ld\n", new_sum);

  if (sum != new_sum)
    printf("Attack Succeeded\n\n");
  else
    printf("Attack Failed\n\n");  
  
  return 0;
}
