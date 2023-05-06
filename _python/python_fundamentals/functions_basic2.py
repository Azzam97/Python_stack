# a function that returns a list counted down from the argument to 0
def countdown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list
print(countdown(5))

# a function that recieves 2 argumrnts, prints the first one and returns the second one
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

# a function that returns the sum value of the first item in the list and it's length
def summing(list):
    sum = 0
    length = len(list)
    sum = length + list[0]
    return sum
print(summing([1,2,3,4,5]))

# a function that prints the values greater than the 2nd value in a new list and the
# length of said list and if the list is smaller than 2 elemnets long the functions returns false
def greater(list):
    new_list = []
    if len(list)<2:
        return False
    else:
        for i in range(len(list)):
            if list[i]>list[1]:
                new_list.append(list[i])
    length = len(new_list)
    print(length)
    return new_list
print(greater([1,2,3,4,5,6,2,3]))
print(greater([5]))

# a function that takes 2 arguments: Size and Value, and returns a list with the length of size and all values of the value argument 
def size_and_value(size,value):
    list = []
    for i in range (size):
        list.append(value)
    return list
print(size_and_value(6,2))