# LeetCode Question No. 24: Exchange nodes in a linked list pairwise

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The title comes from question No. 24 on LeetCode: Pairwise exchange of nodes in a linked list.

### Title description

Given a linked list, swap adjacent nodes in pairs and return the swapped linked list.

**You can't just change the value inside the node**, but you need to actually swap the nodes.

**Example:**

```
Given 1->2->3->4, you should return 2->1->4->3.
```

### Question Analysis - Iterative Method

It can be seen from the title description that two-by-two exchanges are required, so just exchange pointers in a group of two sub-linked lists, and set a **sentinel** to point to the exchanged sub-linked list (or the sentinel points to the second node of the sub-linked list in advance, because the second node becomes the first node after the exchange); then let the sentinel point to the next group of sub-linked lists, and continue to exchange until the end.

Assume **Sentinel** is node `prev`, the first node of the sub-linked list is `A`, the second node is `B`, and the third node is `C`, then the operation process is as follows:

- Termination condition `head == null && head -> next == null`
  1. prev -> B  ( A -> B -> C )
  2. A - > C
  3. B -> A ( prev -> B -> A -> C )
  4. prev -> A
  5. head -> C
  6. Repeat the above steps

### Animation description

<img src="../Animation/Animation1.gif" alt="Animation1" style="zoom:150%;" />

### Code implementation

```javascript
/**
 * JavaScript description
 * Iterative method
 */
var swapPairs = function(head) {
    let dummy = new ListNode(0);
    dummy.next = head;

    let prevNode = dummy;

    while (head !== null && head.next !== null) {
        // Nodes to be swapped
        let firstNode = head,
            secondNode = head.next;
        // Swapping
        prevNode.next = secondNode; // Can be placed before or after the exchange
        firstNode.next = secondNode.next;
        secondNode.next = firstNode;
        // Reinitializing the head and prevNode for next swap
        prevNode = firstNode;
        head = firstNode.next;
    }
    return dummy.next;
};
```

### Complexity analysis

- Time complexity: **O(N)**, where *N* refers to the number of nodes in the linked list
- Space complexity: **O(1)**

### Question Analysis - Recursion

The idea of ​​​​recursion is similar to that of iteration, both of which are group switching. Specifically, the recursion here is not to go deep into a problem, but to continuously push forward.

- Only one pair of nodes is exchanged in each recursion
- The next recursion is to exchange the next pair of nodes
- Return to the second node after the exchange is completed, because it is the new head of the sub-linked list after the exchange
- After the recursion is completed, return the second node of the first recursion, which is the head node of the new linked list

**Note:** Don’t use human recursion, pay more attention to the overall logic

The approximate execution flow of the example is:

- Termination condition: `(head == null) || (head.next == null)`
  1. 1 -> 2 -> 3 -> 4 (original linked list)
  2. 1 -> 3 -> 4 
  3. (2 -> 1) -> 3 -> 4 (After the first recursion is completed, return to the original second node, which is the node with a value of 2)
  4. 2 -> 1 -> 3 -> null
  5. 2 -> 1 -> (4 -> 3) (After the second recursion is completed, the original second node is returned, which is the node with a value of 4)

### Animation description

<img src="../Animation/Animation2.gif" alt="Animation2" style="zoom:150%;" />

### Code implementation

```javascript
/**
 * JavaScript description
 * Recursive method
 */
var swapPairs = function(head) {
    if (head == null || head.next == null) {
        return head;
    }
     // Nodes to be swapped
    let firstNode = head,
        secondNode = head.next;
     // Swapping
    firstNode.next = swapPairs(secondNode.next);
    secondNode.next = firstNode;

    return secondNode;
   
};
```

### Complexity analysis

- Time complexity: **O(N)**, where *N* refers to the number of nodes in the linked list
- Space complexity: **O(N)**, stack space used by the recursive process



![](../../Pictures/qrcode.jpg)

