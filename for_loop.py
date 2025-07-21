# What is loop??
'''
loop is the repeatation of a process.
'''
# syntax:-
'''
for var_name in range(start,end+1,enc/dec):
    statement
'''
'''
n=int(input("Enter number:-"))
for i in range(1,n+1,1):
    print(i,end="  ")
'''
# Write a python program to print the numbers from 11 to 55.
'''
for i in range(11,56,1):
    print(i)
'''

# Write a python program to print the numbers from 11 to  n where n is taking from the user.
'''
n=int(input("Enter the value of n:-"))
for i in range(11,n+1,1):
    print(i)
'''

# Write a python program to print the numbers from n to  10 where n is taking from the user.
'''
n=int(input("Enter value of n:-"))
for i in range(n,9,-2):
    print(i)
'''

# Write a python program to find the all even numbers from 1 to n where n is taking from the user.
'''
n=int(input("Enter the value of n:-"))#20
for i in range(1,n+1,1):
    if i%2==0:
        print(i,"is even number.")
'''
        
# Write a python program to find the all odd numbers from 1 to n where n is taking from the user.
'''
n=int(input("Enter the value of n:-"))#20
for i in range(1,n+1,1):
    if i%2!=0:
        print(i,"is odd number.")
'''

# Write a python program to find the all even and odd numbers from 11 to n where n is taking from the user.
'''
n=int(input("Enter the value of n:-"))#20
for i in range(1,n+1,1):
    if i%2==0:
        print(i,"is even number.")
    else:
        print(i,"is odd number.")
'''


# Write a python program to find the factorial of a number where number is taking from the user.
'''
5
1x2x3x4x5=factorial of 5=fact
'''
'''
n=5
fact=1
for i in range(1,n+1,1):
    fact=fact*i#120
print("factorial is",fact)
'''
# Write a python program to find the sum of digit from 1 to 10:
'''
1+2+3+4+5+6+7+8+9+10=sum of digit from 1 to 10.
'''
sum=0
for i in range(1,11,1):
    sum=sum+i
print("sum of digit from 1 to 10 is:-",sum)

# Write a python program to find the hcf of two numbers where number is taking from the user
# write a python program to find the lcm of two numbers where numbers is taking from the user.
# write a python program to find the reverse number of a number where number is taking from the  user.
# write a python program to check given number by the user is pallindrome or not.
# write a python program to check given number by the user is armstrong number or not.
# write a python program to check a number given by the user is prime or not.
# write a python program to find the prime number from 11 to n where n is taking from the user.
    





    

   
    
    

