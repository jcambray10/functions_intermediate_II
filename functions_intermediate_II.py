x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
# print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
# print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)
# Change the value 20 in z to 30
z[0]['y'] = 30
# print(z)

def iterateDictionary(name_list):
    for idx in range(len(name_list)):
        for key in name_list[idx]:
            # print(name_list[idx][key])
            print(key, '-', name_list[idx][key])
# or

def iterateDictionary(name_list):
    for student_dict in range(len(name_list)):
        for key in student_dict:
            print(key, '-', student_dict[key])
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# print(iterateDictionary(students))
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. For example, 
# iterateDictionary2('first_name', students) should output:
def iterateDictionary2(key_name, name_list):
    for idx in range(len(name_list)):
        print(name_list[idx][key_name])

# iterateDictionary2('first_name', students)

# And iterateDictionary2('last_name', students) should output:
# iterateDictionary2('last_name', students)

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list. For example:

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for value in some_dict[key]:
            print(value)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

# output:
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
# python functions_intermediate_II.py

# echo "# functions_intermediate_II" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jcambray10/functions_intermediate_II.git
# git push -u origin main