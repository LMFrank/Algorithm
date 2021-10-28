package main

import "fmt"

func BubbleSort(list []int) {
	n := len(list)
	didSwap := false

	for i := n - 1; i > 0; i-- {
		for j := 0; j < i; j++ {
			if list[j] > list[j+1] {
				list[j], list[j+1] = list[j+1], list[j]
				didSwap = true
			}
		}
		if !didSwap {
			return
		}
	}
}

func main() {
	// list := []int{5, 9, 1, 6, 8, 14, 6, 49, 25, 4, 6, 3}
	list := []int{1, 2, 3, 4, 5}
	BubbleSort(list)
	fmt.Println(list)
}
