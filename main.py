# Expense tracker project 

expensesList = [] # List of expenses in form of dictionary
print("Welcome to expense tracker : Kharcha kam kiya karo ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View all expenses")
    print("3. View total Kharcha")
    print("4. Exit")

    choice= int(input("Please enter your Choice : "))

# 1. Add expense
    if(choice == 1):
        date= input("Kis date par kharcha kiya tha?: ")
        category= input("Kis type ka kharcha kiya? (Food, Travel, Makeup, Books): ")
        description= input("Aur detail dedo: ")
        amount= float(input("Enter the amount: "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print(" \n Expense is added sucessfully")

# 2. View all expenses 
    
    elif(choice == 2):
        if( len(expensesList)==0 ):
            print("No expenses added. Jao Pehle kharcha karo. ")
        else:
            print("====== Ye hai apka sara expense ======")
            count= 1
            for eachkharcha in expensesList:
                print(f"Kharcha number {count} -> {eachkharcha["date"]}, {eachkharcha["category"]}, {eachkharcha["description"]}, {eachkharcha["amount"]}")
                count= count+1

# 3. View total spending 
    elif(choice == 3):
        total= 0
        for eachkharcha in expensesList:
            total = total + eachkharcha["amount"]

        print("\n TOTAL KHARCHA = ", total)

# 4. EXIT
    elif(choice == 4):
        print("Dhanyawad aapne humara system use kiya")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")
