/*
Package hamming contains the Distance method for
calculating the Hamming distance of two strings.
*/
package hamming

import (
	"errors"
)

/*
Distance returns the hamming distance between two strings.
If the strings are of unequal length it returns 0 and an error.
*/
func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, errors.New("Unequal String Lengths")
	}
	count := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			count++
		}
	}
	return count, nil
}
