"""
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
"""

from curses.ascii import isupper


class Solution:
    def toLowerCase(self, s: str) -> str:
        #return s.lower()
        output = []
        for c in s:
            if c.isupper():
                output.append(chr(ord(c)+32))
            else:
                output.append(c)
        return "".join(output)