## M3
## L2: Numbers
## L3: Boolean and comparision operator

### INTEGER
# Valid integer literals:
# x = input("Please input some integer: ")
# print(type(x))
# y = int(x) # the result of the input function is a string. Therefore, before using it, you should convert it to an integer.
# print("This is Y content: ", y, " This is Y type: ", type(y))
#
# #Unallowed leading zeros:
# ## x = 001234
#
# ##The int() function allows converting string and float values to int.
# x = "100"
# y = int(x)
# print(type(y))
#
# ### FLOAT
# a = 7893.45
# 5.244
# b = -4.44
# 0.32
# 1.0e0
# #
# # #The float type in Python is represented by the float class. Use the float() function to convert string, int to float.
# x = "100"
# y = float(x)
# print(type(y))
# print(y)
#
# ### COMPLEX
# x = "1+2j"
# y = complex(x)
# print(type(y))
#
#
# ## Using operators:
#
# c = 5 + 10
# b = 3
# a = c / b
# print(a)
#
# ## In this example, you should also notice that the result of the division is always a floating-point number.
# ## In complex expressions, you should consider operators precedence:
# x = 10 + 30 + 6 / 3
# print(x)
# #42.0
#
# x = (10 + 30 + 6) / 3
# print(x)
# #15.3333333…….

import math
a = 5
b = 2.5
c = 4
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(area)

angle_degrees = 60
angle_radians = math.radians(angle_degrees)
print(math.cos(angle_radians))
#0.5000000000000001

#Another example using Euclidean distance:
x = 3.5
y = 5.2
print("Euclidean distance for x=", x, " y=", y, " hypot=", math.hypot(x, y))

x = 6
y = 7
print("Euclidean distance for x=", x, " y=", y, " hypot=", math.hypot(x, y))

x = 9.2
y = 10
print("Euclidean distance for x=", x, " y=", y, " hypot=", math.hypot(x, y))

# Euclidean norm for x= 3.5  y= 5.2  hypot= 6.2681735776859275
# Euclidean norm for x= 6  y= 7  hypot= 9.219544457292887
# Euclidean norm for x= 9.2  y= 10  hypot= 13.588230201170422


import random

x = 0
y = 6
print(random.randint(x, y))
print(random.randint(x, y))
print(random.randint(x, y))

















