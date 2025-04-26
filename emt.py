#----------------------------------------------------------------------Q1---------------------------------------------------------
# import turtle
# def first():
#     for s in range(10):
#         for i in range(4):
#             turtle.color('green')
#             turtle.forward(50)
#             turtle.left(90)
#         turtle.left(-90)
#     turtle.done()
#-----------------------------------------------------------------------------Q2------------------------------------------------------
# primery = [2,3,5,7,11,13,17,19,23]
# def aval(n):
#     if primery[n]%primery[n]==0 and primery[n]%1==0:
#         print(primery[n],'is primery number')

# def second():
#     b=int(input('enter n:'))
#     d=int(input('enter k:'))
#     aval(b)
#     print(primery[b+d])
# #----------------------------------------------------------------------------Q3---------------------------------------------------------
# import random
# import itertools

# numbers = [random.randint(1, 15) for _ in range(20)]
# print("list number:", numbers)

# valid_subsets = []

# for r in range(1, len(numbers)+1):
#     for subset in itertools.combinations(numbers, r):
#         if 50 <= sum(subset) <= 52:
#             valid_subsets.append(subset)

# print("elemans:")
# for subset in valid_subsets:
#     print(subset, "sum:", sum(subset))