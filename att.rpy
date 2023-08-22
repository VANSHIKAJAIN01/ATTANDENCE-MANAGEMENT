# Attendance Management Project

# Initialize dictionaries to store data
users = {'admin': 'admin123'}
employees = {}
attendance_records = {}

# Function to authenticate users
def login():
    username = input("Username: ")
    password = input("Password: ")
    
    if username in users and users[username] == password:
        return True
    else:
        print("Invalid credentials")
        return False

# Function to add employee information
def add_employee():
    emp_id = input("Enter employee ID: ")
    emp_name = input("Enter employee name: ")
    employees[emp_id] = emp_name
    attendance_records[emp_id] = {}

# Function to mark attendance
def mark_attendance():
    emp_id = input("Enter employee ID: ")
    if emp_id in employees:
        date = input("Enter date (YYYY-MM-DD): ")
        attendance_status = input("Present (P) or Absent (A): ").upper()
        
        if date not in attendance_records[emp_id]:
            attendance_records[emp_id][date] = attendance_status
            print("Attendance marked successfully.")
        else:
            print("Attendance already marked for this date.")
    else:
        print("Employee not found.")

# Function to view attendance records
def view_attendance():
    emp_id = input("Enter employee ID: ")
    if emp_id in employees:
        print(f"Attendance records for {employees[emp_id]}:")
        for date, status in attendance_records[emp_id].items():
            print(f"{date}: {status}")
    else:
        print("Employee not found.")

# Function to generate attendance report
def generate_report():
    emp_id = input("Enter employee ID: ")
    if emp_id in employees:
        print(f"Attendance report for {employees[emp_id]}:")
        for date, status in attendance_records[emp_id].items():
            print(f"{date}: {status}")
    else:
        print("Employee not found.")

# Main loop
while True:
    print("\nAttendance Management System")
    print("1. Login")
    print("2. Add Employee")
    print("3. Mark Attendance")
    print("4. View Attendance Records")
    print("5. Generate Attendance Report")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        if login():
            print("Login successful!")
        else:
            print("Login failed!")
    elif choice == '2':
        add_employee()
    elif choice == '3':
        mark_attendance()
    elif choice == '4':
        view_attendance()
    elif choice == '5':
        generate_report()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select again.")
