#1) Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F
def abbrev_name(name):
    names=name.split()
    names1=names[0]
    names2=names1[0].upper()
    lastname1=names[1]
    lastname2=lastname1[0].upper()
    return names2 + "." + lastname2
# 2) Create a function that accepts a parameter representing a name 
# and returns the message: "Hello, <name> how are you doing today?".
def greet(name):
    return f"Hello, {name} how are you doing today?"
# 3) Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated,
# he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need 
# to return the number of litres Nathan will drink, rounded down.
def litres(time):
    return int(time*0.5)
#4)Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example (Input => Output):
# 35231 => [1,3,2,5,3]
# 0     => [0]
 
def digitize(n):
    n = str(n)
    n = n[::-1]
    res = []
    for i in n:
        res.append(int(i))
    return res






# 5)Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]
def maps(a):
    result=[]
    for x in a:
        result.append(x*2)
    return result
# 6) Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

# Example:
# n= 5, m=5: 25
# n=-5, m=5:  0
def paperwork(n, m):
    if n<0 or m<0:
        return 0
    else:
        return n*m
# 7) Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
def are_you_playing_banjo(name):
    if name[0]=="R" or name[0]=="r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"