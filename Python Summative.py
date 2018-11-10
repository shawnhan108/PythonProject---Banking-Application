import time
import datetime

#Start the app:
def StartProgram ():
    print ("Welcome to MAY Banking App. This app includes the following features: ")
    print ("A. Transfer, B. Deposit, C. Withdrawal, D. View Balance, E. View Transaction History F. Pay Bills")
    print ("First, please create or login to your account.")

#Username and password setup subprogram (Feature 1)
#First ask for username and password, check if they are valid or used before.
#then store username and password in .txt doc as username and UPchain

def uname_pw_setup ():
    Username_list = []
    #to setup the username
    while True:
        found=0
        Username = input("Please enter the username you want to have.")
        with open("Username.txt", "r") as f:
            for line in f:
                Username_list.append(line.strip())
            f.close()
            length_ulist= len(Username_list)
            #to check if the username has been taken or not
            for x in range(length_ulist):
                if Username_list[x] == Username:
                    print ("The username you entered has already been used. Please enter another one.")
                    Username_list=[]
                    found=1
                    break
                else:
                    continue
            if found!=1:
                #update the .txt document to store Username
                Username_tem=(Username+"\n")
                with open("Username.txt", "a+") as f:
                    f.write("\n")
                    f.write(Username_tem)
                f.close()
                break
            else:
                pass
    global login_uname
    login_uname = Username
    
    #to set up the password
    while True:
        password = input ("Please enter the password you want to have.")
        repassword = input ("please re-enter your password")
        if password != repassword:
            print ("The two passwords you have entered are not the same.")
            continue
        else:
            break
    #to match the username and password created, and store them in separated .txt file.
    UPchain = (Username+","+password)
    print ("Please remember your username and password.")
    with open("UPchain.txt", "a+") as f:
        f.write("\n")
        f.write(UPchain)
        f.close()
        
    #to setup the amount of bills the user has to pay each month.
    f= open(login_uname+"bills"+".txt","a+")
    f.write("120")
    f.write("\n")
    f.write("100")
    f.write("\n")
    f.write("90")
    f.write("\n")
    f.write("70")
    f.write("\n")
    f.write("150")
    f.write("\n")
    f.write("200")
    f.write("\n")
    f.write("50")
    f.write("\n")
    f.close()
        
#login subprogram (Feature 1)
#Need to verify the UPchain. If correct, proceed the program; else deferred.       
def login():
    UPchain_list=[]
    correct=0
    while correct==0:
        #to create a temporary UPChain
        global login_uname
        login_uname=input("Please enter your username:")
        login_pw=input("Please enter your password")
        login_UPchain=(login_uname+","+login_pw)
        with open("UPchain.txt", "r") as f:
            for line in f:
                UPchain_list.append(line.strip())
            f.close()
            len_chainlist= len(UPchain_list)
        #to check if uname password are correct by comparing the old & new UPChain
            for x in range(len_chainlist):
                if UPchain_list[x] == login_UPchain:
                    print ("Successful Login.")
                    correct=1
                else:
                    continue
            if correct==0:
                print ("The username or password you have entered is INCORRECT.")
            else:
                pass

#Feature 2: Create personal accounts subprogram
#Need to check if the account name has been taken or not, and if the user entered amount is a valid integer.
def create_account (login_uname):
    Exit1=0
    while Exit1==0:
        found=0
        name=input("What is the name of the account that you want to create?")
        #the following exception may occur in the case when the user has just created the application account
        #and has no accounts created yet
        try:
            read (login_uname)
        except FileNotFoundError:
            break
        #to check if the account name has been taken or not
        for x in range(len_account):
            if accounts[x] == name:
                found=1
                print ("The account you entered already exists. Please use another name.")
                break
            else:
                continue
        if found==0:
            Exit1=1
        else:
            pass
        
    #to check if the amount entered is valid
    Exit=0
    while Exit==0:
        bal= input ("What is the current account balance? Must be an integer")
        Exit= check_int (bal,Exit)
    print ("Account created. Thank you.")
    
    #create two files to store all account names and all balances.
    f= open(login_uname+"account"+".txt","a+")
    f.write(name)
    f.write ("\n")
    f.close()
    f= open(login_uname+"amount"+".txt","a+")
    f.write(bal)
    f.write ("\n")
    f.close()
    read (login_uname)
    history (name,bal,"0")


