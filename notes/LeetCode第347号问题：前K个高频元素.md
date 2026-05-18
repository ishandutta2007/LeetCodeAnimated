# LeetCode Problem No. 347: Top K High Frequency Elements

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The topic shared today comes from question No. 347 on LeetCode: the first K high-frequency elements. The difficulty level of the questions is Medium, and the current passing rate is 56.9%.

## Title description

Given a non-empty integer array, return the top k elements with the highest frequency.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**illustrate:**

- You can assume that the given k is always reasonable and 1 ≤ k ≤ the number of distinct elements in the array.
- The time complexity of your algorithm must be better than O(n log n) , where n is the size of the array.

### Question analysis

### Solution 1: Rough sorting method

The simplest and crudest idea is to use a sorting algorithm to sort the elements from high to low frequency, and then take the top k elements.

The following ten sorting algorithms are available for you to choose from!

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/qya5e.png)

It can be found that using conventional methods such as bubble, selection, and even quick sort do not meet the requirements of the question. Their time complexity is greater than or equal to O(n log⁡n), and the question requires that the time complexity of the algorithm must be better than O(n log n).

#### Complexity analysis

- **Time complexity**: O(nlogn), n represents the array length. First, traverse the array to count the frequency of elements. The time complexity of this series of operations is O(n); then, the time complexity of the sorting algorithm is O(nlogn); therefore, the overall time complexity is O(nlogn).
- **Space complexity**: O(n), in the most extreme case (different for each element), the Map used to store elements and their frequencies needs to store n key-value pairs.

### Solution 2: Minimum heap

The question ultimately needs to return the first k elements with the highest frequency. It can be thought of that with the help of a data structure such as a heap, elements after k frequencies do not need to be processed, further optimizing the time complexity.

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/nloow.jpg)

The specific operations are:

- Use **hash table** to establish a mapping between numbers and their occurrence times, and traverse the array to count the frequency of elements
- Maintain a min-heap with k elements
- Compare the new element with the top element of the heap (the element with the smallest frequency in the heap) every time
- If the frequency of the new element is greater than the element at the top of the heap, pop the element at the top of the heap and add the new element to the heap
- Finally, the k elements in the heap are the top k high-frequency elements



![The elements in the heap are the top k elements with the highest frequency](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/xged1.gif)

The code is as follows:

```java
class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        // Use a dictionary to count the number of occurrences of each element. The element is the key and the number of occurrences of the element is the value.
        HashMap<Integer,Integer> map = new HashMap();
        for(int num : nums){
            if (map.containsKey(num)) {
               map.put(num, map.get(num) + 1);
             } else {
                map.put(num, 1);
             }
        }
        // Traverse the map and use the minimum heap to save the k elements with the highest frequency
        PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return map.get(a) - map.get(b);
            }
        });
        for (Integer key : map.keySet()) {
            if (pq.size() < k) {
                pq.add(key);
            } else if (map.get(key) > map.get(pq.peek())) {
                pq.remove();
                pq.add(key);
            }
        }
        //Remove elements from the min-heap
        List<Integer> res = new ArrayList<>();
        while (!pq.isEmpty()) {
            res.add(pq.remove());
        }
        return res;
    }
}

```

#### Complexity analysis

- **Time complexity**: O(nlogk), n represents the length of the array. First, traverse the array to count the frequency of elements. The time complexity of this series of operations is O(n); then, traverse the map used to store the frequency of elements. If the frequency of the element is greater than the top element in the minimum heap, delete the top element and add the element to the heap. **The number of maintained heaps here is k**, so the time complexity of this series of operations is O(nlogk); therefore, the total time complexity is O(nlog⁡k).
- **Space complexity**: O(n). In the worst case (each element is different), map needs to store n key-value pairs, and the priority queue needs to store k elements. Therefore, the space complexity is O(n).



### Solution 3: Bucket sorting method

First, still use the hash table to count the frequencies. After the statistics are completed, create an array and use the frequencies as the array subscripts. For sets of numbers with different frequencies, just store them in the corresponding array subscripts.

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/6tge2.jpg)

The code is implemented as follows:

```java
//Solve the "top K high-frequency elements" based on bucket sorting
class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        List<Integer> res = new ArrayList();
        // Use a dictionary to count the number of occurrences of each element. The element is the key and the number of occurrences of the element is the value.
        HashMap<Integer,Integer> map = new HashMap();
        for(int num : nums){
            if (map.containsKey(num)) {
               map.put(num, map.get(num) + 1);
             } else {
                map.put(num, 1);
             }
        }
        
        //Bucket sorting
        //Use frequency as an array subscript. For sets of numbers with different frequencies, store them in the corresponding array subscripts.
        List<Integer>[] list = new List[nums.length+1];
        for(int key : map.keySet()){
            // Get the number of occurrences as a subscript
            int i = map.get(key);
            if(list[i] == null){
               list[i] = new ArrayList();
            } 
            list[i].add(key);
        }
        
        // Traverse the array in reverse order to get the order of appearance from largest to smallest
        for(int i = list.length - 1;i >= 0 && res.size() < k;i--){
            if(list[i] == null) continue;
            res.addAll(list[i]);
        }
        return res;
    }
}
```

#### Complexity analysis

- **Time complexity**: O(n), n represents the length of the array. First, traverse the array to count the frequency of elements. The time complexity of this series of operations is O(n); the number of buckets is n + 1, so the time complexity of bucket sorting is O(n); therefore, the total time complexity is O(n).
- **Space Complexity**: Obviously O(n)



