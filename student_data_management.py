import os

def accept_data():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    with open('student_data.txt', 'a') as file:
        file.write(f"{name},{roll}\n")

def display_data():
    if os.path.isfile('student_data.txt'):
        with open('student_data.txt', 'r') as file:
            for line in file:
                name, roll = line.strip().split(',')
                print(f"Name: {name}, Roll Number: {roll}")
    else:
        print("No student data found.")

def main():
    while True:
        print("\nMENU:")
        print("1. Accept Data")
        print("2. Display Data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            accept_data()
        elif choice == '2':
            display_data()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
