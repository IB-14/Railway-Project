#iMPORTING LIBRARIES
import random
import sys
import pickle
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

#---------------------------------------------------------------------------------------------------------------------

pd.options.display.width=None
pd.options.display.max_columns = None
import numpy as np
data = pd.read_csv('trainsxx.csv')
trainsno = data['Train No'].unique()
stations = data['Station Name'].unique()
stations = np.array(stations)
#---------------------------------------------------------------------------------------------------------------------


print("--------------------------------------------------Welcome to Railway Reservation Portal----------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------")

Email_ID=''
Name={'ishan@gmail.com':'Ishan'}
Accounts={'ishan@gmail.com':"ib14"}
Age={'ishan@gmail.com':18}
Gender={'ishan@gmail.com':'M'}
Dist={}
PNR={}
Tickets={}

train_nd_stationss={107:["SAWANTWADI R","THIVIM","KARMALI","MADGOAN JN."],
290:["DELHI-SAFDAR","GANDHINAGAR","JAIPUR JN.","DURGAPURA","SAWAI MADHOP","CHITTAURGARH","UDAIPUR CITY",'JAISALMER','MANDOR','PHULERA JN.','BHARATPUR JN','IDGAH','AGRA CANTT'],477:['SIRSA',
'HISAR JN',
'BHIWANI JN.',
'ROHTAK JN.',
'DELHI-SAFDAR',
'KANPUR CENTR',
'MUGHAL SARAI',
'KANPUR CENTR',
'ROHTAK JN.',
'BHIWANI JN.',
'HISAR JN',
'SIRSA'],
1011:['CST-MUMBAI',
'DADAR',
'THANE',
'KALYAN JN',
'IGATPURI',
'NASIK ROAD',
'MANMAD JN.',
'JALGAON JN.',
'BHUSAVAL JN.',
'MALKAPUR',
'SHEGAON',
'AKOLA JN.',
'MURTAJAPUR J',
'BADNERA JN.',
'DHAMANGAON',
'PULGAON JN.',
'WARDHA JN.',
'NAGPUR JN.(C']}
#---------------------------------------------------------------------------------------------------------------------


def accept_main_option():
    option = input("\nEnter your option :- ")
    if option not in ('1', '2', '3', '4','5'):
        print("Please enter a valid option!")
        return accept_main_option()
    else:
        return int(option)

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
    #print("Name: ", Name[Email_ID])
    #print("Age: ", Age[Email_ID])
    #print("Gender: ", Gender[Email_ID])
    main()

def book_ticket():
    x=input("Enter e-mail id: ")
    if x not in Accounts:
        while x not in Accounts:
            print("Invalid ID, try again.")
            x = input("Enter e-mail id: ")              #elif x in Accounts:
    y = input("Enter Password: ")
    while Accounts[x] != y:
        print("ID and password do not match, try again.")
        x = input("Enter e-mail id: ")
        y = input("Enter Password: ")
    if Accounts[x] == y:
        '''
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
        '''

        for q in trainsno:
            print("\nStations for Train Number ", q)
            for i in range(len(train_nd_stationss[q])):
                print(train_nd_stationss[q][i])
            print()

        start = input('Enter start :')
        end = input('Enter end :')

        if(start=="DELHI-SAFDAR" and end=="AGRA CANTT"):
            route=1
        elif(start=="AGRA CANTT" and end=="DELHI-SAFDAR"):
            route =2
        else:
            route =3
            
        c1 = 0
        c2 = 0

        for i in range(0, len(stations)):
            if start == stations[i]:
                break
            else:
                c1 += 1

        for i in range(0, len(stations)):
            if end == stations[i]:
                break
            else:
                c2 += 1
        dis = c2 - c1
        Dist[x] = dis
        print(data.loc[c1:c2, :])


        # Cost Prediction system
        pickle_in = open("ticketprices.pickle", "rb")
        linear = pickle.load(pickle_in)
        inputt=[3,1,2,5,20,3,300,route]
        inputt = np.asarray(inputt)
        inputt.reshape(-1,1)
        cp=linear.predict([inputt])*4
        print ('Predicted Ticket Price: \n', "Rs.",cp)



       # cp = random.randint(175, 999)
       # print("The cost for your choosen ticket is: ", cp)
        CHOICE = input("\nDo you want to buy ticket? (y/n)\n")
        if CHOICE == 'y':
            pnr = random.randint(1000000000, 9999999999)
            PNR[x] = pnr
            print("Your PNR Number is: ", str(PNR[x]))
            Tickets[PNR[x]] = [cp, start, end]
        else:
            print("Ticket not bought")

    main()


