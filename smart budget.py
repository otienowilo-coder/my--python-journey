#Smart_budget.py - A personal budget advisor using bolean logic

print("===smart budget advisor===")

# 1. GET USER INPUT (Convert to appropriate types)
monthly_income = float(input("Enter your monthly income(ksh)"))
monthly_expense = float(input("Enter a planned expense(ksh)"))
is_essential = input("is this expense essential (yes/no)").lower() == 'yes'
#update
is_essential=input("is this essential? (yes/no):").lower()=='yes'
has_emergency_fund =input("Do you haveemegency fund? (yes/no)").lower () =='yes'

#2.CALCULATE KEY METRICS
expense_ratio=(monthly_expense/ monthly_income) #percentag
savings =monthly_income-monthly_expense

#3.BOOLEAN FLAGS(The core logic variables)
is_expense_small =monthly_expense<500
is_expense_large = expense_ratio>30
can_afford= savings >0

#4.SMART ADVICE LOGIC (if/elif/else with logical operators)
print("/n== Analysis==")

if not can_afford:
    advice = "CRITICAL: this expense exceeds your income!"
elif is_expense_large and not is_essential:
    advice = "WARNING: Large non essential expense.consider postponing"
elif is_expense_large and is_essential and not has_emergency_fund:
    advice = "CAUTION: Large essential expense without emergency fund."
elif is_expense_small or is_essential:
    advice ="APPROVED:This is a responsible expense"
else:
    advice ="NEUTRAL :Expense is within resonable limits"
#5.DISPLAY RESULTS
print(f"Expense/income ratio:{expense_ratio:.1f}%")
print(f"Remaing after  expenses:ksh{savings:.2f}")
print(f"\n Recommendation: {advice}")

#6.BONUS :CATEGORY TIPS(Nested if)
print("\n=== Tips ===")
if is_essential:
    if monthly_expense > 1000 :
        print("For large essential expenes, consider payment plan")
else:
    print("For non-essential expenses, try a 24-hour 'cooling off' period")
    if expense_ratio > 20:
        print("Consider savinf for thisover 2-3 months")