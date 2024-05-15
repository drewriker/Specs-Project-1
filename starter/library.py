def add_book_to_txt(books):
    for book in books:
        with open("library.txt", "a") as file:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['rating']},{book['pages']}\n")
            
def format_book_info(books):
    books_info = "\n"
    for book in books:
        book_info = ""
        book_info += f"Title: {book['title']}\n"
        book_info += f"Author: {book['author']}\n"
        book_info += f"Year: {book['year']}\n"
        book_info += f"Rating: {book['rating']}\n"
        book_info += f"Pages: {book['pages']}\n\n"
        books_info += book_info
    return books_info

def read_books_from_txt():
    books = []
    with open("library.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            book = {
                "title": data[0],
                "author": data[1],
                "year": int(data[2]),
                "rating": float(data[3]),
                "pages": int(data[4])
            }
            books.append(book)
    return books

def create_new_book():
    title = input("What is the title of the book you want to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Please enter a number for the year - "))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:
        rating = float(input("Please enter a number for the rating - "))
    try:
        pages = int(input("What is the page count of the book? - "))
    except:
        pages = int(input("Please enter a number for the number of pages - "))
    
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    add_book_to_txt([book_dictionary])
    return 

def highest_rated(books):
    highest_rated = books[0]
    for book in books:
            highest_rated = book
    return format_book_info([highest_rated])

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. See all books")
        print("2. Add a book")
        print("3. See highest rated book in library")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(format_book_info(read_books_from_txt()))
        elif choice == "2":
            create_new_book()
        elif choice == "3":
            print(highest_rated(read_books_from_txt()))
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    main_menu()