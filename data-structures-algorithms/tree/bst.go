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

// func (bt *BinaryTree) Insert(value int) {
// bt.Root = insert(bt.Root, value)
// }

// func insert(node *Node, value int) *Node {
// if node == nil {
// return &Node{Value: value}
// }
// if value < node.Value {
// node.Left = insert(node.Left, value)
// } else if value > node.Value {
// node.Right = insert(node.Right, value)
// }
// return node
// }

// Space: O(1), Time: O(logN); Time Worst: O(N)
func (bt *BinaryTree) Insert(value int) {
	if bt.Root == nil {
		bt.Root = &Node{Value: value}
		return
	}

	currentNode := bt.Root
	for {
		if value < currentNode.Value {
			if currentNode.Left == nil {
				currentNode.Left = &Node{Value: value}
				break
			} else {
				currentNode = currentNode.Left
			}
		} else if value > currentNode.Value {
			if currentNode.Right == nil {
				currentNode.Right = &Node{Value: value}
				break
			} else {
				currentNode = currentNode.Right
			}
		} else {
			// Value already exist in the tree; do not insert duplicates.
			break
		}
	}
}

// Space: O(N); Time Best: O(logN); Time Worst: O(N)
func (bt *BinaryTree) Contains(value int) bool {
	currentNode := bt.Root
	for currentNode != nil {
		if value == currentNode.Value {
			return true
		} else if value > currentNode.Value {
			currentNode = currentNode.Right
		} else {
			currentNode = currentNode.Left
		}
	}
	return false
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
	fmt.Println(tree.Contains(20)) // true
	fmt.Println(tree.Contains(11)) // false
}
