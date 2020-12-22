def square(num):
    # return the square of the number
    return num*num

def max_list(num_list):
    # return the maximum number of the list
    max = num_list[0]
    for num in num_list:
        if num>max:
            max=num
    return max

def min_list(num_list):
    # return the minimum number of the list
    min = num_list[0]
    for num in num_list:
        if num<min:
            min=num
    return min

def sum_list(num_list):
    # return the sum of all numbers in the list
    sum=0
    for num in num_list:
        sum=sum+num
    return sum


