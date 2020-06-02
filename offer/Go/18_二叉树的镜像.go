package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func Mirror(p *TreeNode) {
	if p == nil {
		return
	}

	p.Left, p.Right = p.Right, p.Left
	Mirror(p.Left)
	Mirror(p.Right)
}

func Print(root *TreeNode) {
	if root == nil {
		return
	}

	fmt.Printf("%d", root.Val)
	Print(root.Left)
	Print(root.Right)
}

func main() {
	root := &TreeNode{1, &TreeNode{2, &TreeNode{4, nil, nil}, &TreeNode{5, nil, nil}}, &TreeNode{3, nil, nil}}
	Print(root)
	fmt.Printf("\n")
	Mirror(root)
	Print(root)
}
