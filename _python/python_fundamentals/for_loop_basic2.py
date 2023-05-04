biggie_size = [-1,3,5,-5]
def biggie():
    for i in range(len(biggie_size)):
        if biggie_size[i] > 0 :
            biggie_size[i] = "big"
    return biggie_size
c = biggie()
print(c)