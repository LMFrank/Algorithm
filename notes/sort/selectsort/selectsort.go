package main

import "fmt"

func SelectSort(list []int) {
	n := len(list)
	for i := 0; i < n-1; i++ {
		min := list[i]
		minIndex := i
		for j := i + 1; j < n; j++ {
			if min > list[j] {
				min = list[j]
				minIndex = j
			}
		}

		if i != minIndex {
			list[i], list[minIndex] = list[minIndex], list[i]
		}
	}
}

func main() {
	list := []int{5, 9, 1, 6, 8, 14, 6, 49, 25, 4, 6, 3}
	SelectSort(list)
	fmt.Println(list)
}
