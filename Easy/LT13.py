#Roman to Integer
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
'''
IV 4,  IX 9, XL 40, XC 90, CD 400, CM 900
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        str_len = len(s)
        i = 0
        while i < str_len - 1:
            if s[i] == 'I':
                if s[i + 1] == 'V':
                    count += 4
                    i += 2
                elif s[i + 1] == 'X':
                    count += 9
                    i += 2
                else:
                    count += 1
                    i += 1
            elif s[i] == 'X':
                if s[i + 1] == 'L':
                    count += 40
                    i += 2
                elif s[i + 1] == 'C':
                    count += 90
                    i += 2
                else:
                    count += 10
                    i += 1
            elif s[i] == 'C':
                if s[i + 1] == 'D':
                    count += 400
                    i += 2
                elif s[i + 1] == 'M':
                    count += 900
                    i += 2
                else:
                    count += 100
                    i += 1
            elif s[i] == 'V':
                count += 5
                i += 1
            elif s[i] == 'L':
                count += 50
                i += 1
            elif s[i] == 'D':
                count += 500
                i += 1
            elif s[i] == 'M':
                count += 1000
                i += 1
        if i < str_len :
            if s[i] == 'I':
                count += 1
            if s[i] == 'V':
                count += 5
            if s[i] == 'X':
                count += 10
            if s[i] == 'L':
                count += 50
            if s[i] == 'C':
                count += 100
            if s[i] == 'D':
                count += 500
            if s[i] == 'M':
                count += 1000
        return count

s = Solution()
print(s.romanToInt("MCMXCIV"))