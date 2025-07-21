# Write a python program to find the hcf of two numbers where number is taking from the user.
'''
10,20
20%10==0
hcf=10

20,25
25%20==0
r=5
20%5==0
hcf is 5
51,61
'''
n1=int(input("Enter first Number:-"))#20
n2=int(input("Enter second Number:-"))#10
if n1<n2:
    small=n1
else:
    small=n2#10
for i in range(small,0,-1):
    if n1%i==0 and n2%i==0:
        print("Hcf is:-",i)
        break
lcm=(n1*n2)//i
print("lcm is :-",lcm)
# write a python program to find the lcm of two numbers:-
'''
hcfxlcm=n1xn2
'''

    
