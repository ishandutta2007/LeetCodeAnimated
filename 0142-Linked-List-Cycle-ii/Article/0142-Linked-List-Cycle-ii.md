# LeetCode Problem No. 142: Circular Linked List II

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The topic shared today comes from question No. 142 on LeetCode: Circular Linked List II. The difficulty level of the questions is Medium.

### Title description

Given a linked list, return the first node where the linked list begins to enter the loop. If the linked list is acyclic, `null` is returned.

To represent a cycle in a given linked list, we use the integer `pos` to represent the position in the linked list where the tail of the linked list is connected (indexing starts from 0). If `pos` is `-1`, there is no cycle in the linked list.

**Example 1:**

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a ring in the linked list, the tail of which is connected to the second node.
```

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/vweoq.png)

**Example 2:**

```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a ring in the linked list, the tail of which is connected to the first node.
```

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/kxbrz.png)

**Example 3:**

```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/w3vsg.png)

**Advanced:**

Can you solve this problem without extra space?

### Question Analysis - Hash Table

The common solution is to use a hash table to save the visited nodes, and at the same time check whether the same node already exists in the hash table during the traversal process

### Code implementation

```javascript
/**
 * JavaScript description
 * Hash table method
 */
var detectCycle = function(head) {
    let res = [ ];
    while (head !== null) {
        if (res.includes(head)) {
            return head;
        }
        res.push(head);
        head = head.next;
    }
    return null;
};
```

### Complexity analysis

- Time complexity: **O(n)**
- Space complexity: **O(n)**

### Question Analysis - Floyd Algorithm

Floyd's algorithm can reach constant space to solve this problem.

I found this algorithm description on Wikipedia, and I quote it here.

**Floyd Cycle Detection Algorithm**, also known as **Tortoise and Hare Algorithm** (**Tortoise and Hare Algorithm**), is an algorithm that can determine whether there is a [ring](https://zh.wikipedia.org/wiki/ring_(graph theory)), [iterative function](https://zh.wikipedia.org/wiki/iterative function) or [linked list](https://zh.wikipedia.org/wiki/linked list), and find the starting point and length of the ring.

If there is a ring in a finite state machine, iterative function or linked list, then there must be a starting point that can reach somewhere in a certain ring (this starting point can also be on a certain ring).

In the initial state, it is assumed that a certain starting node is known to be node *S*. Now suppose there are two pointers `t` and `h`, pointing both of them to *S*.

Then, move `t` and `h` forward at the same time, but at different speeds: `t` advances `1` step and `h` advances `2` steps. As long as both can move forward without encountering each other, keep both moving forward. When `h` cannot go forward, that is, when it reaches a node with no successor, it can be determined that starting from *S* will not encounter a cycle. On the contrary, when `t` and `h` meet again, it can be determined that starting from S will definitely enter a certain ring, let it be ring *C*.

If it is determined that a certain ring exists, the starting point and length of the ring can be found.

When the above algorithm just determines that there is a ring *C*, it is obvious that t and `h` are located at the same node, let it be the node *M*. Obviously, we only need to keep `h` motionless, and t continues to advance, and eventually it will return to node *M*. Count the number of steps t advances this time. Obviously, this is the length of ring *C*.

In order to find the starting point of the ring *C*, just let h still be located at the node *M*, and let t return to the starting node *S*. At this time, the distance between h and t is an integer multiple of the length of the ring *C*. Then, move `t` and `h` forward simultaneously, keeping both at the same speed: `t` moves forward `1` step for every `1` step forward. This process continues until `t` and `h` meet again. Assume that this encounter is at the same node *P*. Then node *P* is the first node of ring *C* reached from node *S*, that is, a starting point of ring *C*.

**After reading this, do you have many doubts and why do you think this is happening?**

Let’s simply prove it with mathematics:

Assume that the number of nodes in the linked list is `num`, the number of nodes from head to the entrance of the linked list ring is `m` (excluding the entry node), the number of nodes in the ring is `n`, and the entry point of the linked list ring is *P*

From this we can get `num = m + n`

Assume that the slow pointer `Tortoise` (turtle) walks `1` nodes each time and takes `x` steps

Assume that the fast pointer `Hare` (rabbit) walks `2` nodes each time and takes `f` steps

Then `f = 2x`

When they meet for the first time, they must be inside the ring. Let the point be *M*. After the rabbit reaches point *M* for the first time, it will at least make one more circle in the ring before catching up with the tortoise.

Assuming that we go around `k` circles, we can get

`f = x + kn`

The number of steps the rabbit takes to reach point *P* is

`f = m + kn`

From the two equations `f = 2x` and `f = x + kn` we can get `x = kn`

From `f = m + kn` and `x = kn`, it can be seen that the turtle needs to walk `m` steps to reach point *P*

The length of `m` is exactly the length from head to the number of nodes at the entrance of the linked list ring, which is unknown.

Then let the rabbit walk from head at the speed of the tortoise, and the tortoise walks at point *M*. When the rabbit and the tortoise meet, they have taken `m` steps, and they have reached node *P*.

### Animation description

![](../Animation/Animation.gif)

### Code implementation

```java
/**
 * JavaScript description
 *Floyd's Circle Algorithm
 */
var detectCycle = function(head) {
    if (head == null) {
        return head;
    }
    //Set the speed pointer
    let tortoise = head,
        hare = head;
    // Check if there is a cycle in the linked list
    while (true) {
        if (hare == null || hare.next == null) {
            return null;
        }
        hare = hare.next.next;
        tortoise = tortoise.next;
        if (hare == tortoise) {
            break;
        }
    }
    // The rabbit and the tortoise meet for the second time and find the entrance to the ring
    hare = head;
    while (hare != tortoise) {
        hare = hare.next;
        tortoise = tortoise.next;
    }
    return hare;
};
```

### Complexity analysis

- Time complexity: **O(n)**
  - In the case of a loop, for the first and second encounters, the number of turtle steps is less than the number of linked list nodes, so it is linearly related to the number of linked list nodes;
  - In the case of a loop, the rabbit takes approximately n/2 steps to reach the end, so it is also linearly related to the number of nodes in the linked list.
- Space complexity: **O(1)**, double pointers use constant size extra space

![](../../Pictures/qrcode.jpg)