#define a subprogram for reading the account and amount file
#need to read then globalize the account and amount lists for other subprograms to use.
def read (login_uname):
    global accounts
    global amounts
    global len_account
    accounts=[]
    amounts=[]
    with open(login_uname+"account"+".txt", "r") as f:
        accounts = [line.rstrip('\n') for line in f]
    f.close()
    with open(login_uname+"amount"+".txt", "r") as f:
        amounts = [line.rstrip('\n') for line in f]
    f.close()
    len_account=len(accounts)

#transaction history (create & update)
#first record a transaction to .txt history doc
def history (acc,DR,CR):
    for x in range (len_account):
        if accounts[x] == acc:
            bal_from = amounts[x]
            break
        else:
            continue
    time=datetime.datetime.now().strftime("%B %d, %Y")
    f= open(login_uname+"history"+".txt","a+")
    f.write("{:<20}".format(time))
    f.write("{:<13}".format(acc))
    f.write("{:<11}".format(DR))
    f.write("{:<13}".format(CR))
    f.write(("{:<15}".format(str(bal_from))))
    f.write("\n")
    f.close()

#display the transaction history by first reading from .txt doc then desmontrate using formatting.
def view_history():
    print("________________________________________________________________________________")
    print("{:^75}".format("Transaction History"))
    print("{:<20}{:<13}{:<11}{:<13}{:<15}".format("Date","Account","Debit","Credit","Balance"))
    print("")
    f= open(login_uname+"history"+".txt","r")
    for line in f:
        print(line)
    f.close()
    print("________________________________________________________________________________")
   
#Feature 5: view account balances subprogram
#read from .txt file and display using formatting.
def viewbal (login_uname):
    read (login_uname)
    print("________________________________________________________________________________")
    print ("{:^75}".format("List of Accounts"))
    print ("{:20} {:20} {:10}".format("","Account","Balance"))
    print ("")
    for x in range (len_account):
        print ("{:20} {:20} {:10}".format("",accounts[x],amounts[x]))
    print("________________________________________________________________________________")

#module: to check if the account entered exists
#use loop to check through the list and then return an exit signal.
def check_acc (acc, Exit):
    found=0
    for x in range(len_account):
        if accounts[x] == acc:
            found=1
            break
        else:
            continue
    if found==0:
        print ("The account you entered does not exist.")
    else:
        Exit=1
    return (Exit)

#module for casting to check the value entered is numerical
#use try-exception with casting. Return an exit signal.
def check_int (am,Exit):
    try:
        int(am)
        Exit=1
    except ValueError:
        print ("The amount you entered is not valid.")
    return (Exit)

#module for checking if the account has enough balance to transfer/withdraw
#use loop to check through the list, then return an exit signal.
def check_bal (acc,Amount_to, Exit):
    for x in range (len_account):
        if accounts[x] == acc:
            bal_from = amounts[x]
            break
        else:
            continue
    if (float(bal_from))<(float(Amount_to)):
        print ("Your",acc,"account balance is inadequate for the operation amount. ")
    else:
        Exit=1
    return (Exit)

#module for updating .txt document after operation
def doc_update ():
    with open(login_uname+"account"+".txt", 'w') as f:
        for a in accounts:
            f.write(str(a) + "\n")
    f.close()
    with open(login_uname+"amount"+".txt", 'w') as f:        
        for a in amounts:
            f.write(str(a) + "\n")
    f.close()
    print ("Your account balance is as follows:")
    viewbal (login_uname)

