import { LinkedList } from "./linkedlist/LinkedList.js";

let myLinkedList = new LinkedList(4);
myLinkedList.pop();
console.log(myLinkedList);
myLinkedList.push(7);
myLinkedList.push(3);
myLinkedList.push(8);
console.log(myLinkedList);
myLinkedList.pop();
myLinkedList.pop();
myLinkedList.pop();
console.log(myLinkedList.pop());
console.log(myLinkedList);
myLinkedList.unshift(4);
myLinkedList.unshift(3);
console.log(myLinkedList);
myLinkedList.shift();
console.log(myLinkedList);