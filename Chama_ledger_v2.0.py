# CHAMA LEDGER v0.3
# Thursday, Feb 12, 2026

import json
import os

# ---------------------------
# 1. INITIAL DATA
# ---------------------------
members = {
    "Mama": {
        "balance":5000,
        "phone" : "072345678",
        "joined" : "2024-01-10",
        "last_contribution" : "2024-01-08",
    },

    "Jane": {
        "balance": 3000,
        "phone": '072345678',
        "joined" : "2024-01-15",
        "last_contribution" : "2024-02-08",
    },

    "Alice":{
        "balance" :4500,
        "phone" : "073456789",
        "joined" :"2024-01-20",
        "last_contribution":"2024-02-12",
}
}
# ---------------------------
# 2. CORE FUNCTIONS
# ---------------------------
def add_member(member_dict, name, balance=0):
    """Add a new member to the chama"""
    if name not in member_dict:
        member_dict[name] = balance
        print(f"➕ Member '{name}' added with balance Ksh {balance}")
    else:
        print(f"⚠️ Member '{name}' already exists.")

def add_contribution(member_dict, name, amount):
    """Add money to member's balance"""
    if name in member_dict:
        member_dict[name]['balance'] += amount
        member_dict[name]['last_contribution'] = "2024-02-16"  # today
        print(f"✅ {name} contributed Ksh {amount}")
        print(f"   New balance: Ksh {member_dict[name]['balance']}")
    else:
        print(f"❌ Member '{name}' not found.")

def calculate_interest(member_dict, rate=0.05):
    """Apply monthly interest to all balances"""
    for name in member_dict:
        interest = member_dict[name] * rate
        member_dict[name] += interest
        print(f"📈 {name}: +Ksh {interest:.2f} interest (5%)")
    return member_dict

def show_all(member_dict):
    """Display all members and their details"""
    print("\n--- CHAMA MEMBERS ---")
    for name, details in member_dict.items():
        print(f"👤 {name}")
        print(f"   Balance: Ksh {details['balance']}")
        print(f"   Phone: {details['phone']}")
        print(f"   Joined: {details['joined']}")
    total = sum(details['balance'] for details in member_dict.values())
    print(f"💰 TOTAL FUNDS: Ksh {total}")
    print("---------------------\n")


# ---------------------------
# 3. FILE SAVE / LOAD
# ---------------------------
DATA_FILE = "chama_data.txt"

def save_data(member_dict):
    """Save member data to a text file (JSON format)"""
    with open(DATA_FILE, "w") as f:
        json.dump(member_dict, f)
    print(f"💾 Data saved to {DATA_FILE}")

def load_data():
    """Load member data from file (if exists)"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        print("📁 No saved data found. Starting fresh.")
        return {}

# ---------------------------
# 4. QUICK TEST (RUN THIS FILE)
# ---------------------------
if __name__ == "__main__":
    print("🚀 CHAMA LEDGER v0.3")
    
    # Show current members
    show_all(members)
    
    # Add a contribution
    add_contribution(members, "Mama", 1000)
    
    # Add a new member
    add_member(members, "Cate", 2000)
    
    # Apply 5% monthly interest
    calculate_interest(members)
    
    # Show final state
    show_all(members)
    
    # Save to file
    save_data(members)

# Added 10 min sesion
def remove_member(member_dict, name):
    """Remove a mamber from chama"""
    if name in member_dict:
        del member_dict[name]
        print(f" Member'{name}' removed")
    else:
        print(f" Member '{name}' not found")


#1. Loop through memmbers and print each with formating 
def print_members(memmber_dict):
    for name, balance in memmber_dict.items():
        print(f" {name}:ksh {balance}")

#2. Find members with balance belowwt threshold
def low_balanc_members(memmber_dict, threshold=1000): 
    low =[]
    for name, balance in member_dict.items():
        if balance < threshold:
            low.append(name)
        return low
#3. Give bonus to everyone(loop+modify)
def new_year_bonus(member_dict, bonus=200):
    for name in member_dict:
        member_dict[name] += bonus
    print(f" New year bonus of ksh {bonus} added to all members")

def get_member_by_phone(member_dict, phone):
    """Find a member using their phone number"""
    for name, details in member_dict.items():
        if details['phone'] == phone:
            print(f"📱 Found: {name} - Balance: Ksh {details['balance']}")
            return name
    print("❌ No member with that phone number.")
    return None

def low_balance_alert(member_dict, threshold=1000):
    """List members below threshold"""
    print(f"\n⚠️ Members with balance below Ksh {threshold}:")
    found = False
    for name, details in member_dict.items():
        if details['balance'] < threshold:
            print(f"   {name}: Ksh {details['balance']}")
            found = True
    if not found:
        print("   None")
if __name__ == "__main__":
    print("🚀 CHAMA LEDGER v0.4 - NESTED DICTIONARIES")
    
    show_all(members)
    add_contribution(members, "Mama", 1000)
    get_member_by_phone(members, "0723456789")
    low_balance_alert(members, 4000)