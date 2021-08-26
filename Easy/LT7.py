# Reverse Integer
#Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.



class Solution:
    def reverse(self, x: int) -> int:

        temp = 1
        if(x < 0):
            temp = -1
            x = x * -1
        y = 0
        while x != 0:
            y = y*10 + x % 10
            x = x//10
        if x < 0:
            return y * -1
        if(y < -2**31) or y > (2**31 -1):
            return 0
        return y * temp



s = Solution()
print(s.reverse(1534236469))


