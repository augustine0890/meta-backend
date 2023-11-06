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

// Space: O(1); Time Best: O(logN); Time Worst: O(N)
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
		// The in-order successor is the smallest node in the node's right subtree.
		for successor.Left != nil {
			successorParent = successor
			successor = successor.Left
		}

		// Once the in-order successor is found, there are two situations to handle:
		// 1. The in-order successor is the right child of the node to be deleted.
		// 2. The in-order successor is further down the left subtree of the node's right child.

		// If the successor is not the immediate right child of the node to be deleted,
		// we need to adjust the successor's parent's left pointer to point to the
		// successor's right child (if it exists). This effectively removes the successor
		// from its current position in the tree.
		if successor != current.Right {
			successorParent.Left = successor.Right
			// Also, the successor's right child must now become the left child of the
			// successor's parent.
			successor.Right = current.Right
		}

		// Place the successor in the position of the node to be deleted
		if current == bt.Root {
			bt.Root = successor
		} else if isLeftChild {
			parent.Left = successor
		} else {
			parent.Right = successor
		}

		// Finally, the successor's left child becomes the left child of the node to be deleted
		successor.Left = current.Left
	}
}

// Level-order traversal
// Space: O(W), where W is maximum width of the tree.
// Time: O(N), where N is the number of nodes in the tree
func (bt *BinaryTree) BreadthFirstTraversal() {
	if bt.Root == nil {
		return
	}

	// Create a queue and enqueue the root node
	queue := []*Node{bt.Root}
	visited := []int{}

	for len(queue) > 0 {
		// Dequeue the first node from the queue
		current := queue[0]
		queue = queue[1:]

		// Process the current node
		// fmt.Println(current.Value)
		visited = append(visited, current.Value)

		// Enque the left child if it exists
		if current.Left != nil {
			queue = append(queue, current.Left)
		}

		// Enque the rifht child if it exists
		if current.Right != nil {
			queue = append(queue, current.Right)
		}
	}
	fmt.Println(visited)
}

// Time: O(logN); Space: O(1)
func (bt *BinaryTree) FindClosestValue(target int) int {
	// If the tree is empty, return the zero value of int
	if bt.Root == nil {
		return 0
	}

	// Initialize the closest value to the value of the root node
	closest := bt.Root.Value
	currentNode := bt.Root

	// Traverse the tree
	for currentNode != nil {
		// Update the closest value
		if abs(target-closest) > abs(target-currentNode.Value) {
			closest = currentNode.Value
		}

		// Decide which part of the tree to exlore next
		if target < currentNode.Value {
			currentNode = currentNode.Left
		} else if target > currentNode.Value {
			currentNode = currentNode.Right
		} else {
			// If the target is equal to the current node's value, it's the closest
			break
		}
	}
	return closest
}

// Returns a new, random binary search tree holding the values 1k, 2k, ..., nk.
func CreateRandomBinaryTree(n, k int) *BinaryTree {
	bt := &BinaryTree{}
	for _, v := range rand.Perm(n) {
		bt.Insert(k * (v + 1))
	}
	return bt
}

// Hepler function to calculate the absolute vaule of an integer
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	tree := CreateRandomBinaryTree(10, 2)
	fmt.Println(tree)
	tree.Insert(110)
	fmt.Println(tree.Contains(20)) // true
	fmt.Println(tree.Contains(11)) // false
	tree.Remove((20))
	fmt.Println(tree.Contains(20)) // false
	// Perform the traversal
	tree.BreadthFirstTraversal()
	// Finding the closest value to the target
	target := 11
	fmt.Printf("The closest value to %d in the BST is %d.\n", target, tree.FindClosestValue(target))
}
