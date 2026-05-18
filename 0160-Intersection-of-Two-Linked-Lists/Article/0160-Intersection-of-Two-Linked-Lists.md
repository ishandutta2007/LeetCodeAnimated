The question comes from question No. 160 on LeetCode: Intersecting linked lists. The difficulty level of the questions is Easy, and the current pass rate is 54.4%.
##Title description
Write a program to find the starting node where two singly linked lists intersect.
Such as the following two linked lists:
![LeetCode illustration|160.Intersecting linked list](https://upload-images.jianshu.io/upload_images/1840444-b62ea7eae24bf88e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
The intersection begins at node c1.
Example 1:
![LeetCode illustration|160. Intersecting linked list example 1](https://upload-images.jianshu.io/upload_images/1840444-59acbe2575d138b2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input explanation: The value of the intersection node is 8 (note that it cannot be 0 if the two linked lists intersect). Counting from the beginning of their respective lists, linked list A is [4,1,8,4,5] and linked list B is [5,0,1,8,4,5]. In A, there are 2 nodes before the intersection node; in B, there are 3 nodes before the intersection node.
```
Notice:
- If the two linked lists have no intersection, return null.
- After returning the result, the two linked lists must still maintain their original structure.
- It can be assumed that there are no loops in the entire linked list structure.
- The program tries to meet O(n) time complexity and only uses O(1) memory.

##Question analysis
In order to meet the time complexity and space complexity requirements of the question, we can use the double pointer method.
- Create two pointers pA and pB pointing to the head nodes headA and headB of the linked list respectively.
- When pA reaches the end of the linked list, relocate it to the head node headB of linked list B. Similarly, when pB reaches the end of the linked list, relocate it to the head node headA of linked list A.
- When pA and pB are equal, it is the first node where the two linked lists intersect.
This is actually equivalent to putting two linked lists together. The pA pointer is a new linked list traversal composed of the B linked list after the A linked list, and the pB pointer is a new linked list traversal composed of the A linked list after the B linked list. Give a simple example:
A linked list: {1,2,3,4}
B linked list: {6,3,4}
pA traverses the newly spliced ​​linked list {1,2,3,4,6,3,4}
pB traverses the newly spliced ​​linked list {6,3,4,1,2,3,4}

##Animation understanding

![](../Animation/Animation.gif)

##Code implementation
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *pA = headA;
        ListNode *pB = headB;
        while(pA != pB){
            if(pA != NULL){
                pA = pA->next;
            }else{
                pA = headB;
            }
            if(curB != NULL){
                pB = pB->next;
            }else{
                pB = headA;
            }
        }
        return pA;
    }
};
```
##Complexity analysis
- Time complexity: O(m+n).
- Space complexity: O(1)
