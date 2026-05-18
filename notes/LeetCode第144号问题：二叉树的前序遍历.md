# LeetCode Question No. 144: Pre-order traversal of binary trees

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 144 on LeetCode: Preorder traversal of binary trees. The difficulty level of the questions is Medium, and the current passing rate is 59.8%.

### Title description

Given a binary tree, return its *preorder* traversal.

 **Example:**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3 

Output: [1,2,3]
```

**Advanced:** The recursive algorithm is simple, can you do it with an iterative algorithm?

### Question analysis

Use the stack idea to deal with problems.

The order of preorder traversal is **root-left-right**, and the specific algorithm is:

- Push the root node to the stack
- Loop to check whether the stack is empty. If not, remove the top element of the stack and save its value.
- Check whether its right child node exists, and if it exists, push it to the stack
- Look at its left child node, and if it exists, push it to the stack.



### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/uu82j.gif)

### Code implementation

```
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        //Non-recursive pre-order traversal requires the use of the stack
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> list = new LinkedList<>();
        //When the tree is an empty tree, directly return an empty list
        if(root == null){
            return list;
        }
        //The first step is to push the root node onto the stack
        stack.push(root);
        //When the stack is not empty, the popped elements are inserted into the end of the list.
        //When its child is not empty, push the child onto the stack. The right child must be pushed first and then the left child.
        while(!stack.isEmpty()){
            //The root here is just a reuse of a variable
            root = stack.pop();
            list.add(root.val);
            if(root.right != null) stack.push(root.right);
            if(root.left != null) stack.push(root.left);
        }
        return list;
    }
}
```







![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/obddd.png)