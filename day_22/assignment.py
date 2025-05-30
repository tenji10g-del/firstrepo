import os

dirname = ""
filename = ""
filepath = ""

def make_directory():
    global dirname
    dirname = input("Enter directory name: ")
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print("Directory created.")
    else:
        print("Directory already exists.")

def make_file():
    global filename, filepath
    if dirname == "":
        print("Please create a directory first.")
        return
    filename = input("Enter file name (example: example.txt): ")
    filepath = os.path.join(dirname, filename)
    text = input("Enter text to write in the file: ")
    with open(filepath, 'w') as f:
        f.write(text + '\n')
    print("File created and text written.")

def read_file():
    if filepath == "":
        print("No file found. Please create a file first.")
        return
    with open(filepath, 'r') as f:
        print("File content:")
        print(f.read())

def update_file():
    if filepath == "":
        print("No file found.")
        return
    text = input("Enter text to append: ")
    with open(filepath, 'a') as f:
        f.write(text + '\n')
    print("Text appended.")

def get_paths():
    if filepath == "":
        print("No file found.")
        return
    print("Current Working Directory:", os.getcwd())
    print("Full File Path:", os.path.abspath(filepath))

def get_name_size():
    if filepath == "":
        print("No file found.")
        return
    print("File Name:", os.path.basename(filepath))
    print("File Size:", os.path.getsize(filepath), "bytes")

def get_extension():
    if filepath == "":
        print("No file found.")
        return
    _, ext = os.path.splitext(filepath)
    print("File Extension:", ext)

def delete_file():
    global filepath
    if filepath == "":
        print("No file found.")
        return
    os.remove(filepath)
    print("File deleted.")
    filepath = ""

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Make a directory")
        print("2. Make a file and write to it")
        print("3. Read the file")
        print("4. Update the file")
        print("5. Show current working directory and file path")
        print("6. Show file name and size")
        print("7. Show file extension")
        print("8. Delete the file")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            make_directory()
        elif choice == '2':
            make_file()
        elif choice == '3':
            read_file()
        elif choice == '4':
            update_file()
        elif choice == '5':
            get_paths()
        elif choice == '6':
            get_name_size()
        elif choice == '7':
            get_extension()
        elif choice == '8':
            delete_file()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

menu()
