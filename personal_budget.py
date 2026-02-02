# personal_budget.py - 50/25/15/10 Smart Budget Planner
print("=" * 45)
print("     PERSONAL BUDGET PLANNER")
print("=" * 45)

# 1. GET INPUT (String -> Float Conversion)
income_input = input("\nEnter your total monthly income (Ksh): ")
# Convert the input string to a float for calculations
try:
    monthly_income = float(income_input)
except ValueError:
    print("❌ Please enter a valid number.")
    exit()  # Stops the program if input isn't a number

# 2. DEFINE RATIOS (Float Constants)
NEEDS_RATIO = 0.50      # 50% for Needs (Expenses)
GROWTH_RATIO = 0.25     # 25% for Growth & Investments
EMERGENCY_RATIO = 0.15  # 15% for Emergency Fund
FUN_RATIO = 0.10        # 10% for "Pay Yourself" / Fun

# 3. CALCULATE ALLOCATIONS (Float Arithmetic)
needs_allocation = monthly_income * NEEDS_RATIO
growth_allocation = monthly_income * GROWTH_RATIO
emergency_allocation = monthly_income * EMERGENCY_RATIO
fun_allocation = monthly_income * FUN_RATIO

# 4. DISPLAY RESULTS (Using f-strings for clean formatting)
print("\n" + "=" * 45)
print("RECOMMENDED MONTHLY ALLOCATION")
print("=" * 45)

# :,.2f formats the number with commas and 2 decimal places
print(f"\nTotal Income:       Ksh {monthly_income:,.2f}\n")
print(f"📍 Needs (50%):      Ksh {needs_allocation:,.2f}")
print(f"📈 Growth (25%):     Ksh {growth_allocation:,.2f}")
print(f"🛡️  Emergency (15%):  Ksh {emergency_allocation:,.2f}")
print(f"🎉 Fun / Self (10%): Ksh {fun_allocation:,.2f}")

print("\n" + "=" * 45)
# 5. ADD A SIMPLE BOOLEAN CHECK
high_income = monthly_income > 100000  # A Boolean variable
if high_income:
    print("💡 Tip: With your income, consider automating transfers to savings!")
else:
    print("💡 Tip: Track every shilling against your 'Needs' budget first.")
print("=" * 45)