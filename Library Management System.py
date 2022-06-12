import datetime
import re


# function to write the information of book in a txt file
class Information:
    def __init__(self, name1, author, quantity12, price):
        self.name = name1
        self.author = author
        self.quantity = quantity12
        self.price = price

    def book_info(self):
        info_all = [self.name, self.author, self.quantity, self.price]
        file = open("Book information.txt", "a")  # writing information of the book in Book information file
        file_one = ",".join(info_all)
        file.writelines(file_one)
        file.write("\n")
        file.close()

    def display(self):
        book_display = [self.name, self.author, self.quantity, self.price]
        str_display = ",".join(book_display)
        print(str_display)


# List of books
# Format of book is ["name of book", "author", "quantity", "borrowing price"]
book1 = Information("Code Complete", " Steve McConnell", " 30", " 2 ")
book2 = Information("Time Machine", " H.G. Wells", " 15", " 1 ")
book3 = Information("Origin of Species", " Charles Darwin", " 25", " 1.5 ")
book4 = Information("The Wild Iris", " Louis Gluck", " 10", " 1.5 ")
book5 = Information("Obama: The Call of History", " Peter Baker", " 5", " 1 ")
book6 = Information("Clean Code", " Robert C. Martin", " 35", " 2 ")


# function with all book information is called
def func_all():
    book1.book_info()
    book2.book_info()
    book3.book_info()
    book4.book_info()
    book5.book_info()
    book6.book_info()


func_all()


class BName:
    def __init__(self, nam, code1):
        self.name_user = nam
        self.b_code = code1

    # Creating function for borrowed books
    def borrower_name_code(self):
        # name of borrower is outside for loop since it is only one and should not be repeated
        name_a = "Name of the borrower: ", self.name_user
        code_b = "Borrowing code: ", self.b_code
        file_a = open(self.name_user + self.b_code + ".txt", "a")  # writing name of the borrower in borrowed file
        file_a.writelines(name_a)
        file_a.writelines("\n")
        file_a.writelines(code_b)
        file_a.writelines("\n")
        file_a.close()


class BBname:
    def __init__(self, book_n2):
        self.book_ns2 = book_n2

    # creating function for book name because it is used frequently below

    def func_user(self):
        ask_user2_p = "Name of the book: ", self.book_ns2
        file_c = open(n1.name_user + n1.b_code + ".txt", "a")  # appending name of the book in borrowed file
        file_c.writelines(ask_user2_p)
        file_c.writelines("\n")
        file_c.close()


class DateTime:
    def __init__(self, date_borrow, time_borrow):
        self.date = date_borrow
        self.time = time_borrow

    # Creating function for date and time
    def date_func(self):
        date_b = "Date of book borrowed: ", self.date
        time_b = "Time of book borrowed: ", self.time
        file_b = open(n1.name_user + n1.b_code + ".txt", "a")  # appending date and time of the book borrowed in file
        file_b.writelines(date_b)
        file_b.writelines("\n")
        file_b.writelines(time_b)
        file_b.writelines("\n")
        file_b.close()

    def books_return(self):
        date_r = "Date of book returned: ", self.date
        time_r = "Time of book returned: ", self.time
        file_r2 = open(borrower + code_re + " return.txt", "a")  # appending date and time of the book borrowed in file
        file_r2.writelines(date_r)
        file_r2.writelines("\n")
        file_r2.writelines(time_r)
        file_r2.writelines("\n")
        file_r2.close()


# function that noted the date and time of book borrowed
def borrow_date_time():
    date = datetime.datetime.today().date()  # taking only date from datetime
    date_str = str(date)
    time = datetime.datetime.today().time()  # taking only time from datetime
    time_zone = time.strftime("%I:%M %p")  # Time are in 24-hour format so converting into 12-hour format
    d1 = DateTime(date_str, time_zone)
    d1.date_func()


# function that noted the date and time of book returned
def returning_date_time():
    date_02 = datetime.datetime.today().date()  # taking only date from datetime
    date_str02 = str(date_02)
    time_02 = datetime.datetime.today().time()  # taking only time from datetime
    time_zone2 = time_02.strftime("%I:%M %p")  # Time are in 24-hour format so converting into 12-hour format
    d2 = DateTime(date_str02, time_zone2)
    d2.books_return()


