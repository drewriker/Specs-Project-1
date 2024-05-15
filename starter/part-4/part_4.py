### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. 
# After that be sure to turn it into a function.

# Code here
'''
def create_new_book():
    title = input("What is the title of the book you want to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    year = input("What year was this book published? - ")
    rating = input("What rating out of 5 would you give this book? - ")
    pages = input("What is the page count of the book? - ")
    
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    return book_dictionary

print(create_new_book())
'''

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. 
# Feel free to comment out your old function so you don't get an error, 
# or copy/paste and give it a new name.

# Code here
'''
def create_new_book():
    title = input("What is the title of the book you want to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    year = int(input("What year was this book published? - "))
    rating = float(input("What rating out of 5 would you give this book? - "))
    pages = int(input("What is the page count of the book? - "))
    
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    return book_dictionary
    
'''

### Step 3 - Error handling

## Now take your previous function, and handle potential errors 
# should the user type an answer that doesn't convert data-type properly.

# Code here

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
    return book_dictionary


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. 
# Handle their choices with if/elif/else statements.

# Code here
books = [
    {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "year": 2008,
        "rating": 4.32,
        "pages": 374
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "rating": 4.27,
        "pages": 336
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "rating": 4.77,
        "pages": 328
    }
]
def highest_rated(books):
    highest_rated = books[0]
    for book in books:
        if book["rating"] > highest_rated["rating"]:
            highest_rated = book
    return highest_rated

'''
def main_menu():
    choice = int(input("Would you like to - \n1. See all books - \n2. Add a book - \n3.See highest rated book in library - "))
    
    if choice == 1:
        print(books)
    elif choice == 2:
        # create_new_book()
        books.append(create_new_book())
    elif choice == 3:
        print(highest_rated(books))
    else:
        return False

main_menu()
'''

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, 
# and continually asking for input until the user chooses to exit the program. 
# Call the main menu to ensure it functions properly.

# Code here

def main_menu():
    while True:
        choice = int(input("Would you like to - \n1. See all books - \n2. Add a book - \n3. See highest rated book in library - \n4. Exit - "))
        
        if choice == 1:
            print(books)
        elif choice == 2:
            # create_new_book()
            books.append(create_new_book())
        elif choice == 3:
            print(highest_rated(books))
        elif choice == 4:
            print("exiting the program")
            break
        else:
            print("invalid choice. Please choose between 1-4")

main_menu()