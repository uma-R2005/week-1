total_spots = 10
occupied_spots = 0

def show_status():
    print(f"\nTotal spots: {total_spots}")
    print(f"Occupied spots: {occupied_spots}")
    print(f"Available spots: {total_spots - occupied_spots}\n")

while True:
    print("Smart Parking Lot System")
    print("1. Car Enter")
    print("2. Car Exit")
    print("3. Show Parking Status")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        if occupied_spots < total_spots:
            occupied_spots += 1
            print("Car entered. Spot allocated.")
            if occupied_spots == total_spots:
                print("⚠️ Notification: Parking is now FULL!")
        else:
            print("Parking Full! No spots available.")

    elif choice == '2':
        if occupied_spots > 0:
            occupied_spots -= 1
            print("Car exited. Spot freed.")
            if occupied_spots == 0:
                print("ℹ️ Notification: Parking is now EMPTY!")
        else:
            print("Parking Empty! No cars to exit.")

    elif choice == '3':
        show_status()

    elif choice == '4':
        print("Exiting Smart Parking Lot System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

    print("\n")
