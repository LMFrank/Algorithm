package problem02

func replaceSpace(str string) string {
	var res string

	for _, s := range str {
		if s == 32 {
			res += "%20"
		} else {
			res += string(s)
		}
	}
	return res
}
