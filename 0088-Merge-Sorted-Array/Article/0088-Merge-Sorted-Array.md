# LeetCode Problem No. 88: Merging two sorted arrays

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 88 on LeetCode: Merge two ordered arrays. The difficulty of the question is Easy

### Title description

Given two ordered integer arrays *nums1* and *nums2*, please merge *nums2* into *nums1* to make *nums1* an ordered array.

**illustrate:**

- Initialize *nums1* and *nums2* with number of elements *m* and *n* respectively.
- You can assume that *nums1* has enough space (space size greater than or equal to *m* + *n*) to hold the elements in *nums2*.

**Example:**

```
enter:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

### Question analysis

It’s much easier to put this problem into reality. If you don’t believe me, take a look.

If you are the owner of a toy store, two of the shelves are filled with cars of the same shape and different sizes. The cars are arranged from small to large. Now you want to move the cars on the second shelf to the first shelf. In order to make them look intuitive to customers, these cars must be placed in an orderly manner. What would you do?

**Obviously, you don't put all the cars together and then sort them one by one and put them on the first shelf.**

You will definitely compare the sizes of the two shelf cars and move the second shelf car to the corresponding position of the first shelf.

So the question is, should we compare from the small one or the large one?

**Let’s start with a small comparison**. Now the first car on the second shelf is the smallest, so you have to move all the toys back on the first shelf one place before you can put down the car. **It seems a bit laborious**.

If we don’t want to go to great lengths, we can first move the toys on the first shelf to the third shelf, compare the second shelf with the third shelf, and put the smaller car on the first shelf. It seems that we have to move the first shelf first, and **need to occupy other space**.

**If we compare from the back**, **that is, compare the larger cars first**, now the last one on the second shelf is the largest car. I only need to take the largest car to the back of the first shelf. Isn’t it very easy? By comparing them one by one, it moves to the back of the first shelf without any effort or space. After comparing with the first shelf, I find that there is still one smallest car left on the second shelf. At this time, you will find that the first position of the first shelf is empty. We can just take it over.

The story is over. By trying these methods, you may have discovered:

> The corresponding algorithm for the first method is **' sorting after merging '**, which has a relatively large time complexity;
>
> The second method corresponds to the algorithm **' double pointer + front-to-back comparison '**
>
> - Moving the car backward has high time complexity
> - Moving to the third shelf space has high complexity
>
> The corresponding algorithm of the third method is **' double pointer + back-to-forward comparison '**, which saves time and does not take up space, perfect!

Let's talk about the specific idea of ​​**' double pointer + compare '** from back to front:

1. Set up double pointers, pointing to the last bit of the ordered array;

2. From back to front

   - Termination condition: One of the pointers no longer points to the array

   - Compare the values ​​pointed to by two pointers

   - Large or identical values ​​are placed at the end of the *num1* space (the end is filled sequentially from back to front), and the corresponding pointer is moved forward one position.
   - Repeat the above steps

3. Check after the traversal is completed

   - If the pointer pointing to *num2* is still valid, it means that there is still a minimum value in *num2* that is smaller than *num1*
   - Move these values ​​to the front of *num1*

### Animation description

<img src="../Animation/Animation.gif" alt="Animation" style="zoom:150%;" />

### Reference code
C++ Code:

```c++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=m-1, j=n-1, k=m+n-1;
        // merge
        while(i>=0 && j>=0)
        {
            if(nums1[i] > nums2[j])
            {
                nums1[k--] = nums1[i--];
            }
            else
            {
                nums1[k--] = nums2[j--];
            }
        }
        // Combine remaining nums2
        while(j>=0)
        {
            nums1[k--] = nums2[j--];
        }
    }
};
```

Java Code:

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i=m-1, j=n-1, k=m+n-1;
        // merge
        while(i>=0 && j>=0)
        {
            if(nums1[i] > nums2[j])
            {
                nums1[k--] = nums1[i--];
            }
            else
            {
                nums1[k--] = nums2[j--];
            }
        }
        // Combine remaining nums2
        while(j>=0)
        {
            nums1[k--] = nums2[j--];
        }
    }
}
```

Python Code:

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = m-1, n-1, m+n-1

        while i >= 0 and j >= 0:
            # print(i,j,k, nums1)
            # print(nums1[i], nums2[j])
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k-=1
                i-=1
            else:
                nums1[k] = nums2[j]
                k-=1
                j-=1
        while j >= 0:
            nums1[k] = nums2[j]
            k-=1
            j-=1

```

JavaScript Code:

```javascript
/**
 * JavaScript description
 *Dual pointers + from back to front
 */
var merge = function(nums1, m, nums2, n) {
    let len = m + n;
    while(m > 0 && n > 0){
        // '>=' can be compared one less time than '>' when some values ​​are the same.
        nums1[--len] = nums2[n-1] >= nums1[m-1] ? nums2[--n]: nums1[--m];
    }
    if(n > 0){
        nums1.splice(0,n,...nums2.slice(0,n));
    }
};
```

### Complexity analysis

- Time complexity: **O( m+n )**

- Space complexity: **O( 1 )**





![](../../Pictures/qrcode.jpg)
