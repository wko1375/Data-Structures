#Question 5a

def count_lowercase(s, low, high):
    count = 0
    if low == high:
        if s[high].islower():
            count += 1
        return count
    else:
        if s[low].islower():
            count += 1
        count += int(count_lowercase(s, low+1, high))
        return count

#Question 5b

def is_number_of_lowercase_even(s, low, high):
    string = ""
    if low == high:
        if s[high].islower():
            return len(s[high]) % 2 == 0
    if low + 1 == high:
        if s[high].islower():
            string += s[high]
        if s[low].islower():
            string += s[low]
        return len(string) % 2 == 0
    else:
        if s[low].islower():
            string += s[low]
        string += str(is_number_of_lowercase_even(s,low+1,high))
        return len(string) % 2 == 0
