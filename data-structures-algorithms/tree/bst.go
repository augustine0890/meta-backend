package main

import (
	"fmt"
	"math/rand"
)

type Node struct {
	Value       int
	Left, Right *Node
}

type BinaryTree struct {
	Root *Node
}

// NewBinaryTree creates a new instance BinaryTree
func NewBinaryTree() *BinaryTree {
	return &BinaryTree{}
}

func (bt *BinaryTree) Insert(value int) {
	bt.Root = insert(bt.Root, value)
}

func insert(node *Node, value int) *Node {
	if node == nil {
		return &Node{Value: value}
	}
	if value < node.Value {
		node.Left = insert(node.Left, value)
	} else if value > node.Value {
		node.Right = insert(node.Right, value)
	}
	return node
}

// Returns a new, random binary search tree holding the values 1k, 2k, ..., nk.
func CreateRandomBinaryTree(n, k int) *BinaryTree {
	bt := &BinaryTree{}
	for _, v := range rand.Perm(n) {
		bt.Insert(k * (v + 1))
	}
	return bt
}

func main() {
	tree := CreateRandomBinaryTree(10, 2)
	fmt.Println(tree)
	tree.Insert(110)
	fmt.Println(tree)
}
