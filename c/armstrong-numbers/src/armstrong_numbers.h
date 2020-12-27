#ifndef ARMSTRONG_NUMBERS
#define ARMSTRONG_NUMBERS

#include <stdbool.h>

bool is_armstrong_number(int candidate);
int get_armstrong_length(int candidate);
int* get_armstrong_array(int *arr, int size, int candidate);

#endif
