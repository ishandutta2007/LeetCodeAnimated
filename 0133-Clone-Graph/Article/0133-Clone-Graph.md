# LeetCode Issue No. 133: Clone Graph

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The title comes from question No. 133 on LeetCode: Clone Graph. The difficulty level of the questions is Medium, and the current pass rate is 54.8%.

### Title description

Given a reference to a node in an undirected connected graph, please return a deep copy (clone) of the graph. Each node in the graph contains its value val (int) and a list of its neighbors (list[Node]).


**Example 1:**

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
explain:
There are 4 nodes in the graph.
The value of node 1 is 1, and it has two neighbors: nodes 2 and 4.
The value of node 2 is 2 and it has two neighbors: nodes 1 and 3 .
The value of node 3 is 3 and it has two neighbors: nodes 2 and 4 .
The value of node 4 is 4 and it has two neighbors: nodes 1 and 3 .
```

**Example 2:**

```
Input: adjList = [[]]
Output: [[]]
Explanation: The input contains an empty list. The graph has just one node with value 1 and it has no neighbors.
```

**Example 3:**

```
Input: adjList = [[2],[1]]
Output: [[2],[1]]
```

### Question analysis

I’ll give you a picture and ask you to make a complete copy. This question is not difficult, but it is often encountered in actual work projects. There are many ways to solve this question, but it is recommended to think from the perspective of practical work.

The graph is composed of nodes. To completely copy the graph means that we need to copy each node, and the relationship between nodes also needs to be copied. It is not difficult to do this. We only need to traverse the graph once. The key point here is that the question emphasizes that it is an **undirected graph**, which means that we can start from any point on the graph and reach all nodes on the graph. Then the question turns to how to traverse the graph. We can use breadth-first search or depth-first search. From a work perspective, breadth-first search is recommended because it is easy to understand, simple to implement, and does not involve stack overflow issues. It is safer to process large-scale data.

<br>

### Animation demonstration

![](../Animation/133.gif)

<br>

### Complexity analysis

Generally, breadth-first search is used to traverse the graph, and the time complexity is `O(n + m)`, where n here represents the number of nodes on the graph, and m represents the number of edges on the graph. From the point-to-face nature of breadth-first search, you can easily understand this result. In extreme cases, when this graph is a fully connected graph, the time complexity will be `O(n^2)`. It is easy to explain, because every time you visit a node, you will visit the adjacent nodes. A node is connected to all nodes, so the time spent on a node is n, and the time spent on n nodes is n^2. Because we use a queue to store the nodes that need to be traversed next, the space complexity is `O(n)`.






![](../../Pictures/qrcode.jpg)