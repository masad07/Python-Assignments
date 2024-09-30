# Library Management System

# Data structures for books and users
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "status": "Available"},
    {"id": 2, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "Checked Out"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "status": "Available"}
]

users = [
    {"id": 1, "name": "Alice", "borrowed_books": []},
    {"id": 2, "name": "Bob", "borrowed_books": []}
]

# Function to display the menu
def display_menu():
    print("""
Welcome to the Community Library System!
----------------------------------------
Please choose an option:
1. View all books
2. Search for a book
3. Borrow a book
4. Return a book
5. View all users
6. Exit
    """)

# Function to display all books
def view_all_books():
    print("All Books:")
    for book in books:
        print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')
    print("----------------------------------------")

# Function to search for books by title, author, or genre
def search_books():
    criteria = input("Search by (title/author/genre): ").lower()
    keyword = input(f"Enter the {criteria}: ").lower()
    
    matching_books = [book for book in books if keyword in book[criteria].lower()]
    
    if matching_books:
        for book in matching_books:
            print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')
    else:
        print("No matching books found.")
    print("----------------------------------------")

# Function to borrow a book
def borrow_book():
    user_id = int(input("Enter your User ID: "))
    book_id = int(input("Enter the Book ID you want to borr1ow: "))
    
    # Find the book and user
    book = next((book for book in books if book["id"] == book_id), None)
    user = next((user for user in users if user["id"] == user_id), None)
    
    if book and user:
        if book["status"] == "Available":
            book["status"] = "Checked Out"
            user["borrowed_books"].append(book["title"])
            print(f'You have successfully borrowed "{book["title"]}".')
        else:
            print(f'Sorry, the book "{book["title"]}" is currently checked out.')
    else:
        print("Invalid User ID or Book ID.")
    print("----------------------------------------")

# Function to return a book
def return_book():
    user_id = int(input("Enter your User ID: "))
    book_id = int(input("Enter the Book ID you want to return: "))
    
    # Find the book and user
    book = next((book for book in books if book["id"] == book_id), None)
    user = next((user for user in users if user["id"] == user_id), None)
    
    if book and user and book["title"] in user["borrowed_books"]:
        book["status"] = "Available"
        user["borrowed_books"].remove(book["title"])
        print(f'You have successfully returned "{book["title"]}".')
    else:
        print("Invalid return. Either the book was not borrowed by this user or the information is incorrect.")
    print("----------------------------------------")

# Function to view all users
def view_all_users():
    print("All Users:")
    for user in users:
        print(f'ID: {user["id"]}, Name: {user["name"]}, Borrowed Books: {", ".join(user["borrowed_books"]) if user["borrowed_books"] else "None"}')
    print("----------------------------------------")

# Main program loop
def library_system():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            view_all_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_all_users()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            print("----------------------------------------")

# Run the system
library_system()
