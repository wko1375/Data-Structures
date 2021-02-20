def is_palindrome(strang, low, high):
    if high-low <= 2:
        if strang[low] == strang[high]:
            return True
        else:
            return False
    if strang[low] == strang[high]:
        return is_palindrome(strang, low+1, high-1)
    else:
        return False



print (is_palindrome("ottotto", 0,6))
