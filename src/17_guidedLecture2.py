# define a doubling function that passes args by value
# function double(2) {}
# const double = (x) => {}

# FUNCTION
def double(x):   # this x is passed by value/basically copied
    return x * 2

# define a doubling function for a list of variables passed by reference


def mult2_list(l):  # this list is passed by reference
    for i in range(len(l)):  # standard for loops in python
        l[i] *= 2  # L is a pointer to a list.
# you do not need a return because it's modifying the list directly.


y = double(12)
print(y)

some_nums = [1, 2, 3, 4]
print(some_nums)
mult2_list(some_nums)
print(some_nums)


# UPER PROBLEM SOLVING METHOD

# understanding = ask tons of questions
# planning = Can you describe or create an MVP or brute force solution?
# execute = code
# repeat/reflect/refactor =  obvious

def centered_average(num):
    # find the max number of nums
    max_num = max(num)
    # find the min number
    min_num = min(num)
    # get the sum of nums
    current_sum = sum(num)
    # subtract the min and the max
    final_sum = current_sum - max_num - min_num
    # divide the value by len(nums) -2
    return final_sum // (len(num) - 2)
