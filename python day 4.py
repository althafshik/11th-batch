
# -----> while loop
# -----> break using while loop

# eg : 1
# 1.) iterate from 20 to 30 and break the loop in 27

i = 20
while i<31:
    print(i)
    i+=1

# 2.)
i = 20
while i<31:
    print(i)
    i+=1

    if i==27:
        break

    
# 3.)
# i = 20
# while i<31:
#    print(i)
#    if i==27:
#        break
#    i+=1


# i = 20
# while i<31:
#    if i==27:
#        print(i)
#        break
#    i+=1
    
# ! ------> continue
# ---> eg:1
# i = 20
# while i<31:
#    if i==27:
#        continue
#    print(i)
#    i=i+1


# i = 20
# while i<31:
#    i=i+1
#    if i==27:
#       continue
#    print(i)

# ! eg:5
# while to iterate from 12 to 22
# find the sum of all numbers



# i = 12
# while i<23:
#   sum=0
#    sum=sum+i
#   print(sum)
#    i+=1
# print(sum)

# ! Eg :6
# Find the average of value from 20to 30

# i = 20
# sum = 0
# count = 0
# while i<=30:
#     sum = sum+1
#     count+=1
#  i+=1
# print(sum/count)
# ------> nested for loop
# eg:1
# for row in range (1, 3+1):
#     for col in range (1, 4+1):
#        print(row,col)

# eg:2
# * * * *
# * * * *
# * * * *
# * * * *

row = int(input("enter the rows: "))
col = int(input("enter the cols: "))

# for row in range (rows):
#     for col in range (cols):
#        print("*",end=" ")
#     print()

# sum = 0
# for now in ranges(5):
#     for col in range(5):
#         sum = sum + 1
#       print(sum, end=" ")
#     print()


# ! to print stars in right angled triangle
# for row in range (0, 6):
#    for col in range(0, row+1):
#        print("*",end=" ")
#    print()

# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for row in range (0, 6, =1)
#  for col in range(0, row)
#   print("*", ends=" ")
#  print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# for row in range(5):
#     for col in range(5);
#     if col==0 or col==5 or row ==0 or row ==5-1
#        print('*', end=" ")
#    else:
#        print(" ", end=" ")
#    print()


#      *
#    * * *
#   * * * *
#  * * * * *

#  for row in range(0, 5):
#      for col in range(0, 6):
#          if ((row==0 and col==3) or (row==1 and(col>=2 andcol<=4) or
#                                      (row==2 and.(col>=1 and col<=5)))):
#              print("*", end=" ")
#              else:
#                  printy(" ", end=")
#     print()


# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# ? ---> List

# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
# l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]


# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous



#--> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value
# We have 2 types of indexing
# Positive indexing --> starts with @ from left hand side
# Negative indexing --> starts with -1 from right hand side

   
s1 = "hello world to all"
