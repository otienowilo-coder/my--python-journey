# CHAMA LEDGER v0.3
# Thursday, Feb 12, 2026

import json
import os

# ---------------------------
# 1. INITIAL DATA
# ---------------------------
members = {
    "Mama": 5000,
    "Jane": 3000,
    "Alice": 4500
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
        member_dict[name] += amount
        print(f"✅ {name} contributed Ksh {amount}. New balance: {member_dict[name]}")
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
    """Display all members and balances"""
    print("\n--- CHAMA BALANCES ---")
    for name, bal in member_dict.items():
        print(f"{name}: Ksh {bal}")
    total = sum(member_dict.values())
    print(f"💰 TOTAL: Ksh {total}")
    print("----------------------\n")

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