def borrow_file_read():
    print("\n[              Books borrow details                     ]")
    print(" ____________________________________________________ ")
    file3 = open(n1.name_user + n1.b_code + ".txt", "r")
    file_read3 = file3.read()
    print(file_read3)
    file3.close()


def return_file_read():
    print("\n[              Books returned details                        ]")
    print(" ____________________________________________________ ")
    file4 = open(borrower + code_re + " return.txt", "r")
    file_read4 = file4.read()
    print(file_read4)
    file4.close()


# Function that writes total amount of borrowed books
def total_amount(amt):
    total_str02 = "Total amount for borrowed books are $", amt
    file_d = open(n1.name_user + n1.b_code + ".txt", "a")  # appending the total amount in the Borrowed file
    file_d.writelines(total_str02)
    file_d.writelines("\n")
    file_d.writelines("------------------------------------------------------------")
    file_d.writelines("\n")
    file_d.close()


# Function that writes the name of the returning book
def return_book_name(re_name):
    book_name02 = "Name of the books: ", re_name
    file_r = open(borrower + code_re + " return.txt", "a")
    file_r.writelines(book_name02)
    file_r.writelines("\n")
    file_r.close()


# Function that reads the first line i.e. 0 index from borrower file
def borrower_to_return():
    file_open01 = open(borrower + code_re + ".txt", "r")
    file_001 = file_open01.readlines()
    file_0 = file_001[0]
    file_0_str = str(file_0)
    file_open01.close()
    return file_0_str


# Function that reads lines except the first lines from borrower file
def borrower_to_return2():
    file_open01 = open(borrower + code_re + ".txt", "r")
    file_001 = file_open01.readlines()
    file_1 = file_001[1:-1]
    file_1_str = str(file_1)
    file_open01.close()
    return file_1_str


# Function that read Function that reads lines except the first lines from returner file
def double_return():
    file_open200 = open(borrower + code_re + " return.txt", "r")
    file_200 = file_open200.readlines()
    file_201_str = str(file_200)
    file_open200.close()
    return file_201_str


print("                              ** WELCOME TO IIC LIBRARY **                              ")
print("         -----------------------------------------------------------------------         ")