#Feature 3: Transfer between accounts
#check account entered exits or not, check amount entered is an integer and
#is lower then the first account's balance.
#Finally update the account balance, write to .txt file, and display the updated balance.
def Transfer (login_uname):
    while True:
        Exit=0
        Exit1=0
        Exit2=0
        Exit3=0
        read (login_uname)
        print ("Your account balance is as follows:")
        viewbal (login_uname)
        while Exit1==0:
            Acc_from = input("Enter name of the account that you want to transfer FROM:")
            #to check the account entered exists
            Exit1= check_acc (Acc_from, Exit1)

        while Exit2==0:
            Acc_to = input("Enter name of the account that you want to transfer TO: ")
            #to check the account entered exists
            Exit2= check_acc (Acc_to, Exit2)

        while Exit==0:
            Exit3=0
            #to check if the amount entered is valid
            while Exit3==0:
                Amount_to = input("Enter the amount you want to transfer, must be an integer.")
                Exit3= check_int (Amount_to,Exit3)
            #to check if the account has enough balance to transfer
            Exit=check_bal (Acc_from,Amount_to, Exit)       

        #to actually decrease/increase the account balance and record on transaction history
        for x in range (len_account):
            if accounts[x]== Acc_from:
                amounts[x]=int(amounts[x])-int(Amount_to)
                history (accounts[x],"0",Amount_to)
                break
            else:
                continue
            
        for x in range (len_account):
            if accounts[x]== Acc_to:
                amounts[x]=int(amounts[x])+int(Amount_to)
                history (accounts[x],Amount_to,"0")
                break
            else:
                continue           
        print ("Successful transfer.")
        doc_update()

        #ask if the user wants to make another transfer.
        while True:
            Repeat=0
            repeat = input("Do you want to make another transfer? (yes/no)")
            if repeat == "yes":
                Repeat=1
                break
            elif repeat=="no":
                break
            else:
                print ("INVALID. Please re-enter your choice.")
        if Repeat==0:
            break
        else:
            pass

#Feature 4: deposit
#Check the account entered exists, the amount is an integer
#then increase the account balance, update .txt file, and finally display new balance.
def deposit (login_uname):
    while True:
        print ("Your account balance is as follows:")
        read (login_uname)
        viewbal (login_uname)
        Exit1=0
        Exit2=0
        while Exit1==0:
            acc_deposit = input("Enter name of the account that you have DEPOSITED TO:")
            #to check the account entered exists
            Exit1= check_acc (acc_deposit, Exit1)

        while Exit2==0:#to check if the amount entered is an integer
            amount_deposit = input("Enter the amount you have deposited, must be an integer.")
            Exit2=check_int(amount_deposit,Exit2)

        #to increase the amount for deposit
        for x in range (len_account):
            if accounts[x]==acc_deposit:
                amounts[x]=int(amounts[x])+int(amount_deposit)
                history (accounts[x],amount_deposit,"0")
                break
            else:
                continue
        print ("Successful deposit.")
        doc_update ()
        
        #to ask if the user wants to make another deposit
        while True:
            Repeat=0
            repeat = input("Do you want to make another deposit? (yes/no)")
            if repeat == "yes":
                Repeat=1
                break
            elif repeat=="no":
                break
            else:
                print ("INVALID. Please re-enter your choice.")        
        if Repeat==0:
            break
        else:
            pass

