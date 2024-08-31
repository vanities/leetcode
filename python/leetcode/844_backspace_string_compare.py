# https://leetcode.com/problems/backspace-string-compare/description/
"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".



Constraints:

    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.



Follow up: Can you solve it in O(n) time and O(1) space?

"""

# this was my naive way to do it, you could use pop() as well instead of string slicing


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if s == t:
            return True
        return self.generate_new_string(s) == self.generate_new_string(t)

    def generate_new_string(self, s: str) -> str:
        new_s = ""
        for char in s:
            if char == "#":
                new_s = new_s[:-1]
            else:
                new_s += char
        return new_s
