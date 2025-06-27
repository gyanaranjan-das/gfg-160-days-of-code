**1.Second Largest**

Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]

Output: 34

Explanation: The largest element of the array is 35 and the second largest element is 34.

Input: arr[] = [10, 5, 10]

Output: 5

Explanation: The largest element of the array is 10 and the second largest element is 5.

Input: arr[] = [10, 10, 10]

Output: -1

Explanation: The largest element of the array is 10 and the second largest element does not exist.

Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

**🔢 Problem:**
Given an array of positive integers, find the second largest number.

But! If second largest doesn't exist (like all elements are equal), return -1.

Also, second largest ≠ largest. No cheating by repeating.

**🧠 Concept (Mathematical + Real-Life Analogy):**
Imagine you're a teacher watching a running race:

The fastest student = largest number

The second fastest = second largest

You don’t want:

1st and 2nd to be the same person (i.e., no duplicates)

Someone coming in 1st multiple times to count for both slots

So what do you do?

Keep track of the winner (largest)

Keep track of the runner-up (second_largest)

Keep checking every student (element) one by one.

**✅ Algorithm (Simplest Flow)**
Step-by-Step:
1. Initialize two variables:
  largest = -1
  second_largest = -1
2. Loop through each number in the array:

  - If the number is bigger than largest:

    - Now second_largest becomes largest (because the old champ is now runner-up)

    - And largest becomes the new number

  - Else if the number is less than largest but more than second_largest:

    - Then that number is the new second_largest

3. Done looping? Return second_largest
