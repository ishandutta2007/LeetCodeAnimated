# LeetCode Problem No. 25: A set of K flipped linked lists

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 25 on LeetCode: A group of K flipped linked lists. The difficulty of the question is Hard

### Title description

You are given a linked list, and each group of *k* nodes is flipped. Please return the flipped linked list.

*k* is a positive integer whose value is less than or equal to the length of the linked list.

If the total number of nodes is not an integer multiple of *k*, then please keep the last remaining nodes in their original order.

**Example:**

Give you this linked list: `1->2->3->4->5`

When *k* = 2, it should return: `2->1->4->3->5`

When *k* = 3, it should return: `3->2->1->4->5`

**illustrate:**

- Your algorithm can only use a constant amount of extra space.
- **You can't just change the value inside the node**, but you need to actually swap the nodes.

### Question analysis

This algorithm question can be said to be an upgraded version of [Pairwise Swap Nodes in a Linked List](https://github.com/MisterBooo/LeetCodeAnimation/blob/master/0024-Swap-Nodes-in-Pairs/Article/0024-Swap-Nodes-in-Pairs2.md). The difference is that the number of reversed sub-linked list nodes has become customized.

The general idea is still the same, and it can be divided into two processing modules:

1. Divide several sub-linked lists that need to be reversed according to *k*, connect the reversed sub-linked lists, and finally keep the sub-linked lists less than *k* unchanged.

   - Set the sentinel `dummy` to point to `head`, in order to find the reversed list head node;

   - Loop *k* to determine the range of sublists that need to be reversed:

     - The loop is completed and it is determined that the sub-linked list can be reversed

       Assume that *A* and *B* sub-linked lists are adjacent and can be reversed

       - The pointer `start` points to the head node of *A*, `end` points to the tail node of *A*, and `nxt` points to the head node of *B*
       - After `start -> end` is reversed, `start` becomes the end node of A, `start -> next = nxt`, and the reversed *A* linked list points to *B*
       - Reset `start` to the head node of *B*, `end` to the tail node of *B*, `nxt` to the head node of the next sub-linked list, and reverse the *B* linked list
       - Repeat the above actions until the loop terminates

     - The loop terminates, the remaining nodes are insufficient *k*, the reversal is terminated, and the linked list is returned.

2. Reverse the sub-linked list

   Assume that the first three nodes of the sub-linked list are *a*, *b*, *c*, set the pointers `pre`, `cur`, `nxt`, initialize the value of `pre` to `null`, the value of `cur` to *a*, and the value of `nxt` to *a*. The positions of these three pointers remain unchanged and adjacent.

   Termination condition: `cur` is not empty

   Point the current node pointer to the previous node

   1. `cur` points to `nxt` (the value of `nxt` is *b*)
   2. `cur` points to `pre` (`cur` points to `null`)
   3. `cur` is assigned to `pre` (the value of `pre` is *a*), `nxt` is assigned to `cur` (the value of `cur` is *b*)
   4. When executing step `1` (the value of `nxt` is *c*, which is equivalent to `pre`, `cur`, `nxt` points to move backward `1` bit in sequence)
   5. Repeat the above actions

### Animation description

<img src="../Animation/Animation.gif" alt="Animation" style="zoom:150%;" />

### Reference code

#### Reverse linked list

```javascript
/**
 * JavaScript description
 * Reverse the elements of the interval [start, end), note that end is not included
 */
function reverse(start, end) {
    let pre = null,
        cur = start,
        nxt = start;
    while (cur != end) {
        nxt = cur.next;
        //Reverse node by node
        cur.next = pre;
        //Update pointer position
        pre = cur;
        cur = nxt;
    }
    // After the head node is reversed, start has been moved to the end, and end has not changed.
    return pre;
};
```

#### Recursive solution

```javascript
/**
 * JavaScript description
 * recursion
 */
var reverseKGroup = function(head, k) {
    if (head == null) {
        return null;
    }
    let start, end;
    start = end = head;
    for (let i = 0; i < k; i++) {
        // Less than k, no need to reverse
        if (end == null) {
            return head;
        }
        end = end.next;
    }
    //Reverse the first k elements, excluding end
    let reverseHead = reverse(start, end);
    //Recursively reverse the next k elements and connect them back and forth
    start.next = reverseKGroup(end, k);
    return reverseHead;
};
```

#### Iterative solution

```javascript
/**
 * JavaScript description
 * iteration
 */
var reverseKGroup = function(head, k) {
    let dummy = new ListNode(0);
    dummy.next = head;
    let pre, start ,end, nxt;
    pre = start = end = nxt = dummy;
    while (end.next != null) {
        for (let i = 0; i < k && end != null; i++) {
            end = end.next;
        }
        if (end == null) {
            // Less than k, jump out of the loop
            break;
        }
        start = pre.next;
        nxt = end.next;
        //Reverse the first k elements, excluding nxt
        pre.next = reverse(start, nxt);
        //The linked list behind the link
        start.next = nxt;
        // pre, end reset to the next k sub-linked list
        pre = start;
        end = pre;
    }
    return dummy.next;
};
```

### Complexity analysis

- Time complexity: **O( nk )** , best case O( n ), worst case O( n^2 )

- Space complexity: **O( 1 )**





![](../../Pictures/qrcode.jpg)