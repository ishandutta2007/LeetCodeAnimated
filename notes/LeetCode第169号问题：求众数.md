# [More than half of the numbers in the array] Three solutions, the last solution is awesome!

The topic shared today comes from question No. 169 on LeetCode: finding the mode (finding more than half of the numbers in the array). The difficulty of the questions is Easy, and the current passing rate is 45.8%.

The last solution is **Cool**! ! !

#Problem description

Given an array of size n, find its mode. The mode refers to the elements that appear more than ⌊ n/2 ⌋ in the array.

You can assume that arrays are non-empty and that there is always a mode for a given array.

**Example 1:**

```
Input: [3,2,3]
Output: 3
```

**Example 2:**

```
Input: [2,2,1,1,1,2,2]
Output: 2
```

# Question analysis

The meaning of the question is easy to understand: you are given an array in which a number appears more than half the time. You have to find this number and return it.

## Solution 1: Violent solution

Iterate through the entire array and count the number of occurrences of each number.

Finally, return elements that appear more than half the time.

### Animation description

![](https://raw.githubusercontent.com/MisterBooo/myBlogPic/master/20190626114223.gif)

### **Code Implementation**

```java
class Solution {
    public int majorityElement(int[] nums) {
        int majorityCount = nums.length/2;

        for (int num : nums) {
            int count = 0;
            for (int elem : nums) {
                if (elem == num) {
                    count += 1;
                }
            }
            if (count > majorityCount) {
                return num;
            }

        }  
    }
}
```

### Complexity analysis

**Time complexity**: O(n<sup>2</sup>)

The brute force solution consists of two nested for loops, with n iterations at each level, so the time complexity is O(n<sup>2</sup>).

**Space complexity**: O(1)

The brute force solution does not allocate any additional space proportional to the size of the input, so the space complexity is O(1).

## Solution 2: Hash table method

This problem can be regarded as a search problem. For search problems, a **hash table** with a time complexity of O(1) can often be used to optimize by exchanging space for time.

Directly traverse the entire **array**, store each number (num) and the number of times it appears (count) in the **hash table**, and determine whether the number of times it appears is the largest, dynamically update maxCount, and finally output maxNum.

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/bbjtv.gif)

### Code implementation

```java
class Solution {
    public int majorityElement(int[] nums) {
    Map<Integer, Integer> map = new HashMap<>();
    // maxNum represents the element, maxCount represents the number of times the element appears
    int maxNum = 0, maxCount = 0;
    for (int num: nums) {
      int count = map.getOrDefault(num, 0) + 1;
      map.put(num, count);
      if (count > maxCount) {
        maxCount = count;
        maxNum = num;
      }
    }
    return maxNum;
  }
}
```

### Complexity analysis

**Time complexity**: O(n)

There is a total loop, and the insertion into the hash table is constant time, so the time complexity is O(n).

**Space complexity**: O(n)

The hash table takes up O(n) extra space, so the space complexity is O(n).

## Solution three: Moore voting method

Let's review the topic again: Find more than half of the numbers in the array, which means that the sum of the number of occurrences of other numbers in the array is less than the number of occurrences of this number.

That is, if the mode is recorded as `+1` and the other numbers are recorded as `−1`, and they are all added up, the sum is greater than 0.

So it works like this:

* Set two variables candidate and count. **candidate** is used to save a certain number traversed in the array. **count** represents the number of occurrences of the current number. Initially, **candidate** is saved as the first number in the array, and **count** is 1
* Traverse the entire array
* If the number is the same as the number saved by the previous **candidate**, then **count** is increased by 1
* If the number is different from the number previously saved by **candidate**, **count** is decremented by 1
* If the number of occurrences **count** becomes 0, **candidate** changes and is saved as the currently traversed number, and at the same time resets **count** to 1
* After traversing all the numbers in the array, you can get the result

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/8wyb2.gif)

### Code implementation

```java
class Solution {
    public int majorityElement(int[] nums) {
    int candidate = nums[0], count = 1;
    for (int i = 1; i < nums.length; ++i) {
      if (count == 0) {
        candidate = nums[i];
        count = 1;
      } else if (nums[i] == candidate) {
        count++;
      } else{
        count--;
      }
    }
    return candidate;
  }
}
```

### Complexity analysis

**Time complexity**: O(n)

There is only one loop in total, so the time complexity is O(n).

**Space complexity**: O(1)

Only a constant level of extra space is required, so the space complexity is O(1).