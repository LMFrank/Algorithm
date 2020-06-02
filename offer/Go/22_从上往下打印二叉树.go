package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func PrintFromTopToBottem(r *TreeNode) []int {
	var queue []*TreeNode
	var res []int

	queue = append(queue, r)
	for len(queue) != 0 {
		node := queue[0]
		queue = queue[1:]
		res = append(res, node.Val)
		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}
	return res
}

func Print(root *TreeNode) {
	if root == nil {
		return
	}
	fmt.Printf("%d ", root.Val)
	Print(root.Left)
	Print(root.Right)
}

func main() {
	root := &TreeNode{1, &TreeNode{2, &TreeNode{4, nil, nil}, &TreeNode{5, nil, nil}}, &TreeNode{3, nil, nil}}
	Print(root)
	fmt.Printf("\n")
	fmt.Println(PrintFromTopToBottem(root))
	fmt.Printf("\n")
}
