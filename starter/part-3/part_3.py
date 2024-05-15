my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. 
# Define and flesh out your function below, 
# which should accept a dictionary as an argument when called, 
# and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_parser(book):
    book_string = f"The book '{book['title']}' by {book['author']} was published in {book['year']}. It has a rating of {book['rating']} and consists of {book['pages']} pages."
    return book_string

print(book_parser(my_book))

# Once you are finished with that function, 
# create several more functions which return individual pieces of information from the book.

# Code below
def book_title(book):
    return book['title']

def book_author(book):
    return book['author']

def book_year(book):
    return book['year']

def book_rating(book):
    return book['rating']

def book_pages(book):
    return book['pages']



# Finally, create at least three new functions that might be useful as we expand our home library app. 
# Perhaps think of a way you could accept additional arguments when the function is called? 
# Also, imagine you have a list filled with dictionaries like above.

# Code below

def find_longest_book(books):
    longest_book = books[0]
    for book in books:
        if book["pages"] > longest_book["pages"]:
            longest_book = book
    return longest_book

def count_books(books):
    return len(books)

def highest_rated(books):
    highest_rated = books[0]
    for book in books:
        if book["rating"] > highest_rated["rating"]:
            highest_rated = book
    return highest_rated