def check_confirmation():
    x = input("Enter e-mail id: ")
    if x not in Accounts:
        while x not in Accounts:
            print("Invalid ID, try again.")
            x = input("Enter e-mail id: ")  # elif x in Accounts:
    y = input("Enter Password: ")
    while Accounts[x] != y:
        print("ID and password do not match, try again.")
        x = input("Enter e-mail id: ")
        y = input("Enter Password: ")
    if Accounts[x] == y:
        print("Hi ", Name[x], "!")
        if x not in PNR:
            print("You have no booked tickets")
        else:
            for PNR[x] in Tickets:
                print("Gender: ", Gender[x])
                print("Age: ", Age[x])
                print("\nYou have booked train from station {} to station {}".format(Tickets[PNR[x]][1], Tickets[PNR[x]][2]))
                print("Booking fees: Rs. ", Tickets[PNR[x]][0])
                print("Your PNR Number is: ", PNR[x])
    main()



def cancel_ticket():
    x = input("Enter e-mail id: ")
    if x not in Accounts:
        while x not in Accounts:
            print("Invalid ID, try again.")
            x = input("Enter e-mail id: ")
    y = input("Enter Password: ")
    while Accounts[x] != y:
        print("ID and password do not match, try again.")
        x = input("Enter e-mail id: ")
        y = input("Enter Password: ")
    if Accounts[x] == y:
        print("Hi ", Name[x], "!")
        if x not in PNR:
            print("You have no booked tickets")
        else:
            for PNR[x] in Tickets:
                print("Gender: ", Gender[x])
                print("Age: ", Age[x])
                print("\nYou have booked train from station {} to station {}".format(Tickets[PNR[x]][1],
                                                                                     Tickets[PNR[x]][2]))
                print("Booking fees: ", Tickets[PNR[x]][0])
                print("Your PNR Number is: ", PNR[x])
        cancel = input("Enter the PNR Number for the ticket you want to enter:\n")
        '''
        z=0
        for i in Tickets:
            if i == cancel:
                z=1
        while z != 1:
            print("Enter correct PNR number")
            cancel = input("Enter the PNR Number for the ticket you want to enter:\n")
            for i in Tickets:
                if i == cancel:
                    z = 1
                    '''
        for cancel in Tickets:
            while cancel != PNR[x]:
                print("Enter correct PNR number")
                cancel = input("Enter the PNR Number for the ticket you want to enter:\n")
            if cancel == PNR[x]:
                cp = Tickets[PNR[x]][0]
                a = Tickets[PNR[x]]
                b = PNR[x]
                print("Your ticket is cancelled\nAmount of Rs {} will be transferred in your account".format(cp*0.67))

        del Tickets[PNR[x]]
        del PNR[x]


    main()


def exit():
    print(
        "\n------------------------------------------------Thank You!-----------------------------------------------------------------------")
    print(
        "---------------------------------------------------------------------------------------------------------------------------------")
    sys.exit()


def main():
    print("\nChoose one of the following options :-")
    print("1.Create Account\n2.Book Ticket\n3.Check Confirmation\n4.Cancel Ticket\n5.Exit")
    func = {1: create_acc, 2: book_ticket, 3: check_confirmation, 4: cancel_ticket, 5: exit}
    option = accept_main_option()
    func[option]()
#---------------------------------------------------------------------------------------------------------------------


main()
