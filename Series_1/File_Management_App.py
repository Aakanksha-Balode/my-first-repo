# sample.txt
#This is a new content

# write.py
#file = open('sample.txt', 'w')
#file.write('hello ji! this is python')
#file.close()

# read.py
#file = open('sample.txt', 'r')
#content = file.read()
#file.close()
#print(f"content of 'sample.txt':{content}")
# app.py
import os
def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"file name {filename}: created successfully!")
    except FileExistsError:
        print(f'file name {filename} already exists!')

    except Exception as E:
        print('an error occured!')

def view_all_files():
    files = os.listdir()
    if not files:
        print('no file found!')

    else:
        print('files in directory!')
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')

    except FileNotFoundError:
        print('File not found')

    except Exception as e:
        print('an error occurred!')


def read_file(filename):
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f"content of '{filename}' :\n{content}")


    except FileNotFoundError:
            print(f"{filename} doesn't exist!")

    except Exception as e:
            print('an error occurred!')


def edit_file(filename):
    try:
        with open('sample.txt', 'a') as f:
            content = input('Enter data to add = ')
            f.write(content + "\n")
            print('Content added to {filename} Successfully!')


    except FileNotFoundError:
            print(f"{filename} doesn't exist!")

    except Exception as e:
            print('an error occurred!')


def main():
    while True:
        print('File Management App')
        print('1. Create file')
        print('2. View all files')
        print('3. Delete file')
        print('4. Read file')
        print('5. Edit file')
        print('6. Exit')


        choice = input('enter your choice(1-6) = ')

        if choice == '1':
            filename = input("Enter the file-name to create = ")
            creat_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input('Enter the name of file you want = ')
            delete_file(filename)


        elif choice == '4':
            filename = input('Enter file name to read = ')
            read_file(filename)

        elif choice == '5':
            filename = input('enter file name to edit = ')
            edit_file(filename)

        elif choice == '6':
            print('Closing the app....')
            break

        else:
            print('In-valid syntax')


if __name__ == "__main__":
    main()





        
