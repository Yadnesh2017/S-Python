#Anonymous Function Lambda
"""Anonymous function means function without a Name"""
# syntax
# lambda argument:expression

twice = lambda x: x * 2
print(twice(7))         #printing

# syntax
# (lambda argument:expression)(argument)

twice = (lambda x: x * 2)(7)        
print(twice)                        #printing
print((lambda x: x * 2)(7))         #printing


#syntax multiple arguments
#   (lambda arg1,arg2,...argn:expression)(arg1,arg2,...argn)
#   lambda  arg1,arg2,...argn:expression

#1
mul = lambda x,y: x * y
print(mul(5,2)) 

#2
mul = (lambda x,y: x * y)(5,2)  
print(mul) 

#3
print((lambda x,y: x * y)(5,2)) #Function without name : lambda
