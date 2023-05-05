list = [8,5,6,3,4,2,7,9,1]
for j in range (8):
    for i in range (1,9):
        if list [i-1]>list[i]:
            list[i-1],list[i] = list[i], list[i-1]
print(list)

# sequences can be accessed with ([start,stop,step])
# start is where it starts the counting to be printed
# stop where to stop the printing
# step is how it will be incriminted