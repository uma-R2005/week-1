items = []
num_items = int(input("How many different items are in your cart? "))

for i in range(num_items):
    print(f"\nItem {i + 1}:")
    name = input("Enter item name: ")
    price = float(input("Enter item price (₹): "))
    quantity = int(input("Enter quantity: "))
    items.append({"name": name, "price": price, "quantity": quantity})

subtotal = 0.0
for item in items:
    subtotal += item["price"] * item["quantity"]

tax = subtotal * 0.18
discount = 0.10 * subtotal if subtotal > 3000 else 0
total = subtotal + tax - discount

print("\n🧾 BILL SUMMARY")
for item in items:
    print(f"{item['name']} x {item['quantity']} = ₹{item['price'] * item['quantity']:.2f}")

print(f"\nSubtotal: ₹{subtotal:.2f}")
print(f"Tax (18%): ₹{tax:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Total: ₹{total:.2f}")
