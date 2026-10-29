expenses=[] # list of expenses in the form of dictionary
print("Welcome to expense tracker:")

while True:
    print("======MENU======")
    print("1.Add Expense")
    print("2.View All Expense")
    print("3.View Total Expense")
    print("4.Exit")

    choice=int(input("Please Enter Your choice: "))
    
# Add expense
    if(choice ==1):
        date=input("Enter the date: ")
        category=input("Enter category?(Food,Travel,Makeup,Books): ")
        description=input("Enter details: ")
        amount=float(input("Enter the amount: "))
        
        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        
        expenses.append(expense)
        print(" DONE bro. Expense is added successfully.")
        
#2.VIEW ALL EXPENSES
    elif(choice==2):
        if(len(expenses)==0):
            print("No Expense Added.First buy something.")
            
        else:
            count=1
            for eachExp in expenses:
                print(f"Expense {count} -> {eachExp['date']}, {eachExp['category']}, {eachExp['description']}, {eachExp['amount']}")
                count += 1
                
#View total spending
    elif(choice==3):
        total=0
        for eachExp in expenses:
            total=total+eachExp["amount"]
            
        print("\n TOTAL EXPENSE=",total)            
        
#exit
    elif(choice==4):
        print("Thank you for using our system...")
        break
    
    else:
        print("INVALID CHOICE! Try again...")
        