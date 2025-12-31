import library_manager

while(True):
    print("\n--- THE HERITAGE ARCHIVE ---")
    print("1. View All Books")
    print("2. Register New Member")
    print("3. Add new Book")
    print("4. Issue a Book")
    print("5. Return a Book")
    print("6. View Transaction History")
    print("7. EXIT")
    ch = int(input("Enter Choice: "))
    if(ch==1):
        print("\n--- VIEW ALL BOOKS ---")
        library_manager.LibrarySystem.viewAll_Books()

    if(ch==2):
        print("\n--- ADD NEW MEMBER ---")
        member_id=input("Enter Member ID: ")
        name=input("Enter Name: ")
        library_manager.LibrarySystem.add_new_member(member_id,name,"NONE")
    
    elif(ch==3):
        print("\n--- ADD NEW BOOK ---")
        title=input("Enter Title: ")
        author=input("Enter Author: ")
        isbn = input("Enter ISBN: ")
        library_manager.LibrarySystem.add_new_book(title,author,isbn,"true")

    elif(ch==4):
        print("\n--- ISSUE A BOOK ---")
        isbn = input("Enter ISBN: ")
        member_id = input("Enter Member ID:")
        library_manager.LibrarySystem.issue_book(isbn,member_id)

    elif(ch==5):
        print("\n --- RETURN BOOK ---")
        isbn = input("Enter ISBN: ")
        member_id = input("Enter Member ID: ")
        library_manager.LibrarySystem.return_book(isbn,member_id)

    elif(ch==6):
        print("\n --- TRANSACTION HISTORY ---")
        library_manager.LibrarySystem.viewTransaction()

    elif(ch==7):
        print("HAVE A GREAT DAY")
        break