#Feature 5: withdrawal
#check if the account entered exists and if the amount is an integer and lower than the account balance.
#finally decrease the account balance, update .txt file, and then display the new balance.
def withdrawal (login_uname):
    while True:
        print ("Your account balance is as follows:")
        read (login_uname)
        viewbal (login_uname)
        Exit1=0
        Exit2=0
        Exit=0
        while Exit1==0:
            acc_withdraw = input("Enter name of the account that you have WITHDRAWN FROM:")
            #to check the account entered exists
            Exit1= check_acc (acc_withdraw, Exit1)
            
        while Exit==0:
            Exit2=0
            #to check if the amount entered is an integer
            while Exit2==0:
                amount_withdraw = input("Enter the amount you have withdrawn, must be an integer.")
                Exit2=check_int (amount_withdraw,Exit2)
            #to check if the account balance is adequate for the withdrawal amount
            Exit=check_bal(acc_withdraw,amount_withdraw,Exit)

        #to increase the amount for withdrawal
        for x in range (len_account):
            if accounts[x]==acc_withdraw:
                amounts[x]=int(amounts[x])-int(amount_withdraw)
                history (accounts[x],"0",amount_withdraw)
                break
            else:
                continue
        print ("Successful withdrawal.")
        doc_update ()
        
        #to ask if the user wants to make another withdrawal
        while True:
            Repeat=0
            repeat = input("Do you want to make another withdrawal? (yes/no)")
            if repeat == "yes":
                Repeat=1
                break
            elif repeat=="no":
                break
            else:
                print ("INVALID answer. Please re-enter your choice.")
        if Repeat==0:
            break
        else:
            pass

#module for reading and printing bills
#first read from .txt file, then display using formatting.
def print_bills(login_uname):
    global bills
    with open(login_uname+"bills"+".txt", "r") as f:
        bills = [line.rstrip('\n') for line in f]
    f.close()
    print ("Your monthly bills are as the following:")
    print ("_____________________________________________________________")
    print ("{:20} {:20} {:20}".format("Bills", "Price", "Remaining Bills"))
    print ("")
    print ("{:20} {:20} {:20}".format("A.","Electricity", bills[0]))
    print ("{:20} {:20} {:20}".format("B.","Water", bills[1]))
    print ("{:20} {:20} {:20}".format("C.","Gas", bills[2]))
    print ("{:20} {:20} {:20}".format("D.","Cell Phone", bills[3]))
    print ("{:20} {:20} {:20}".format("E.","internet", bills[4]))
    print ("{:20} {:20} {:20}".format("F.","Groceries", bills[5]))
    print ("{:20} {:20} {:20}".format("G.","Insurance", bills[6]))
    print ("_____________________________________________________________")

#subprogram for paying individual bills
#check if the account entered exists and if the amount entered is an integer,
#if it is not greater then the bill, and if the account has enough balance (sufficient fund).
#then update both the account balance and the bill, update .txt files,
#finally display the remaining bills and the account balances.
def pay_bills_sub (login_uname, bill_num):
    Exit=0
    Exit1=0
    Exit2=0
    Exit3=0
    Exit4=0
    #to check the account entered exists
    while Exit1==0:
        viewbal (login_uname)
        pay_account = input ("Which account do you want to use to pay?")
        Exit1=check_acc (pay_account, Exit1)

    #to check if the amount entered is an integer
    while Exit==0:
        Exit2=0
        Exit3=0
        reduce=input("Please enter the amount of payment, must be an integer:")
        Exit2=check_int(reduce,Exit2)
        if Exit2==0:
            continue
        else:
            pass
        # to check if the user input has the appropriate amount
        if float(reduce)>float(bills[bill_num]): 
            print ("The amount you have entered exceeds the bill. Please enter a lower value.")
        else:
            Exit3=1
        if Exit2+Exit3!=2:
            continue
        else:
            pass
                
        #to check if the account balance is adequate for the withdrawal amount
        Exit4=check_bal (pay_account,reduce, Exit4)
        if Exit2+Exit3+Exit4!=3:
            Exit=0
        else:
            Exit=1
        
    #to update the bill file
    bills[bill_num]= int(bills[bill_num])-int(reduce)
    with open(login_uname+"bills"+".txt", 'w') as f:
        for a in bills:
            f.write(str(a) + "\n")
        f.close()
        #to decrease the account balance after paying the bill
        for x in range (len_account):
            if accounts[x]==pay_account:
                amounts[x]=int(amounts[x])-int(reduce)
                print ("Successful payment. The following is your remaining bills:")
                print_bills(login_uname)
                doc_update ()
                history (accounts[x],"0",reduce) #to update the transaction history
                break
            else:
                continue

