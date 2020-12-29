package raindrops

import "strconv"

// Convert takes the number of drops and returns a raindrop string
func Convert(drops int) string {
	result := ""
	if drops%3 == 0 {
		result += "Pling"
	}
	if drops%5 == 0 {
		result += "Plang"
	}
	if drops%7 == 0 {
		result += "Plong"
	}
	if len(result) > 0 {
		return result
	}
	return strconv.Itoa(drops)
}
