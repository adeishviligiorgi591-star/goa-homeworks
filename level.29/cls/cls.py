#1)
def even_or_odd(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
#2)
def positive_sum(arr):
    sum=0
    for i in arr:
        if i>0:
             sum+=i
    return sum 
#3)
def repeat_str(repeat, string):
    return repeat*string
#4)
def greet():
    return "hello world!"
#5)
def double_integer(i):
    return i*2