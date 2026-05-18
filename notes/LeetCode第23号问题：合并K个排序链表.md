# LeetCode Problem No. 23: Merge K sorted linked lists

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 23 on LeetCode: Merging K sorted linked lists. The difficulty of the questions is Hard, and the current pass rate is 45.8%.

### Title description

Merge *k* sorted linked lists and return the merged sorted linked list. Please analyze and describe the complexity of the algorithm.

**Example:**

```
enter:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

**enter**

![Picture 1](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/u2jnp.jpg)

**Output**

![Picture 2](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/yc4ac.jpg)

### Question analysis

### Question Analysis 1

Here we need to integrate these *k* sorted linked lists into one sorted linked list, which means there are multiple inputs and one output, similar to the concept of a funnel.

Therefore, the concept of min-heap can be utilized. If you are not familiar with the concept of heap, you can click here to learn about it first~

Take the smallest node of each Linked List and put it into a heap, and sort it into a minimum heap. Then take out the smallest element at the top of the heap and put it into the output merged List. Then insert the next node of this node in its corresponding List into the heap, loop the above steps, and so on until all nodes have passed through the heap.

Since the size of the heap is always k and the complexity of each insertion is logk, a total of nk nodes are inserted. The time complexity is O(nklogk) and the space complexity is O(k).

### Animation demonstration

![Animation Demonstration](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/iuxmh.gif)

### Code implementation

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        //Use the heap data structure, which is the PriorityQueue in java
        PriorityQueue<ListNode> pq = new PriorityQueue<>(new Comparator<ListNode>() {
            public int compare(ListNode a, ListNode b) {
                return a.val-b.val;
            }
        });
        ListNode ret = null, cur = null;
        for(ListNode node: lists) {
            if(null != node) {
                pq.add(node);    
            }
        }
        while(!pq.isEmpty()) {
            ListNode node = pq.poll();
            if(null == ret) {
                ret = cur = node;
            }
            else {
                cur = cur.next = node;
            }
            if(null != node.next) {
                pq.add(node.next);    
            }
        }
        return ret;
    }
}
```





### Question Analysis 2

This question requires merging k ordered linked lists, and the final merged result must also be ordered. If you don't have a clue at the beginning, you can start simple: **Merge two ordered linked lists**.

Merge two ordered linked lists: Merge two ordered linked lists into a new ordered linked list and return it. The new linked list is formed by concatenating all the nodes of the two given linked lists.

**Example:**

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

Just follow the description of this question: create a new linked list, compare the element values ​​in the two original linked lists, and link the smaller one to the new linked list. One thing to note is that since the lengths of the two input linked lists may be different, eventually one linked list will complete the insertion of all elements first, and the other unfinished linked list will be directly linked to the end of the new linked list.

So the code implementation is easy to write:

```java
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        //Create a new linked list
        ListNode dummyHead = new ListNode(0);
        ListNode cur = dummyHead;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                cur.next = l1;
                cur = cur.next;
                l1 = l1.next;
            } else {
                cur.next = l2;
                cur = cur.next;
                l2 = l2.next;
            }
        }
        // Note: When a linked list is empty, connect to another linked list directly.
        if (l1 == null) {
            cur.next = l2;
        } else {
            cur.next = l1;
        }
        return dummyHead.next;
    }
```



Now back to the original question: merging K sorted linked lists.

The difference between **Merge K sorted linked lists** and **Merge two ordered linked lists** lies in the number of ordered linked lists to operate, so it is completely possible to merge K sorted linked lists according to the above code idea.

Here you can refer to the divide and conquer idea of ​​**Merge Sort**, first divide these K linked lists into two K/2 linked lists, process their merger, and then continue to divide down until it is divided into tasks with only one or two linked lists, and start merging.

![Merge-Divide and Conquer](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/74ush.gif)

### Code implementation

According to the animation above, the implementation code is very simple and easy to understand. Divide first until it can no longer be divided, and then start merging.

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists){
        if(lists.length == 0)
            return null;
        if(lists.length == 1)
            return lists[0];
        if(lists.length == 2){
           return mergeTwoLists(lists[0],lists[1]);
        }

        int mid = lists.length/2;
        ListNode[] l1 = new ListNode[mid];
        for(int i = 0; i < mid; i++){
            l1[i] = lists[i];
        }

        ListNode[] l2 = new ListNode[lists.length-mid];
        for(int i = mid,j=0; i < lists.length; i++,j++){
            l2[j] = lists[i];
        }

        return mergeTwoLists(mergeKLists(l1),mergeKLists(l2));

    }
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;

        ListNode head = null;
        if (l1.val <= l2.val){
            head = l1;
            head.next = mergeTwoLists(l1.next, l2);
        } else {
            head = l2;
            head.next = mergeTwoLists(l1, l2.next);
        }
        return head;
    }
}
```



![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/jhykq.gif)