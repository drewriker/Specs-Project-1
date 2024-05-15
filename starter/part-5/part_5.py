### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, 
# to write and read info from a .txt file. 
# Follow the instructions to create and call a function to add a book, 
# based off of the previous dictionaries for our library, 
# to the .txt file properly formatted with commas as separators.

# Code here
def add_book_to_txt(books):
    for book in books:
        with open("library.txt", "a") as file:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['rating']},{book['pages']}\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, 
# but gets the info from a list, and make it work by reading the information in your home library's .txt document. 
# This will take some new logic, but you can do it.

# Code here
def format_book_info(books):
    books_info = ""
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
print(format_book_info(read_books_from_txt()))
### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement 
# to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. 
# Clean up the code. Make your application functional. 
# Great job getting your first Python application finished!

