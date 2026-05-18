# LeetCode Question No. 102: Level-order traversal of binary trees

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 102 on LeetCode: Level-order traversal of a binary tree. The difficulty level of the questions is Medium, and the current pass rate is 55.8%.

### Title description

Given a binary tree, return the node values ​​traversed hierarchically. (i.e. visit all nodes layer by layer, from left to right).

For example:
Given a binary tree: `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

Return its level traversal results:

```
[
  [3],
  [9,20],
  [15,7]
]
```

### Question analysis

This problem requires the use of **queue**

- Create a queue
- Put the root node in first, then find the left and right child nodes of the root node
- Remove the root node. At this time, the elements in the queue are all the nodes in the next layer.
- Use a for loop to traverse and store the results in a one-dimensional vector
- After traversing, store this one-dimensional vector into a two-dimensional vector.
- By analogy, layer-order traversal can be completed





### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/2elr5.gif)



### Code implementation

```
/// BFS
/// Time Complexity: O(n), where n is the number of nodes in the tree
/// Space Complexity: O(n)
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {

        vector<vector<int>> res;
        if(root == NULL)
            return res;

        queue<pair<TreeNode*,int>> q;
        q.push(make_pair(root, 0));

        while(!q.empty()){

            TreeNode* node = q.front().first;
            int level = q.front().second;
            q.pop();

            if(level == res.size())
                res.push_back(vector<int>());
            assert( level < res.size() );

            res[level].push_back(node->val);
            if(node->left)
                q.push(make_pair(node->left, level + 1 ));
            if(node->right)
                q.push(make_pair(node->right, level + 1 ));
        }

        return res;
    }
};

```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/96yrg.png)