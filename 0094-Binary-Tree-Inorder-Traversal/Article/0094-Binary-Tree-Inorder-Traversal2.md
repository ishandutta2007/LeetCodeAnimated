## LeetCode Problem No. 94: In-order traversal of a binary tree

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 94 on LeetCode: In-order traversal of a binary tree. The difficulty level of the questions is Medium

### Title description

Given a binary tree, return its **inorder** traversal.

#### Example:

```cassandra
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

**Advanced:** The recursive algorithm is simple, can you do it with an iterative algorithm?

### Question analysis

#### The first method: recursion

I believe everyone is familiar with the in-order traversal of a binary tree. The operation process is **Left -> Print -> Right**.

Then just traverse the tree in the order of **Left -> Print -> Right**. Recursive function implementation

- Termination condition: when the current node is empty
- Within the function: recursively call the left node, print the current node, and then recursively call the right node

##### Reference code

```javascript
// lang=javascript
var inorderTraversal = function(root) {
    let res = [];
    handle(root,res);
    return res;
};
function handle(root, res) {
    if (root !== null) {
        handle(root.left, res);
        res.push(root.val);
        handle(root.right, res);
    }
}
```

##### Complexity Analysis

- Time complexity: O(n),
- Space complexity: O(h), h is the height of the tree

#### Second method: iteration

The real difficulty of this problem is how to implement it in a non-recursive way.

The recursive calling process is to keep going to the left. When it can't go any further on the left, it prints the node and turns to the right. Then the process continues on the right. The function calls itself, nested layer by layer. The operating system/virtual machine automatically helps us use **stack** to save each called function. Now we need to simulate such a calling process ourselves.

The characteristic of the stack is **last in, first out**, then we will push the node traversing the left subtree onto the stack. When the left subtree cannot be found, the top of the stack is the bottom left subtree, pop it out and print it out; then turn to the parent node of the right subtree, continue to traverse the left subtree of the parent node and push it onto the stack, and the cycle is like this.

So the traversal process is:

1. Push the root node on the stack
2. Traverse the left subtree and push the stack until the left subtree is empty
3. Pop the top element of the stack and print
4. Turn to the right subtree and repeat steps 1, 2, and 3.

##### Animation understanding

<img src="../Animation/Animation2.gif" alt="Animation2" style="zoom:150%;" />

##### Reference code

```javascript
// lang=javascript
var inorderTraversal = function(root) {
    let res = [],
        stack = [],
        node  = root;
    while (stack.length > 0 || node !== null) {
        while (node) {
            stack.push(node);
            node = node.left;
        }
        node = stack.pop();
        res.push(node.val);
        node = node.right;
    }
    return res;
}
```

##### Complexity Analysis

- Time complexity: O(n)
- Space complexity: O(n)

![qrcode](../../Pictures/qrcode.jpg)







