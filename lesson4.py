# M3 Lesson 4: Loops

# While
# x = int(input("Please input 0 to stop iteration: "))
# sum_result = 0
# while x:
#     sum_result += x
#     x = int(input("Please input 0 to stop iteration: "))
# print(sum_result)


# Continue
# Operator continue allows you to move on to the next iteration, depending on some condition.
# n = int(input("Input integer number: "))
# sum_result = 0
# x = 1
#
# while x < n:
#     x += 1
#     if x % 2:
#         continue
#     sum_result += x


# Break
# The following example checks if the entered number is prime.
# In cases when it is known that the number is not prime at some iteration, there is no longer a reason to continue checking.
# And the loop should be interrupted. For this purpose, Python has a break operator, which allows interrupt loops.
# x = int(input("Imput integer number: "))
# is_prime = True
# div = 2
#
# while div < x:
#     if not x % div:
#         is_prime = False
#         break
#     div += 1
#
# if is_prime:
#     print("Prime")
# else:
#     print("Not prime")

# Else
# x = 1
# while x < 5:
#      print(x)
#      x += 1
# else:
#      print("Loop was stopped at:")
#      print(x)

## FOR loop
# 1
# for i in range(5):
#        print(i)


# 2
# x = int(input("Imput integer number: "))
# is_prime = True
# for div in range(2, x):
#    if not x % div:
#        is_prime = False
#        break
# if is_prime:
#    print("Prime")
# else:
#    print("Not prime")


# 3
x = int(input("Input integer number: "))

for div in range(2, x):
     if not x % div:
            print("Not prime")
            break
else:
     print("Prime")

















