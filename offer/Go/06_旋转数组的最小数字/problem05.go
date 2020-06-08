package problem05

func minNumberInRotateArray(array []int) int {
	if array == nil {
		return 0
	}

	left := 0
	right := len(array) - 1

	for left < right {
		mid := (left + right) / 2
		if array[mid] > array[right] {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return array[left]

}
