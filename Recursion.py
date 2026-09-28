#recursion: to recur to go back
#python limits recursion fn

#higher order fn :
    # two types= fn returns another fn
    #              fn takes another fn as argument
#
# def counttozero(n):
#     print(n)
#     if n==0:
#         return
#     return counttozero(n-1)
# counttozero(10)
#
#
#
# # sum of numbers
# def counttozero(n):
#     if n==0:
#         return 0
#     return n + counttozero(n-1)
# print(counttozero(10))


# Factorial of a number
def counttozero(n):
    if n==1:
        return 1
    return n * counttozero(n-1)
print(counttozero(5))

