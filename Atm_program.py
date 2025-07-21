# Write a python program to perform ATM PROGRAM.
bal=2000
withdraw=int(input("Enter Amount:-"))#1000
if bal>=withdraw:
    bal=bal-withdraw#2000-1000=1000
    print("Transaction is Successfull!!!!!")
    print("Your available ballance is:-",bal)
else:
    print("Invalid Amount!!!!!")
