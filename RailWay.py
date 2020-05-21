print("--------------------------------------------------Welcome to Railway Reservation Portal----------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------")

Email_ID=''
Name={}
Accounts={}
Age={}
Gender={}
Dist={}

def create_acc():
    name = str(input("Enter Your Name: "))
    Email_ID = input("Enter Your e-mail address: ")
    Name[Email_ID]=name
    age = int(input("Enter your age: "))
    Age[Email_ID]=age
    gender = str(input("If you are male, enter M\nIf you are female, enter F\n"))
    Gender[Email_ID]=gender
    pass1 = input("Enter Password: ")
    pass2 = input("Re-enter Password: ")
    while pass1 != pass2:
        print("Passwords do not match, try again.")
        pass1 = input("Enter Password: ")
        pass2 = input("Re-enter Password: ")
    if pass1==pass2:
        passw=pass1
    Accounts[Email_ID]=passw

def book_ticket():
    x=input("Enter e-mail id: ")
    y=input("Enter Password: ")
    if x in accounts:
        while accounts[x] != y:
            print("ID and password do not match, try again.")
            x = input("Enter e-mail id: ")
            y = input("Enter Password: ")
        if accounts[x]==y:
            #From database we will show all the trains and there stations available
            #train = int(input("Enter the train number you want to travel in: "))
            #For now ->
            print("Welcome To Train X\nThe stations are in the following order")
            print("A->B->C->D->E->F")
            print("Distance between each consecutive station is same")
            start = input("Enter starting station: ")
            destination = input("Enter final destination: ")
            while ord(start)>ord(destination):
                print("This train doesn't travel from station {} to station {}\nGive station choice again".format(start, destination))
                start = input("Enter starting station: ")
                destination = input("Enter final destination: ")
            distance = ord(destination)-ord(start)
            Dist[x] = distance

def main():
    print("Choose one of the following options :-")
    print("1.Create Account\n2.Book Ticket\n3.Check Confirmation\n4.Cancel Ticket")
    func = {1: create_acc, 2: book_ticket, 3: check_confirmation, 4: cancel_ticket}
