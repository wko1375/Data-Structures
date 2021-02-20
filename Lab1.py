def add_binary(num1_str, num2_str):
    power1 = len(num1_str)
    power2 = len(num2_str)
    sum1 = 0
    sum2 = 0
    for number in num1_str:
         if number == '1':
            sum1 += 2^power1
         power1 -= 1
         print(sum1)
    for number in num2_str:
        if number == '1':
            sum2 += 2^power2
        power2 -= 1
        print(sum2)
    finalsum = sum1+sum2

print(add_binary('11','1'))