#Feature 7: Pay Bills
#display the bills and ask if user wants to pay
#if they want, then according to the bill they indicate, call the subprogram to pay that particular bill.
def pay_bills_main(login_uname):
    Exit=0
    read (login_uname)
    #ask user if he/she wants to pay the bill
    print_bills(login_uname)
    while True:
        choice=input ("Pay them now? (yes/no)")
        if choice== "yes":
            break
        elif choice== "no":
            Exit=1
            break
        else:
            print ("INVALID. Please re-enter your choice.")

    #ask about which bill the user wants to pay and run the subprogram.
    while Exit==0: 
        while True:
            ans = input("Please enter the letter of the bill that you want to pay:")
            if (ans=="A") or (ans=="a"):
                pay_bills_sub (login_uname, 0)
                break
            elif (ans=="B") or (ans=="b"):
                pay_bills_sub (login_uname, 1)
                break
            elif (ans=="C") or (ans=="c"):
                pay_bills_sub (login_uname, 2)
                break
            elif (ans=="D") or (ans=="d"):
                pay_bills_sub (login_uname, 3)
                break
            elif (ans=="E") or (ans=="e"):
                pay_bills_sub (login_uname, 4)
                break
            elif (ans=="F") or (ans=="f"):
                pay_bills_sub (login_uname, 5)
                break
            elif (ans=="G") or (ans=="g"):
                pay_bills_sub (login_uname, 6)
                break
            else:
                print ("Input INVALID. Please re-enter your choice.")

        #to check if the user wants to pay another bill
        while True:
            Repeat=0
            repeat = input ("make another payment? (yes/no)")
            if repeat == "yes":
                Repeat=1
                break
            elif repeat=="no":
                break
            else:
                print ("INVALID. Please re-enter your choice.")
        if Repeat==0:
            break
        else:
            pass

#Main program: Feature 1: To create user account or login
#first ask if the user wants to login or signup. For either option, call the corresponding subprogram.
#then display all the operation/feature choices,
#and according to user's input choice, call the corresponding subprogram.
StartProgram ()
while True:
    create_login = input("To login, press L. To sign up, press S.")
    if (create_login == "S") or (create_login == "s"):
        uname_pw_setup()
        create_account (login_uname)
        break
    elif (create_login == "L") or (create_login == "l"):
        login()
        break
    else:
        print ("Invalid input. Please re-enter your choice.")

#Display choice of operations for the user.
print ("Now you can choose operations to manage your bank accounts.")
while True:
    print ("Operation Choices:")
    print ("To create a personal account, press A.")
    print ("To view your accounts and balances, press V.")
    print ("To transfer between accounts, press T.")
    print ("To deposit, press D.")
    print ("To withdraw, press W.")
    print ("To view transaction history, press H.")
    print ("To pay bills, press P.")
    print ("To exit, press E.")
    choice=input("Please enter your choice:")
    if (choice=="A") or (choice=="a"): #Feature 2: Personal Accounts
        create_account (login_uname)
    elif (choice=="V") or (choice=="v"): #Feature 5: view accounts and balances
        viewbal (login_uname)
    elif (choice=="T") or (choice=="t"): #Feature 3: transfer between accounts
        Transfer (login_uname)
    elif (choice=="D") or (choice=="d"): #Feature 4: Deposit
        deposit (login_uname)
    elif (choice=="W") or (choice=="w"): #Feature 4.5: withdrawal
        withdrawal (login_uname)
    elif (choice=="H") or (choice=="h"): #Feature 6: view history
        view_history()
    elif (choice=="P") or (choice=="p"): #Feature 7: pay bills
        pay_bills_main (login_uname)
    elif (choice=="E") or (choice=="e"): #To exit the program
        print ("THANK YOU for using the application.")
        print ("Free trial is over.")
        break
    else:
        print ("INVALID. Please re-enter your choice.")
 
