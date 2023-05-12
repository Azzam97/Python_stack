# loop that changes the positive numbers into the word big
biggie_size = [-1,3,5,-5]
def biggie():
    for i in range(len(biggie_size)):
        if biggie_size[i] > 0 :
            biggie_size[i] = "big"
    return biggie_size
c = biggie()
print(c)

#loop that changes the final value into the number of positive values
def count_positive():
    sum = 0
    count_positives = [1,6,-4,-2,-7,-2]
    for i in range (len(count_positives)):
        if count_positives[i] > 0:
            sum +=1
    count_positives[len(count_positives)-1]=sum
    return count_positives
x = count_positive()
print(x)

# lopp that takes all of the values in the list and sums them up
def sum_totals():
    sum = 0
    sum_total = [1,2,3,4]
    for i in range (len(sum_total)):
        sum += sum_total[i]
    return sum
z = sum_totals()
print(z)

# a loop that gives the average of a list of numbers
def average():
    numbers =[1,2,3,4]
    sum = 0
    for i in range (len(numbers)):
        sum += numbers[i]
    return sum/len(numbers)
y = average()
print(y)

# a loop that returns the length of a list
def length():
    numbers = [37,2,1,-9]
    length_of_list = 0
    for i in range (len(numbers)):
        length_of_list += 1
    return length_of_list
b = length()
print (b)

# a loop that returns the minimum value in a list
def minimum():
    numbers = [37,2,1,-9]
    minimum_value = 0
    length = len(numbers)
    if length == 0:
        minimum_value = "false"
    else:
        for i in range(len(numbers)):
            if numbers[i]<minimum_value :
                minimum_value = numbers[i]
    return minimum_value
c = minimum()
print(c)

# a loop that returns the maximum value for the list
def maximum():
    numbers = [37,2,1,-9]
    maximum_value = 0
    length = len(numbers)
    if length == 0:
        maximum_value = "false"
    else:
        for i in range(len(numbers)):
            if numbers[i]>maximum_value :
                maximum_value = numbers[i]
    return maximum_value
d = maximum()
print(d)

# a loop that returns a dictionary of total sum, average, length, maximum and minimum values
def analysis():
    numbers = [37,2,1,-9]
    maximum_value = 0
    minimum_value = 0
    length = len(numbers)
    sum = 0
    average = sum/length
    average = 0
    for i in range (length):
        sum += numbers[i]
        if numbers[i]<minimum_value :
            minimum_value = numbers[i]
        if numbers[i]>maximum_value :
            maximum_value = numbers[i]
    list_analysis = {'sum_total': sum,'average': average,'length': length,'maximum': maximum_value,'minimum': minimum_value}
    return list_analysis
e = analysis()
print(e)

# a function that reverses a list
numbers = [37,2]
numbers.reverse()
print(numbers)

def reverse1(numbers):
    for i in range (len(numbers)):
        if i<(len(numbers)/2):
            numbers[i], numbers[len(numbers)-i-1] = numbers[len(numbers)-i-1], numbers[i]
    return numbers
f = reverse1(numbers)
print(f)

def reverse2(numbers):
    temp = 0
    for i in range (len(numbers)):
        if i<(len(numbers)/2):
            temp = numbers[len(numbers)-i-1]
            numbers[len(numbers)-i-1] = numbers[i]
            numbers[i] = temp
    return numbers
g = reverse2(numbers)
print(g)