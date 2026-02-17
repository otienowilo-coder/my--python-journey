# Simple Logic for the Farm Data App

farmer_list = []

def add_farmer (name, phone , crop , is_organic):
    farmer_data = {
        "name" : name,
        "phone" : phone,
        "crop" : crop,
        "status" : "Lead" if not is_organic else "Ready for export"
    }
    farmer_list.append(farmer_data)
    print(f"Added{name}.status:{farmer_data['status']}")
     