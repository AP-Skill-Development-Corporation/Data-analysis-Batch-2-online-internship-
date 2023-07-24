def greetings(name):
    print('Hello :',name)
def addition(a,b):
    return a+b
def reverse(n):
    rev = 0
    while(n!=0):
        rem = n%10
        rev=rev*10+rem
        n = n//10
    return rev
a = 100