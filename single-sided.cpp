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

  for (int i = 0; i < N; ++i)
      X[i] = rand () % 10000;

  // Calculate original sum
  long int sum = 0;
  for (int i = 0; i < N; ++i)
    sum += X[i];
  printf("Original sum: %ld\n", sum);

  // Perform attack
  int value = X[N/2-1]; 
  for (int i = 0; i < M; i++)
    X[N/2-1] = rand() % 10000;
  X[N/2-1] = value;

  // Check new sum
  long int new_sum = 0;
  for (int i = 0; i < N; ++i)
    new_sum += X[i];
  printf("Sum after attack: %ld\n", new_sum);

  if (sum != new_sum)
    printf("Attack Succeeded\n\n");
  else
    printf("Attack Failed\n\n");  
  
  return 0;
}
