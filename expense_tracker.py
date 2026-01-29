#expense_tracker.py
#This programme collects an expense and stores it in a list


#1. Ask for expense details (USER INPUT)
print("---Expense Tracker v1.o---")
expense_name= input("What did you spenf money on?")#Returns a string
expense_amount= input("How much did it cost in ksh?")#Returns a string

#2. Convert the amount from txt (str) to a decimal number (float)
#This is necessary to do math later
expense_amount=float(expense_amount)

#3. Store the data in a list 
# A list stores multiple items in oder. We stat with one expense
expenses_list =[expense_amount] #[] creates the list

#4. Display summary(OUTPUT)
print("\n--- Receipt---")
print(f'item:{expense_name}')  #float insertd variable into text
print(f'amount: ksh{expense_amount}')
print(f'total expenses so far:ksh {sum(expenses_list)}')
print('thank you')

#Addition to expense tracker
budget=1000

#BOLEAN AND COMPARISON {free code camp boleans and conditionals}
is_over_budget = expense_amount >budget  # this evaluates to True of False
print(f'is over budget ?{is_over_budget}')

#IF/ELSE 
if expense_amount >budget:
    print('OVER BUDGET! considfe reducing this expense')
elif expense_amount== budget:
    print("Exactly at budget limit")
else:
    #logical operators

     if expense_amount > 0 and expense_amount < budget*0.5:
        print("Good! this uses less than 50% of your budget")
     else:
        print("Within budget")