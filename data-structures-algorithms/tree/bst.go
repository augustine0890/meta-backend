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

func (bt *BinaryTree) Remove(value int) {
	var parent *Node
	current := bt.Root
	isLeftChild := false

	// Find the node to be deleted and its parent
	for current != nil && current.Value != value {
		parent = current
		if value < current.Value {
			current = parent.Left
			isLeftChild = true
		} else {
			current = parent.Right
			isLeftChild = false
		}
	}

	if current == nil {
		return // Node not found
	}

	// Case 1: Node with no children
	if current.Left == nil && current.Right == nil {
		if current == bt.Root {
			bt.Root = nil
		} else if isLeftChild {
			parent.Left = nil
		} else {
			parent.Right = nil
		}
	} else if current.Left == nil {
		// Case 2-1: Node with no left child (one child right)
		if current == bt.Root {
			bt.Root = current.Right
		} else if isLeftChild {
			parent.Left = current.Right
		} else {
			parent.Right = current.Right
		}
	} else if current.Right == nil {
		// Case 2-2: Node with no right child (one child left)
		if current == bt.Root {
			bt.Root = current.Left
		} else if isLeftChild {
			parent.Left = current.Left
		} else {
			parent.Right = current.Left
		}
	} else {
		// Case 3: Node with two children
		successorParent := current
		successor := current.Right
		for successor.Left != nil {
			successorParent = successor
			successor = successor.Left
		}
		if successor != current.Right {
			successorParent.Left = successor.Right
			successor.Right = current.Right
		}

		if current == bt.Root {
			bt.Root = successor
		} else if isLeftChild {
			parent.Left = successor
		} else {
			parent.Right = successor
		}
		successor.Left = current.Left
	}
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
