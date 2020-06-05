package main

import "fmt"

type NodeList struct {
	Val  int
	Next *NodeList
}

func printListFromTailToHead01(head *NodeList) []int {
	if head == nil {
		return []int{}
	}
	return append(printListFromTailToHead01(head.Next), head.Val)
}

func printListFromTailToHead02(head *NodeList) []int {
	if head == nil {
		return []int{}
	}
	var res []int
	for head != nil {
		res = append(res, head.Val)
		head = head.Next
	}

	for i, j := 0, len(res)-1; i < j; {
		res[i], res[j] = res[j], res[i]
		i++
		j--
	}
	return res
}

func main() {
	n3 := &NodeList{3, nil}
	n2 := &NodeList{2, n3}
	n1 := &NodeList{1, n2}

	fmt.Printf("\n NodeList: 1 -> 2 -> 3 \n")
	//res := printListFromTailToHead01(n1)
	res := printListFromTailToHead02(n1)
	fmt.Printf("\n Output: %v", res)
}
