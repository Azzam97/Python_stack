# a function to change the values in lists and dict
def change():
    x = [ [5,2,3], [10,8,9] ] #change the value of x=10 to x=15
    x[1][0] = 15
    students = [ #change the last name from jordan to bryant
        {'first_name':  'Michael', 'last_name' : 'Jordan'}, 
        {'first_name' : 'John', 'last_name' : 'Rosales'}
    ]
    students[0]['last_name'] = 'Bryant'
    sports_directory = { #change messi to andres
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer' : ['Messi', 'Ronaldo', 'Rooney']
    }
    sports_directory['soccer'][0]='Andres'
    z = [ {'x': 10, 'y': 20} ]
    z[0]['y'] = 30
    return x,students,sports_directory,z
print(change())

#a function that iterates through each key-value in the dict
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in students:
        print(f'first_name - {i["first_name"]}, last_name - {i["last_name"]}')
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


#a function that prints values from a list of dictionaries
def iterateDictionary2(key_name):
    for i in students:
        print(i[key_name])
iterateDictionary2('first_name')
iterateDictionary2('last_name')

# a function that prints the name of the values with the length of the list

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# print(len(dojo['instructors']))
def printInfo(dojo):
    print (len(dojo['locations']), 'LOCATIONS')
    for i in range (len(dojo['locations'])):
        print (dojo['locations'][i])
    print("")
    print (len(dojo['instructors']), 'INSTRUCTORS')
    for i in range (len(dojo['instructors'])):
        print (dojo['instructors'][i])
printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
