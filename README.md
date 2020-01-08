# Hackerrank-Challenges
## 1. 
Given a  2D Array, :

1 1 1 0 0 0  
0 1 0 0 0 0  
1 1 1 0 0 0  
0 0 0 0 0 0  
0 0 0 0 0 0  
0 0 0 0 0 0  
  
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c  
  d  
e f g  
  
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every ## hourglass in , then print the maximum hourglass sum.

For example, given the 2D array:

-9 -9 -9  1 1 1   
 0 -9  0  4 3 2  
-9 -9 -9  1 2 3  
 0  0  8  6 6 0  
 0  0  0 -2 0 0  
 0  0  1  2 4 0  
   
We calculate the following  hourglass values:

-63, -34, -9, 12,   
-10, 0, 28, 23,   
-27, -11, -2, 10,   
9, 17, 25, 18  
  
Our highest hourglass value is  from the hourglass:  

0 4 3  
  1  
8 6 6  
  

Sample Input

1 1 1 0 0 0  
0 1 0 0 0 0  
1 1 1 0 0 0  
0 0 2 4 4 0  
0 0 0 2 0 0  
0 0 1 2 4 0  

Sample Output

19  

## 2.

A left rotation operation on an array shifts each of the array's elements  1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

Given an array a of n integers and a number, d , perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):

An array of integers a .
An integer d, the number of rotations.
Input Format

The first line contains two space-separated integers n and d, the size of a and the number of left rotations you must perform.
The second line contains n space-separated integers a[i].

Output Format

Print a single line of n space-separated integers denoting the final state of the array after performing d left rotations.

Sample Input

5 4  
1 2 3 4 5  

Sample Output

5 1 2 3 4  
