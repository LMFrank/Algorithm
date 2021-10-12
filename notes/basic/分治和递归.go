package main

import "fmt"

// 1 * 2 * 3 * 4 *...* N

func Rescuvie(n int) int {
	if n == 0 {
		return 1
	}

	return n * Rescuvie(n-1)
}

func RescuiveTail(n int, a int) int {
	if n == 1 {
		return a
	}

	return RescuiveTail(n-1, a*n)
}

func main() {
	fmt.Println(Rescuvie(5))
	fmt.Println(RescuiveTail(5, 1))
}
