# LeetCode Problem No. 128: Longest Contiguous Sequence

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 128 on LeetCode: The longest continuous sequence. The difficulty of the questions is Hard, and the current pass rate is 48.5%.


<br>


### Title description

Given an unsorted array of integers, find the length of the longest consecutive sequence.

The time complexity of the required algorithm is O(n).

**Example 1:**

```
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest continuous sequence is [1, 2, 3, 4]. Its length is 4.
```

<br>

### Question analysis

The question is straightforward. Give you an unsorted array and ask you to find some elements from it so that these elements can form the longest **continuous increasing sequence**. Output the length of this sequence. The order of the elements does not matter. For example:

```
[100, 4, 200, 1, 3, 2]

You can find 4, 1, 3, 2 to form a continuous increasing sequence 1, 2, 3, 4

Output this sequence length 4
```
The very straightforward idea is to sort the array and then traverse it once to find the answer. However, the difficulty of this question is that it limits the time complexity to O(n). In this way, sorting is not feasible.

This question actually has a feature, that is, this question implies the property of **connectivity**. How do you explain it? Let’s take the above example as an example:

```
[100, 4, 200, 1, 3, 2]

We enumerate the elements in the array from left to right. You can consider the enumerated elements to be valid:
............100 enumerates the first element, and there is 1 connected area at this time
......4............100 Enumerate the second element. The second element is not connected to the previous element. At this time, there are 2 connected areas.
......4............100............200 Enumerate the third element. The three elements are not connected to each other. At this time, there are 3 connected areas.
1..4......100......200 enumerates the fourth element. The four elements are not connected to each other. At this time, there are 4 connected areas.
1.34......100......200 Enumerate the fifth element. This element is connected to the second connected area before. The connected area is maintained at 4
1234......100......200 Enumerate the sixth element. This element is connected to two connected areas, and the connected areas become 3

The number of elements contained in the connected region that finally contains the most elements is the answer we want.
```

How does knowing these things help us solve problems? Regarding the issue of connectivity, the first data structure that comes to mind is **Union Lookup**. This data structure was originally designed to solve the connectivity problem, and the time complexity of its two operations, search and merge, can be approximated as O(1), so it is perfect for solving this problem.

If you can think of and search the set, then there is actually no more difficulty in this question, but what I want to say is that there is actually a more interesting solution to this question, which is to use HashMap to record the length of connected blocks covered by boundary points, or follow the example:

```
[100, 4, 200, 1, 3, 2]

We still enumerate the elements in the array from left to right. Each time we traverse, we check whether the left and right sides of the element exist and update the HashMap:
100 At this time, neither 99 nor 101 has any blocks. Map {100=1} means that the block size of 100 is 1.
4 At this time, neither 3 nor 5 has any blocks, Map {100=1, 4=1}
200 At this time, 199 and 201 do not have any blocks, Map {100=1, 4=1, 200=1}
1 At this time, neither 0 nor 2 has any blocks, Map {100=1, 4=1, 200=1, 1=1}
3 finds that 4 exists, 4 and 3 form a new block,
      The left margin of this block is 3, the right margin is 4, and the block size is 2.
      Update the block size represented by the boundary element in Map, Map {100=1, 4=2, 200=1, 1=1, 3=2}
2 It is found that the left and right boundaries exist at the same time, 1, 2, 3, 4 form a new block
      The left border of this block is 1, the right border is 4, and the block size is 4,
      Update the block size represented by the boundary element in the Map and record the current element to avoid repeated access.
      Map {100=1, 4=4, 200=1, 1=4, 3=2, 2=4}
```

It can be seen that every time we record, we only need to ensure that the block size represented by the boundary elements of the block is correct. As for the elements in the middle of the block, it does not matter, because these elements will not be accessed again.

This method is actually quite clever. It uses the elements of the hash table to extend left and right to determine the size of the block.

<br>

### Code implementation (joint search)

```java
class Solution {
    // roots are used to record the representative elements of a connected area
    private Map<Integer, Integer> roots = new HashMap<>();
    
    // counts are used to record the number of elements in a connected region
    private Map<Integer, Integer> counts = new HashMap<>();
    
    private int find(int a) {
        if (roots.get(a) == a)  {
            return a;
        }
        
        int root = find(roots.get(a));
        
        //Path compression
        roots.put(a, root);
        
        return root;
    }
    
    private void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        
        if (rootA != rootB) {
            roots.put(rootA, rootB);
            
            // Merge two connected areas and update the number of elements in the entire area
            counts.put(rootB, counts.get(rootA) + counts.get(rootB));
        }
    }
    
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        for (int i = 0; i < nums.length; ++i) {
            if (roots.containsKey(nums[i])) {
                continue;
            }
            
            roots.put(nums[i], nums[i]);
            counts.put(nums[i], 1);
            
            // Check whether adjacent elements have connected blocks
            if (roots.containsKey(nums[i] - 1) && roots.containsKey(nums[i] + 1)) {
                int root = find(roots.get(nums[i] - 1));
                
                // There are connected areas on the left and right, merge these three areas
                union(nums[i], root);
                union(root, roots.get(nums[i] + 1));
            } else if (roots.containsKey(nums[i] - 1)) {
                int root = find(roots.get(nums[i] - 1));
                
                // There is a connected area on the left, merge these two areas
                union(nums[i], root);
            } else if (roots.containsKey(nums[i] + 1)) {
                int root = find(roots.get(nums[i] + 1));
                
                // There is a connected area on the right, merge these two areas
                union(nums[i], root);
            }
        }
        
        int result = 1;
        
        // Traverse all connected blocks and find the block containing the most elements
        for (int i : counts.keySet()) {
            result = Math.max(result, counts.get(i));
        }
        
        return result;
    }
}
```

<br>

### Animation description (and search)

![](../Animation/128-1.gif)

<br>

### Code implementation (hash table)

```java
public int longestConsecutive(int[] nums) {
    if (nums == null || nums.length == 0) {
        return 0;
    }
    
    Map<Integer, Integer> distances = new HashMap<>();
    
    int result = 1;
    
    for (int num : nums) {
        if (distances.containsKey(num)) {
            continue;
        }
        
        // Find the longest distance that can be extended to the left
        int left = distances.getOrDefault(num - 1, 0);
        
        // Find the longest distance that can extend to the right
        int right = distances.getOrDefault(num + 1, 0);
        
        // Update the block size represented by the left and right boundaries at this time
        distances.put(num - left, left + right + 1);
        distances.put(num + right, left + right + 1);
        
        // There may be duplicate elements in the array. Record the current element to avoid accessing it again.
        distances.put(num, left + right + 1);

        result = Math.max(result, left + right + 1);
    }
    
    return result;
}
```

<br>

### Animation description (hash table)

![](../Animation/128-2.gif)

<br>

![](../../Pictures/qrcode.jpg)