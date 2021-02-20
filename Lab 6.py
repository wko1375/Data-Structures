def maximum(lst, index):
    if index == len(lst)-1:
        if(lst[index] < lst[index+1]):
            num = lst[index+1]
            return num
        else:
            num = lst[index]
            return num
    else:
        if(lst[index] > lst[index+1]):
            num = lst[index]
        else:
            num = maximum(lst, index+1)
        return num

print(maximum([4,33,500,3,4,5000], 0))
