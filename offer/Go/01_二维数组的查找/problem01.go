package problem01

func Find(array [][]int, target int) bool {
	n := len(array)
	m := len(array[0])
	for i, j := 0, m-1; i < n && j > 0; {
		if array[i][j] == target {
			return true
		}
		if array[i][j] > target {
			j--
			continue
		} else {
			i++
		}
	}
	return false
}
