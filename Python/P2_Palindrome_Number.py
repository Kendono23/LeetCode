# With String

def isPalindrome(x):
  return str(x)[::-1] == str(x)

#Without String

def isPalindrome(x):
  rem = 0
  rev = 0
  negative=False

  if (x < 0):
    x = -x
    temp = x
    negative = True
  else:
    temp = x

while (x != 0):
  rem = int(x % 10)
  rev = (rev * 10) + (rem)
  x = int(x/10)

if negative:
  x = -temp
  return True if (-rev == -x) else False
else:
  x = temp
  return True if (rev == x) else False

"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
