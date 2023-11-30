package main

import (
	"fmt"
	"strings"
)

// Time: O(N/2) and Space: O(1)
func isPalindrome(inputString string) bool {
	inputString = strings.ToLower(inputString)
	first, last := 0, len(inputString)-1
	for first < last {
		if inputString[first] != inputString[last] {
			return false
		}
		first++
		last--

	}
	return true
}

func main() {
	inputList := []string{"RACECAR", "Racecar", "ABBA", "TART", "", "A man, a plan, a canal, Panama"}

	for i, value := range inputList {
		fmt.Printf("Test Case #%d: %s -> %t\n", i+1, value, isPalindrome(value))
	}
}
