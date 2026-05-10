import sys

def opt():
    print("\n")
    print("""==== DREAMS FILE MANAGER ====
1. Read inspiring messages
2. Add a new inspiring message
3. Rewrite the entire file
4. Exit
    """)

while True:
    opt()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        file = open("dreams.txt", "r")
        content = file.read()
        print("\n--- Inspiring messages ---\n\n", content)
        file.close()
        continue
    elif choice == 2:
        new_message = input("Enter your new inspiring line: ")
        file = open("dreams.txt", "a")
        file.write(new_message)
        file.close()
        print("\nNew inspiring message added successfully!")
        continue
    elif choice == 3:
        print("Warning!!! This will overwrite the entire file.")
        confirm = input("Type YES to confirm: ").upper()
        if confirm == "YES":
            new = input("Write your new set of inspiring messages: ")
            file = open("dreams.txt", "w")
            file.write(new)
            file.close()
            print("\nFile has been overwritten.")
        else:
            print("\nOperation cancelled.")
            continue
        continue
    elif choice == 4:
        sys.exit()
        break
    else:
        print("\nInvalid option. Please try again.")
        continue