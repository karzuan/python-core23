### M3 Lesson 3
## Boolean and comparison operators:

# AND
result = 3 >= 1 and 10 < 20
print(result)

# OR
result = 3 >= 1 or 10 > 20
print(result)

# NOT
a = True
print(not a)


# not equal to
a = True
b = False
print(a!=b)

#examples:

#1
result = (a >= minimum and b >= minimum) or minimum == 0

#2
expression1 = (a > b and a < c) or limit == 0
expression2 = x <= y or x <= z or x <= g
result = expression1 or expression2

#3 - In addition, you should know that if there are several operators, you will get the result from the first false statement, and the interpreter will not compute the others:
a = 10
result = a < 10 and a < 20 and a > 5 and a % 5 == 0
print(result)

#4 - If you replace and with or, the result will return from the first true statement:
a = 10
result = a < 10 or a < 20 or a > 5 or a % 5 == 0
print(result)

# Conditions - if, elif

#1
a = 20
b = 33
minimum = 0
if (a >= minimum and b >= minimum) and minimum != 0:
    result = (a + b) * 2
elif minimum == 0:
    print("The minimum value is not defined!")
    result = 0
else:
    result = 1
print(result)

#2
my_operation = "read":
if my_operation == "read":
    print("perform read operation…")
elif my_operation == "update":
    print("perform update operation …")
elif my_operation == "insert":
    print("perform insert operation …")
elif my_operation == "delete":
    print ("perform delete operation …")
else:
    print("wrong variant if operation !!! ")

## Match/case operator
# But in Python 3.10, you can use another solution—a match/case construction (pattern matching). It may be more suitable for such cases because the result code is more readable.

my_operation = "read"
match my_operation:
    case "read":
        print("perform read operation…")
    case "update":
        print("perform update operation …")
    case "insert":
        print("perform insert operation …")
    case "delete":
        print("perform delete operation …")
    case _:
        print("wrong variant if operation !!!")


#Ternary operator
fruit = "apple"
is_apple = "Yes" if fruit == "apple" else "No"
print(is_apple)

# bool
result = 2 > 1 and 1 < 2
print(type(result))
# <class 'bool'>
# compare with 0
if x == 0:
    print("x is zero!")
elif x != 0:
    print("x is not zero!")
# compare with False
# 0 will convert to False, while any number that is not 0 will convert to True.
if not x:
    print("x is zero!")
elif x:
    print("x is not zero!")


# None type
# 1
nothing = None
print(type(nothing))

# 2
if x == None:
    print("x is None!")
elif x != None:
    print("x is not None!")

# 3
if not x:
    print("x is None!")
elif x:
    print("x is not None!")

