def checkPalindrome(str):
    str_len = len(str)
    if str_len == 0:
        #print("Enter a String")
        return "Enter a String"
    start = 0
    end = str_len - 1
    mid = (start + end)/2
    while start < mid:
        if(str[start] != str[end]):
            return "Not a Palindrome"
        else:
            start += 1
            end -= 1
    return "Palindrome"

def checkPalindromeNumber(num):
    num2 = num
    temp = 0
    while num2 != 0:
        unit = num2 % 10
        temp = temp * 10 + unit
        num2 = num2//10
    if temp == num:
        return True
    else:
        return False

def isPalindrome(x):
    if x < 0:
        x = x * -1
    num2 = x
    temp = 0
    while num2 != 0:
        unit = num2 % 10
        temp = temp * 10 + unit
        num2 = num2//10
    if temp == x:
        return True
    else:
        return False

print(checkPalindrome(""))
print(checkPalindromeNumber(1001001))
print(isPalindrome(121))
