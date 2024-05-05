print("this is client\n")
import Pyro4
#prompt the user to enter the url of the server 
uri=input("enter the url of the server:")
#CONNECT TO THE SERVER 
calc=Pyro4.Proxy(uri)
#function to perform addition
def perform_addition():
    x=float(input("enter the first number:"))
    y=float(input("enter the second number "))
    result=calc.add(x,y)
    print("result of addition",result)
#function to perform subtraction
def perform_subtraction():
    x=float(input("enter the first number:"))
    y=float(input("enter the second number "))
    result=calc.subtract(x,y)
    print("result of subtract",result)
#interactive menu
while True:
    print("\n choose operation:")
    print("1.addition")
    print("2.subtraction")
    print("3.EXIT")
    choice=input("enter your choice 1,2,3:")
    if choice=="1":
        perform_addition()
    elif choice=="2":
        perform_subtraction()
    elif choice=="3":
        print("exiting client")
        break
    else:
        print("invalid choice.Please enter 1,2 and 3.")


