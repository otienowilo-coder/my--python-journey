# Can do:
#1.Add members(name,balance)
#2.Record contributions
#3.Calculate 5% monthly intrest
#4.Save data to chama_data txt


#functions
def calculate_intrest(balance, rate=0.05):
    """Calculate 5% monthly intrest"""
    return balance*rate

def add_contribution(member_dict, name, amount):
    """Add money to member's balance"""
    if name in member_dict:
        member_dict[name] += amount
        print(f"✅ {name} contributed Ksh {amount}. New balance: {member_dict[name]}")
    else:
        print(f"❌ Member '{name}' not found.")
    return member_dict   # optional, dictionary is updated in place
