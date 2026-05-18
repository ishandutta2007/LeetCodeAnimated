The question comes from question No. 540 on LeetCode: Single element in an ordered array. The difficulty of the questions is medium, and the current pass rate is 60.2%.
##Title description
Given a sorted array containing only integers, each element appears twice, except a number that appears only once. Find this number.

```
Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time complexity and O(1) space complexity.
```
##Question analysis
Let's read the question first and find out the keywords in the question "ordered array containing integers", "" element appears twice", "only one number appears once", here we can know: the number of elements in the ordered array where the element appears only once must be an odd number. This is the key to solving the problem. Because the question requires our time complexity to be O(log n), so we can use the binary search method.

## Solution 1: Binary search

First, lo and hi point to the first and last elements of the array respectively, and mid points to the middle element. At this time, we will find that the middle element and its left and right elements have the following three situations, such as: (1) 3, 3, 4, (2) 3, 4, 3, (3) 4, 3, 3. For the second case, we immediately found the element that only appeared once. So for the first case mid=mid-1, then divide the array into two with (3, 3) as the boundary, and determine the number of elements on both sides, because we know that the number of elements in the ordered array where the element that only appears once must be an odd number, if the number of elements on the left side of (3, 3) is an odd number , then the number that only appears once is on the left, then move hi to the mid-2 position, that is, the left side of (3, 3). If the number of elements on the right side of (3, 3) is an odd number, then the number that only appears once is on the right, then move lo to the mid+1 position, that is, the right side of (3, 3). The third case is analyzed similarly to the second case. If the left side of (3, 3) is an odd number, then hi moves to the mid-1 position. If the right side of (3, 3) is an odd number, lo moves to the mid+2 position. And so on, until lo=hi, the search ends.

##Animation understanding

![](../Animation/Animation.gif)

##Code implementation
```
class Solution {
    public int singleNonDuplicate(int[] nums) {
        int lo = 0;
        int hi = nums.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            boolean halvesAreEven = (hi - mid) % 2 == 0;
            if (nums[mid + 1] == nums[mid]) {
                if (halvesAreEven) {
                    lo = mid + 2;
                } else {
                    hi = mid - 1;
                }
            } else if (nums[mid - 1] == nums[mid]) {
                if (halvesAreEven) {
                    hi = mid - 2;
                } else {
                    lo = mid + 1;
                }
            } else {
                return nums[mid];
            }
        }
        return nums[lo];
    }
}
```
##Complexity analysis

- Time complexity: O(log n), in each loop iteration we reduce the search space by half.
- Space complexity: O(1), only constant space is used

##Solution 2: Perform binary search only on even indexes

We find that when the mid index is an even number, the number of array elements on both sides of mid is even. If the mid index is an odd number, the number of array elements on both sides of mid is an odd number. When the mid index is an even number, if mid=mid+1, which is the third case of solution 1, because the number on the right side of mid is an even number, so the number from mid+2 to hi is an odd number, then the element that only appears once must be on the right side of mid, and lo is moved to the mid+2 position. If mid! = mid+1, then the element that appears only once must be to the left of mid or is mid. If the mid index is an odd number, then in order to ensure that the mid index is an even number, we move the mid to the mid-1 position, so that the mid index becomes an even number. Repeat the above operation until hi=lo and the search ends.

##Animation understanding

![](../Animation/2.gif)

##Code implementation

```
class Solution {
    public int singleNonDuplicate(int[] nums) {
        int lo = 0;
        int hi = nums.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (mid % 2 == 1) mid--;
            if (nums[mid] == nums[mid + 1]) {
                lo = mid + 2;
            } else {
                hi = mid;
            }
        }
        return nums[lo];
    }
}
```

##Complexity analysis

- Time complexity: O(log2/n)=O(log n), we only perform a binary search on half of the elements.
- Space complexity: O(1), only constant space is used
