import models as md
import datetime as dt

books_path = "/Users/harshitsingh/Developer/Python_Project_Bank/data/books.txt"
members_path = "/Users/harshitsingh/Developer/Python_Project_Bank/data/members.txt"
log_path = "/Users/harshitsingh/Developer/Python_Project_Bank/data/activity.txt"

books_list = []
members_list = []
log_entries = []


def load_data():
    books_list.clear()
    members_list.clear()
    log_entries.clear()

    # Load Books
    with open(books_path, "r") as file:
        for line in file:
            split = line.strip().split(",")
            if len(split) == 4:
                books_list.append(md.Book(split[0], split[1], split[2], split[3]))

    # Load Members
    with open(members_path, "r") as file:
        for line in file:
            split = line.strip().split(",")
            if len(split) == 3:
                members_list.append(md.Member(split[0], split[1], split[2]))

    # Load Logs
    with open(log_path, "r") as file:
        for line in file:
            log_entries.append(line.strip())


def save_data():
    with open(books_path, "w") as file_book:
        for eachObj in books_list:
            file_book.write(str(eachObj))

    with open(members_path, "w") as file_members:
        for eachObj in members_list:
            file_members.write(str(eachObj))


def write_log(category, isbn, member_id):
    with open(log_path, "a") as file:
        res = f"{dt.datetime.now()} | {category} | ISBN: {isbn} | Member ID: {member_id}\n"
        file.write(res)


class LibrarySystem:

    @staticmethod
    def issue_book(isbn, member_id):
        load_data()
        book_found = False
        for book in books_list:
            if book.isbn == isbn and book.is_available.lower() == "true":
                book.is_available = "false"
                book_found = True
                break

        if not book_found:
            print("Book is unavailable. Thank you!")
            return

        for member in members_list:
            if member.member_id == member_id:
                if member.borrowed_books_isbns.lower() != "none":
                    member.borrowed_books_isbns += ";" + isbn
                else:
                    member.borrowed_books_isbns = isbn

                write_log("ISSUE", isbn, member_id)
                save_data()
                print("Book issued successfully.")
                return

        print("Member does not exist.")

    @staticmethod
    def return_book(isbn, member_id):
        load_data()

        for book in books_list:
            if book.isbn == isbn:
                book.is_available = "true"
                break

        for member in members_list:
            if member.member_id == member_id:
                lst = member.borrowed_books_isbns.split(";")
                if isbn in lst:
                    lst.remove(isbn)
                member.borrowed_books_isbns = ";".join(lst) if lst else "none"

        write_log("RETURN", isbn, member_id)
        save_data()
        print("Book returned successfully.")

    @staticmethod
    def add_new_book(title, author, isbn, is_available):
        load_data()
        books_list.append(md.Book(title, author, isbn, is_available))
        save_data()
        print("Book added successfully.")

    @staticmethod
    def add_new_member(member_id, name, borrowed_books_isbn):
        load_data()
        members_list.append(md.Member(member_id, name, borrowed_books_isbn))
        save_data()
        print("Member added successfully.")

    @staticmethod
    def viewTransaction():
        load_data()
        logs = list(reversed(log_entries))
        for i in range(min(10, len(logs))):
            print(logs[i])

    @staticmethod
    def viewAll_Books():
        load_data()
        for book in books_list:
            print(
                f"\nTitle: {book.title}"
                f"\nAuthor: {book.author}"
                f"\nISBN: {book.isbn}"
                f"\nAvailability: {book.is_available}"
            )