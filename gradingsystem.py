import statistics

#-------------login------------
def login():
    admin_username = "admin"
    admin_password= "1234"

    username = input("Enter username: ")
    password=input("Enter password: ")

    if username == admin_username and password ==admin_password:
        print('login sucessfull!\n')
        return True
    else:
        print('Invalid credentials!\n')
        return False
    
   # -------- ADD STUDENT GRADES --------
def add_student(students):
    name = input("Enter student name: ")

    grades_input = input("Enter grades separated by space: ")
    grades = list(map(int, grades_input.split()))

    students[name] = grades
    print(f"Grades added for {name}\n")


# -------- REMOVE STUDENT --------
def remove_student(students):
    name = input("Enter student name to remove: ")

    if name in students:
        del students[name]
        print(f"{name} removed successfully\n")
    else:
        print("Student not found\n")


# -------- CALCULATE AVERAGE --------
def calculate_average(students):
    if not students:
        print("No student data available\n")
        return

    for name, grades in students.items():
        avg = statistics.mean(grades)
        print(f"{name}'s Average: {avg}")

    print()


# -------- MAIN MENU --------
def main():
    students = {}

    if not login():
        return

    while True:
        print("1. Add Student Grades")
        print("2. Remove Student")
        print("3. Calculate Average")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            remove_student(students)

        elif choice == "3":
            calculate_average(students)

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid choice\n")


# -------- RUN PROGRAM --------
main()


'''
import statistics

admins = {'python':'pass123@', 'user2':'pass2'}

def main():
    print("""
    welcome to Grade Central

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    
    """)
action = input('what would you like to do today?(Enter a number)')

if action == '1':
    print('1')
elif action == '2':
    print('2')
elif action == '3':
    print('3')
else:
    print('No valid choice was given, try again')

login = input('Username: ')
passw = input('password: ')


if login in admins:
    if admins[login]== passw:
        print('Welcome,', login)
        while True:
            main()
    else:
        print('Invalid password, will detonate in 5 seconds!')
else:
    print('Invalid username, calling the FBI to report this')
'''
