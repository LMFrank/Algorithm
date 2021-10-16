package main

import "fmt"

/*
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
*/

/*
// 斐波那契数列：1123581321... N-1 N 2N-1

func Fib(n int, a1 int, a2 int) int {
	if n == 0 {
		return a1
	}

	return Fib(n-1, a2, a1 + a2)
}

func main() {
	fmt.Println(Fib(1, 1, 1))
	fmt.Println(Fib(2, 1, 1))
	fmt.Println(Fib(3, 1, 1))
	fmt.Println(Fib(4, 1, 1))
	fmt.Println(Fib(5, 1, 1))
}
*/

// 二分查找：1, 5, 9, 15, 81, 89, 123, 189, 333，找到189
func BinarySearch(array []int, target int, l int, r int) int {
	if l > r {
		return -1
	}

	mid := (l + r) / 2
	midNum := array[mid]

	if midNum == target {
		return mid
	} else if midNum > target {
		return BinarySearch(array, target, l, mid-1)
	} else {
		return BinarySearch(array, target, mid+1, r)
	}
}

func main() {
	array := []int{1, 5, 9, 15, 81, 89, 123, 189, 333}
	target := 500
	result := BinarySearch(array, target, 0, len(array)-1)
	fmt.Println(target, result)

	target = 189
	result = BinarySearch(array, target, 0, len(array)-1)
	fmt.Println(target, result)
}
