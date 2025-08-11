library = [
    {'title': '1984', 'author': 'George Orwell', 'available': True},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'available': True},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'available': True},
]

def show_catalog():
    if not library:
        print("\nLibrary catalog is empty.\n")
        return
    print("\n--- Library Catalog ---")
    for idx, book in enumerate(library, 1):
        status = "Available" if book['available'] else "Borrowed"
        print(f"{idx}. '{book['title']}' by {book['author']} - {status}")
    print("-----------------------\n")

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    library.append({'title': title, 'author': author, 'available': True})
    print(f"Book '{title}' by {author} added to the catalog.\n")

def borrow_book():
    show_catalog()
    if not library:
        return
    try:
        choice = int(input("Enter book number to borrow: "))
        if 1 <= choice <= len(library):
            book = library[choice - 1]
            if book['available']:
                book['available'] = False
                print(f"You have borrowed '{book['title']}'. Enjoy reading!\n")
            else:
                print("Sorry, this book is already borrowed.\n")
        else:
            print("Invalid book number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def return_book():
    show_catalog()
    if not library:
        return
    try:
        choice = int(input("Enter book number to return: "))
        if 1 <= choice <= len(library):
            book = library[choice - 1]
            if not book['available']:
                book['available'] = True
                print(f"Thank you for returning '{book['title']}'.\n")
            else:
                print("This book was not borrowed.\n")
        else:
            print("Invalid book number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

while True:
    print("Digital Library Catalog")
    print("1. Show Catalog")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        show_catalog()
    elif choice == '2':
        add_book()
    elif choice == '3':
        borrow_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        print("Exiting Library Catalog. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
