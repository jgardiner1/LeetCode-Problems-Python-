"""
125. Valid Palindrome
Solved
Easy
Topics
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


class Solution:
    def processString(self, s: str) -> str:
        s = s.lower()
        sCopy = ""
        for char in s:
            if char.isalnum():
                sCopy += char

        return sCopy

    def isPalindrome(self, s: str) -> bool:
        s = self.processString(s)

        isEven = True if len(s) % 2 == 0 else False
        palindrome = True

        y = len(s) - 1

        for x in range(len(s)):
            if y - x == 1 and isEven:
                if s[x] != s[y]:
                    palindrome = False
                    break

            if s[x] != s[y]:
                palindrome = False
                break

            y -= 1

        return palindrome


sol1 = Solution()
print(sol1.isPalindrome("rac  e  ^%&   ca&^*r*&^"))