c = True
while c:
    print('''
Enter D: to display all the available books
Enter B: to borrow books from the library
Enter R: to return books from the library
Enter E: to exit the library
''')

    # asking user for information
    ask_user = input("Enter your choice: ").upper()
    print("\n")

    if ask_user == "D":
        print("| Available books for you |\n")
        book1.display()
        book2.display()
        book3.display()
        book4.display()
        book5.display()
        book6.display()
        continue  # Choice to display/borrow/return/exit are shown again

    # Borrowing books
    elif ask_user == "B":
        print("                              [Borrowing section]                             ")
        print("         -----------------------------------------------------------------------         ")
        print("Borrow from available books displayed above")
        condition = False
        borrow_again = True
        name = input("Enter your name: ")
        print('''Note: 
        You can set your own borrowing code. As your data needs to be stored in a unique file so this code 
        should be unique for example: ram1, SI32, Com11 etc. Borrowing code is very important since it is 
        required while returning book so do not lose it!
        ''')
        ''' code variable is created to store each user data separately even if the same user wants to 
        borrow or return the book for better management '''
        code = input("Enter a borrowing code for yourself: ")
        n1 = BName(name, code)
        n1.borrower_name_code()
        # Total variable is created to store amount of total book borrowed
        total = 0
        while borrow_again:
            ask_user2 = input("Enter book name to borrow: ")
            # Comparing the book searched by user with the books available in library
            if ask_user2 == book1.name:
                b1 = BBname(ask_user2)
                if int(book1.quantity) >= 1:  # Checking the quantity of book
                    print("Book is available")
                    b1.func_user()
                    total += int(book1.price)
                    quantity = int(book1.quantity)
                    quantity -= 1
                    quantity_str = str(quantity)
                    book1.quantity = quantity_str
                    condition = True
                else:
                    print("Book is out of stock. Please visit later.")
            elif ask_user2 == book2.name:
                b1 = BBname(ask_user2)
                if int(book2.quantity) >= 1:
                    print("Book is available")
                    b1.func_user()
                    total += int(book2.price)
                    quantity1 = int(book2.quantity)
                    quantity1 -= 1
                    quantity_str1 = str(quantity1)
                    book2.quantity = quantity_str1
                    condition = True
                else:
                    print("Book is out of stock. Please visit later.")
            elif ask_user2 == book3.name:
                b1 = BBname(ask_user2)
                if int(book3.quantity) >= 1:
                    print("Book is available")
                    b1.func_user()
                    total += float(book3.price)
                    quantity2 = int(book3.quantity)
                    quantity2 -= 1
                    quantity_str2 = str(quantity2)
                    book3.quantity = quantity_str2
                    condition = True
                else:
                    print("Book is out of stock. Please visit later.")

            elif ask_user2 == book4.name:
                b1 = BBname(ask_user2)
                if int(book4.quantity) >= 1:
                    print("Book is available")
                    b1.func_user()
                    total += float(book4.price)
                    quantity3 = int(book4.quantity)
                    quantity3 -= 1
                    quantity_str3 = str(quantity3)
                    book4.quantity = quantity_str3
                    condition = True
                else:
                    print("Book is out of stock. Please visit later.")

            elif ask_user2 == book5.name:
                b1 = BBname(ask_user2)
                if int(book5.quantity) >= 1:
                    print("Book is available")
                    b1.func_user()
                    total += int(book5.price)
                    quantity4 = int(book5.quantity)
                    quantity4 -= 1
                    quantity_str4 = str(quantity4)
                    book5.quantity = quantity_str4
                    condition = True
                else:
                    print("Book is out of stock. Please visit later.")

            elif ask_user2 == book6.name:
                b1 = BBname(ask_user2)
                if int(book6.quantity) >= 1:
                    print("Book is available")
                    b1.func_user()
                    total += int(book6.price)
                    quantity5 = int(book6.quantity)
                    quantity5 -= 1
                    quantity_str5 = str(quantity5)
                    book6.quantity = quantity_str5
                    condition = True
                else:
                    print("Book is out of stock. Please visit later.")

            else:
                print("Sorry! The book you requested is not available.")
                condition = False

            # Asking if user is going to borrow more books
            print("Do you want to borrow more book?")
            asking_borrow = input("Enter Y for yes and N for no: ").lower()
            if asking_borrow == "y":
                continue
            else:
                borrow_again = False
        # Updating book information
        func_all()

        # calling function of time and date after for loop because it should be used one time only
        borrow_date_time()

        # Converting the total amount of book borrowed to string to write in a txt file
        total_str = str(total)
        total_amount(total_str)

        # borrower information is displayed
        if condition is True:  # Condition if book is available and borrowed
            borrow_file_read()
            print("\nYou have borrowed books from this library. Thank you for visiting!.\n")
        else:  # Condition if book is not available
            print("\nTry other available books.\n")
        continue  # Choice to display/borrow/return/exit are shown again

    # Returning books
    elif ask_user == "R":
        print("                              [Returning section]                             ")
        print("         -----------------------------------------------------------------------         ")
        print('''Note:
    Enter name of the borrower who borrowed the specific book which you are going to return.
    Time limitation for borrowed books is 10 days. So, if you failed to return the books within
    10days then fine is to be paid.
    ''')
        name02 = input("Enter your name: ")
        borrower = input("Enter borrower name: ")
        print('''Note: 
        Enter the borrowing code that you set while borrowing this book
        ''')
        code_re = input("Enter your borrowing code: ")
        name_fi = f"Name of the returner: {name02}"
        name_fi2 = f"Name of the borrower: {borrower}"
        code_re2 = f"Your borrowing code: {code_re}"
        # writing of the returner/borrower/borrowing code in file
        file_r1 = open(borrower + code_re + " return.txt", "a")
        condition02 = True
        return_again = True
        total2 = 0
        try:  # exceptional handling
            if code_re not in double_return():
                file_r1.writelines(name_fi)
                file_r1.writelines("\n")
                file_r1.writelines(name_fi2)
                file_r1.writelines("\n")
                file_r1.writelines(code_re2)
                file_r1.writelines("\n")
                file_r1.close()
                if borrower.lower() in borrower_to_return().lower():
                    while return_again:
                        book_name = input("Enter the name of the borrowed book: ")
                        if book_name.lower() in borrower_to_return2().lower():
                            if book_name == book1.name:
                                print("This book was borrowed.")
                                quantity = int(book1.quantity)
                                quantity += 1
                                quantity_str = str(quantity)
                                book1.quantity = quantity_str
                                total2 += int(book1.price)
                                condition02 = False

                            elif book_name == book2.name:
                                print("This book was borrowed.")
                                quantity1 = int(book2.quantity)
                                quantity1 += 1
                                quantity_str1 = str(quantity1)
                                book2.quantity = quantity_str1
                                total2 += int(book2.price)
                                condition02 = False

                            elif book_name == book3.name:
                                print("This book was borrowed.")
                                quantity2 = int(book3.quantity)
                                quantity2 += 1
                                quantity_str2 = str(quantity2)
                                book3.quantity = quantity_str2
                                total2 += int(book3.price)
                                condition02 = False

                            elif book_name == book4.name:
                                print("This book was borrowed.")
                                quantity3 = int(book4.quantity)
                                quantity3 += 1
                                quantity_str3 = str(quantity3)
                                book4.quantity = quantity_str3
                                total2 += int(book4.price)
                                condition02 = False

                            elif book_name == book5.name:
                                print("This book was borrowed.")
                                quantity4 = int(book5.quantity)
                                quantity4 += 1
                                quantity_str4 = str(quantity4)
                                book5.quantity = quantity_str4
                                total2 += int(book5.price)
                                condition02 = False

                            elif book_name == book6.name:
                                print("This book was borrowed.")
                                quantity5 = int(book6.quantity)
                                quantity5 += 1
                                quantity_str5 = str(quantity5)
                                book6.quantity = quantity_str5
                                total2 += int(book6.price)
                                condition02 = False
                            return_book_name(book_name)
                        else:
                            print("This book was not borrowed.")

                        # Asking if user is going to return more books
                        print("Do you want to return more book?")
                        asking_return = input("Enter Y for yes and N for no: ").lower()
                        if asking_return == "y":
                            continue
                        else:
                            return_again = False
                else:
                    condition02 = True
            else:
                print("You have already returned the book")
                continue
            # updating the book information
            func_all()

            # Date and time of book returned
            returning_date_time()

            # taking date from borrower books txt file
            file_read01 = borrower_to_return2()
            file_str = str(file_read01)
            dates = re.findall(r'\d{4}-\d{2}-\d{2}', file_str)
            dates_str = ' '.join(dates)
            date_format1 = datetime.datetime.strptime(dates_str, '%Y-%m-%d').date()
            # taking date from Returner txt file
            file_open_re = open(borrower + code_re + " return.txt", "r")
            file_read_re = file_open_re.read()
            dates_re = re.findall(r'\d{4}-\d{2}-\d{2}', file_read_re)
            dates_re2 = ' '.join(dates_re)
            date_format2 = datetime.datetime.strptime(dates_re2, '%Y-%m-%d').date()
            file_open_re.close()

            # Calculating borrowed and returning date to check if fine is charged or not
            number_of_days = 10
            fine = 1.5
            cc = True
            amount_with_fine = total2
            if condition02 is False:
                for ti in range(number_of_days):
                    total_days = date_format1 + datetime.timedelta(days=ti)
                    if date_format2 == total_days:
                        cc = True
                        print("You have return book in time so no fine is charged!")
                        total2_str = str(total2)
                        file_fine = "Your total amount is $" + total2_str
                        file_open_re11 = open(borrower + code_re + " return.txt", "a")
                        file_open_re11.write("You have return book in time so no fine is charged\n")
                        file_open_re11.write(file_fine)
                        file_open_re11.close()
                        return_file_read()
                        break
                    else:
                        cc = False

                if not cc:
                    print("You are late.")
                    count = int(input("How many days are you late to return the book: "))
                    for i in range(count):
                        amount_with_fine += fine
                    total_final = amount_with_fine
                    fine_str = str(total_final)
                    file_fine2 = "Your total amount with fine is $" + fine_str
                    file_open_re5 = open(borrower + code_re + " return.txt", "a")
                    file_open_re5.write("--------Fine is to be paid---------\n")
                    file_open_re5.write(file_fine2)
                    file_open_re5.close()
                    print("--------Fine is to be paid---------\n")
                    print(f"Your total amount with fine is ${fine_str}")
                    return_file_read()
            else:
                print("You have not borrowed any books from this library or you must have entered wrong name.")
            continue  # Choice to display/borrow/return/exit are shown again
        except FileNotFoundError:
            print("Enter correct borrower name.")
    elif ask_user == "E":
        exit()
    else:
        print("Enter valid choice.")
