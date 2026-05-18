# LeetCode Problem No. 445: Adding Two Numbers II

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronize personal blog: www.zhangxiaoshuai.fun


```txt
Difficulty: medium Current pass rate: 57.2%
Topic description:
	You are given two non-empty linked lists to represent two non-negative integers. The highest digit of the number is at the beginning of the linked list.
	Each of their nodes stores only one digit. Adding these two numbers returns a new linked list.
	You can assume that neither number will start with a zero other than the number 0.

Example:
	Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
	Output: 7 -> 8 -> 0 -> 7
```

<!-- more -->

Obviously, the two given "numbers" are arranged in order from high to low from left to right. According to custom, we need to reverse the linked list and then add them, and then reverse the resulting linked list and return.

So the order problem is solved, but there is still one problem:

**It is possible to add two one-digit numbers to produce a two-digit number, but our node cannot store a two-digit number. If a carry occurs, we need to save the carry, and then add the carry to the result of the addition of the next two numbers. **

**The following is a GIF illustration:**

![Solution 1](../Animation/Animation01.gif)

**Then let’s try writing this version of the code first:**

Because the function of linked list reversal is used three times in the entire calculation, we can extract this function separately and write a method. (The method is relatively simple, just attach the code directly without going into details)

```java
//Reverse linked list
private ListNode reverseListNode(ListNode head){
    if(head == null) return null;
    ListNode prev = null;
    while (head != null) {
        ListNode next = head.next;
        head.next = prev;
        prev = head;
        head = next;
    }
    return prev;
}
```

To return the result of adding two linked lists, we need a new linked list to store this result. The value of the dummy node is arbitrary, because what we ultimately return is the chat linked list connected behind it.

We need to initialize **addOne** (representing carry) to 0

```java
//Add the numbers of each node in the two linked lists
private ListNode add(ListNode l1, ListNode l2){
    if (l1 == null && l2 == null) return null;
    ListNode dummy = new ListNode(0);
    ListNode temp = dummy;
    int addOne = 0;
    while (l1 != null || l2 != null || addOne != 0) {
        int val1 = l1 == null ? 0 : l1.val;
        int val2 = l2 == null ? 0 : l2.val;
        int sum = val1 + val2 + addOne;
        temp.next = new ListNode(sum%10);
        temp = temp.next;
        addOne = sum / 10;
        if (l1 != null) l1 = l1.next;
        if (l2 != null) l2 = l2.next;
    }
    return dummy.next;
}
```

Ok, then we now only need to call these two methods in the specified method and pass the corresponding parameters to get what we want.

```java
public static ListNode addTwoNumbers(ListNode l1, ListNode l2){
    ListNode node1 = reverseListNode(l1);
    ListNode node2 = reverseListNode(l2);
    return reverseListNode(add(node1,node2));
}
```

If you think the above solution is too simple, let’s take a look at the advanced version:

**What should I do if the input linked list cannot be modified? In other words, you cannot flip nodes in the list. **
Then the "reverse linked list" method we used above cannot be used again.
First of all, we should make it clear that the "reverse linked list" method appears to solve the problem of the order of "numbers" in the linked list. So is this the only way to get the correct order of numbers?
We also have a data structure we can rely on: the stack. The characteristic of the stack is "**first in, last out**"

**Algorithm idea:** First push the numbers of the two linked lists into two stacks respectively, and then pop up the numbers on the top of the two stacks each time and add them. The node added for the first time points to the null node. Each time the head node is updated, the subsequent nodes point to the head node of the new linked list in turn. Then in the end we can get the same result as the above solution.

**Solution 2 diagram:**

![Solution 2](../Animation/Animation02.gif)

**Code:**

```java
public static ListNode addTwoNumbers(ListNode l1, ListNode l2){
    Stack<Integer> s1 = new Stack<>();
    Stack<Integer> s2 = new Stack<>();
    while (l1 != null) {
      s1.push(l1.val);
      l1 = l1.next;
    }
    while (l2 != null) {
      s2.push(l2.val);
      l2 = l2.next;
    }
    int addOne = 0;//carry
    ListNode head = null;
   	while (!s1.isEmpty() || !s2.isEmpty() || addOne != 0) {
      int sum = addOne;
      sum += s1.isEmpty() ? 0 : s1.pop();
      sum += s2.isEmpty() ? 0 : s2.pop();
      ListNode temp = new ListNode(sum%10);
      temp.next = head;
      head = temp;
      addOne = sum/10;
    }
    return head;
  }
```

![](../../Pictures/qrcode.jpg)
