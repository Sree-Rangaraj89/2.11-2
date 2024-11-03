class Library:

    def __init__(self, list_of_books, name):
        self.bookslist = list_of_books
        self.name = name
        self.lenDict = {}

    def displayBooks(self):
        print(f"We have the followuing books in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendbook(self, user, book):
        if book not in self.booksList:
            print("Sorry, we do not have that book.")
        elif book in self.landDict:
            print(f"The book is already being used by {self.lanDict[book]}")
        else:
            self.lenDict[book] = user
            print(
                "Lender Book database has been updated.You can take book now"
                  )
            
        def addBook(self, book):
            self.bookList.append(book)
            print(f"{book} has been added to the book list.")

        def returnBook(self, book):
            if book in self.lenDict:
                del self.lenDict[book]
                print("book has been returned.")
            else:
                print("That book wasn't borrowed form us.")


if __name__ == "__main__":
    books = Library([
        'Python','Rich dad Poor dad', 'Harry Potter', 'C++ Basics',
        'Algorithms by CLRS'
    ], "Let's Upskill")
    user_name = input("Welcome to our library! Please enter your name: ")

    while True:
        print(
            f"\nHello {user_name}, welcome to the {books.name} library.Please choose an option:"
        )
        print(
            "1. Display books\n2. Lend a book\n3.Add a Book\n4.Return a Book\n5.Quit"
        )
        user_choice = input("Enter your choice to countinue:")

        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a valid option.")
            continue

        if user_choice == '1':
            books.displayBooks()
        elif user_choice == '2':
            book = input("Enter the name of the book you want to lend: ")
            books.lendbook(user_name, book)
        elif user_choice == '3':
            book = input("Enter the name of the book you want to add: ")
            books.addBook(book)
        elif user_choice == '4':
            book = input("Enter the name of the book you want to return: ")
            books.returnBook(book)
        elif user_choice == '5':
            print(f"thank you for using the libray,{user_name}. Goodbye!")
            break