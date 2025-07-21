# Write a python program to find the star pattern of the following :-

'''
*
**
***
****
*****
'''
n=int(input("Enter number of rows:-"))
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print("*",end="")
    print()

'''
*****
****
***
**
*
'''
n=int(input("Enter number of rows:-"))
for i in range(n,0,-1):
    for j in range(1,i+1,1):
        print("*",end="")
    print()

'''
*****
****
***
**
*
**
***
****
*****
'''
n=int(input("Enter number of rows:-"))
for i in range(n,0,-1):
    for j in range(1,i+1,1):
        print("*",end="")
    print()
for i in range(2,n+1,1):
    for j in range(1,i+1,1):
        print("*",end="")
    print()

'''
*
**
***
****
*****
****
***
**
*
'''


    

    
