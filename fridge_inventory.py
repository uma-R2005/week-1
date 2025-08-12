from datetime import datetime, timedelta

# Predefined fridge inventory (like real-time data)
fridge_inventory = {
    "milk": {"quantity": 1, "expiry": datetime(2025, 8, 14)},
    "eggs": {"quantity": 12, "expiry": datetime(2025, 8, 20)},
    "lettuce": {"quantity": 0, "expiry": datetime(2025, 8, 10)},  # Expired & out of stock
    "yogurt": {"quantity": 2, "expiry": datetime(2025, 8, 13)},   # Expires tomorrow
    "cheese": {"quantity": 1, "expiry": datetime(2025, 8, 30)},
    "orange juice": {"quantity": 3, "expiry": datetime(2025, 8, 15)},
    "butter": {"quantity": 0, "expiry": datetime(2025, 9, 1)},    # Out of stock but not expired
}

today = datetime.now()

print(f"Smart Fridge Inventory Report - {today.strftime('%Y-%m-%d')}")
print("--------------------------------------------------")

restock_list = []
consume_soon_list = []

for item, details in fridge_inventory.items():
    quantity = details["quantity"]
    expiry = details["expiry"]
    days_left = (expiry - today).days

    print(f"\n{item.capitalize()} | Qty: {quantity} | Expiry: {expiry.strftime('%Y-%m-%d')}")

    if quantity == 0 and expiry < today:
        print("Out of stock AND expired! Discard any leftovers and restock.")
        restock_list.append(item)
    elif quantity == 0:
        print("Out of stock. Please restock.")
        restock_list.append(item)
    elif expiry < today:
        print("Expired! Please discard.")
    elif days_left <= 2:
        print("About to expire soon. Use it quickly!")
        consume_soon_list.append(item)
    elif days_left <= 7:
        print("Will expire this week. Plan to use it.")
    else:
        print("Fresh and good to use.")

print("\n" + "="*50)
if restock_list:
    print("Restock these items ASAP: " + ", ".join(restock_list))
else:
    print("No items need restocking.")

if consume_soon_list:
    print("Use these items soon: " + ", ".join(consume_soon_list))
else:
    print("No items expiring soon.")

print("="*50)
print("Fridge inventory check complete.")
