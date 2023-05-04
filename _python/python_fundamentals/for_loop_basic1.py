#basic for loop that counts from 0 to 150
for i in range(151):
  print(i)
#multiples of 5
for i in range(5,1001,5):
  print(i)
#counting the dojo way
for i in range(1,101):
  if i%10 == 0:
    print("Coding Dojo")
  elif i%5 == 0:
    print("Coding")
  else:
    print(i)
#whoa, that sucker's huge
sum = 0
for i in range(500001):
  if i%2 != 0:
    sum +=i
print(sum)
#counting down by fours
for i in range (2018,1,-4):
  print(i)
#flexible counter
lownum, highnum, mult = 9,500,33
for i in range(lownum,highnum+1):
  if i%mult == 0:
    print(i)