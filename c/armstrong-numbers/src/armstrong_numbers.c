#include "armstrong_numbers.h"
#include <math.h>

bool is_armstrong_number(int candidate) {
    if (candidate == 0) {
        return true;
    }
    int count = get_armstrong_length(candidate);
    int candidate_array[count];
    int* ptr = get_armstrong_array(candidate_array, count, candidate);
    int sum = 0;
    for (int i = 0; i < count; i++) {
        sum += pow(ptr[i], count);
    }
    if (sum == candidate) {
        return true;
    } else {
        return false;
    }
}

int* get_armstrong_array(int *arr, int size, int candidate) {
    for (int i = 0; i < size; i++) {
        arr[i] = candidate % 10;
        candidate /= 10;
    }
    return arr;
}

int get_armstrong_length(int candidate) {
    int count = 0;
    while (candidate != 0) {
        candidate /= 10;
        count += 1;
    }
    return count;
}