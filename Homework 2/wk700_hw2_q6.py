def two_sum(lst, target):
    low = 0
    high = len(lst)-1
    while(low<high):
        if lst[low] + lst[high] == target:
            return "(" + str(low) + ", " + str(high) + ")"
        if lst[low] + lst[high] > target:
            high -= 1
        if lst[low] + lst[high] < target:
            low += 1
    return None

print(two_sum([2,8,22,36,46,70],83))
