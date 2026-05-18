# LeetCode Problem No. 21: Merge two ordered linked lists

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 21 on LeetCode: Merge two ordered linked lists. The difficulty of the questions is Easy, and the current passing rate is 45.8%.

### Title description

Merge two sorted linked lists into a new sorted linked list and return. The new linked list is formed by concatenating all the nodes of the two given linked lists.

**Example:**

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

### Question analysis

#### General plan

##### 1.1 Problem-solving ideas

> (1) Process the situation where the empty linked list exists. If pHead1 is empty, pHead2 will be returned. If pHead2 is empty, pHead1 will be returned. (Both are empty, this situation has been intercepted when pHead1 is empty)
> (2) Determine the first node when there are no empty linked lists in the two linked lists, compare the values ​​of the first nodes of linked list 1 and linked list 2, and save the node with the smaller value as the first node after the merger. And move the linked list whose first node is the smallest one element backward.
> (3) Continue to select small values ​​among the remaining elements, connect them to the back of the first node, and continue to connect nodes with small values ​​to the back of the first node until a certain linked list is empty.
> (4) When the lengths of the two linked lists are inconsistent, that is, one of the linked lists is empty after the comparison is completed. At this time, the remaining elements of the other linked list need to be connected to the back of the first node.

##### 1.2 Code implementation

```c++
ListNode* mergeTwoOrderedLists(ListNode* pHead1, ListNode* pHead2){
    ListNode* pTail = NULL;//Points to the last node of the new linked list pTail->next to connect
    ListNode* newHead = NULL;//Points to the first node of the merged linked list
    if (NULL == pHead1){
        return pHead2;
    }else if(NULL == pHead2){
        return pHead1;
    }else{
        //Determine the head pointer
        if ( pHead1->data < pHead2->data){
            newHead = pHead1;
            pHead1 = pHead1->next;//points to the second node of the linked list
        }else{
            newHead = pHead2;
            pHead2 = pHead2->next;
        }
        pTail = newHead;//points to the first node
        while ( pHead1 && pHead2) {
            if ( pHead1->data <= pHead2->data ){
                pTail->next = pHead1;  
                pHead1 = pHead1->next;
            }else {
                pTail->next = pHead2;
                pHead2 = pHead2->next;
            }
            pTail = pTail->next;

        }
        if(NULL == pHead1){
            pTail->next = pHead2;
        }else if(NULL == pHead2){
            pTail->next = pHead1;
        }
        return newHead;
}
```

#### 2 Recursive scheme

##### 2.1 Problem-solving ideas

> (1) Process the situation where the empty linked list exists. If pHead1 is empty, pHead2 will be returned. If pHead2 is empty, pHead1 will be returned.
> (2) Compare the sizes of the first nodes of the two linked lists to determine the position of the head node
> (3) After the head node is determined, continue to select the next node among the remaining nodes to link to the node selected in the second step, and then continue to repeat steps (2) (3) until the linked list is empty.

##### 2.2 Code implementation

```c++
ListNode* mergeTwoOrderedLists(ListNode* pHead1, ListNode* pHead2){
    ListNode* newHead = NULL;
    if (NULL == pHead1){
        return pHead2;
    }else if(NULL ==pHead2){
        return pHead1;
    }else{
        if (pHead1->data < pHead2->data){
            newHead = pHead1;
            newHead->next = mergeTwoOrderedLists(pHead1->next, pHead2);
        }else{
            newHead = pHead2;
            newHead->next = mergeTwoOrderedLists(pHead1, pHead2->next);
         }
        return newHead;
    }   
}
```

### 





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/1ubug.png)