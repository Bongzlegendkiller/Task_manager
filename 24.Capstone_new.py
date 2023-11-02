# import datetime module
from datetime import datetime
# list to store user credentials
credentials = []
# dict to store CURRENT user credentials
current_username = ""
# Date time format
date_format = "%d" " %b " "%Y"
# list to store all tasks
loaded_tasks_all = []
# dict to store all tasks
loaded_tasks_all_formatted = {}
# dict to store user's tasks
loaded_tasks_mine_formatted = {}
# loads/reads tasks into memory

def load_tasks():
    task_id = 0
    if len(loaded_tasks_all) > 0:
        loaded_tasks_all.clear()
    # Open the "tasks.txt" file in read mode
    with open("tasks.txt", "r") as file_tasks:     
            # Read all the lines from the file and store them in a list
            tasks = file_tasks.readlines()
            for task in tasks:
                loaded_tasks_all.append(task)
                task_id += 1
                task_items = task.strip().split(", ")
                task_ob = f'''
Task ID: #{task_id}
    Task: {task_items[1]} | Task complete? {task_items[5]}
    Assigned to: {task_items[0]} | Due date: {task_items[4]}
-------------
    Task description:
    {task_items[2]}
'''
                loaded_tasks_all_formatted.update({task_id: task_ob})                
                if task_items[0].lower() == current_username.lower():
                    loaded_tasks_mine_formatted.update({task_id: task_ob})
    return True
    

def register_user():
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    re_password = input("Confirm new password: ")
    # Check if the new password and confirmed password match
    if new_password != re_password:
        # Display an error message if the passwords don't match
        print("Passwords do not match. Please try again.")
    else:
        # Open the "user.txt" file in append mode
        with open("user.txt", "a") as file_users:
            # Write the new username and password to the file
            file_users.write(f"\n{new_username}, {new_password}")
            # Display a success message
        print("User registration successful.")


# function to add a new task
def add_task():
    # Prompt the user to enter the username of the assigned task
    user_task = input("Enter username of assigned task: ")
    # Prompt the user to enter the title of the task
    tasks = input("Enter title of task: ")
    # Prompt the user to enter the task description
    task_des = input("Enter task description: ")
    # Set the default completion status of the task to "No"
    complete = "No"
    # Get the current date in the format "yyyy-mm-dd"
    current_date = datetime.today().strftime("%d" " %b " "%Y")
    # Prompt the user to enter the due date of the task
    due_date = input("Enter due date (Example: 10 Oct 2019): ")
    # Open the "tasks.txt" file in append mode
    with open("tasks.txt", "a") as file_tasks:
        # Write the task details to the file
        file_tasks.write(f"\n{user_task}, {tasks}, {task_des}, {due_date}, {current_date}, {complete}")
    # Display a success message
    print("Task added successfully.")


# function to view all tasks
def view_all():
    # update task list and print
    response = load_tasks()
    for task in loaded_tasks_all_formatted.values():
        print(task)


# function to view assigned tasks
def view_mine():
    # update task list and print
    response = load_tasks()
    for task in loaded_tasks_mine_formatted.values():
        print(task)
    print("Enter [Task ID] to Edit\nEnter '-1' to Continue...\n")
    select_task = int(input("> "))
    for task_id in loaded_tasks_mine_formatted.keys():
        if select_task == task_id:
            edit_task(task_id)


# edit a task selected
def edit_task(task_id):
    updated_task_list = []
    print("Selected Task ID: ", task_id)
    print("Enter (1) - 'Edit Task Assignee'\nEnter (2) - 'Edit Task Due Date'\nEnter (3) - 'Mark Task as Completed'")
    selection = input("> ")

    if selection == "1":
        task_id_file = 0
        with open("tasks.txt", "r") as file_tasks:
            # Read all the lines from the file and store them in a list
            tasks = file_tasks.readlines()
            for task_file in tasks:
                task_id_file += 1
                task_items = task_file.strip().split(", ")
                if task_id_file == task_id:                    
                    print("Editing Assignee...")
                    print("Current Assignee: ", task_items[0])
                    update_assignee = input("New Assignee Name: \n> ")
                    if update_assignee != task_items[0]:
                        updated_task_list.append(f"{update_assignee}, {task_items[1]}, {task_items[2]}, {task_items[3]}, {task_items[4]}, {task_items[5]}")
                else:
                    updated_task_list.append(f"{task_items[0]}, {task_items[1]}, {task_items[2]}, {task_items[3]}, {task_items[4]}, {task_items[5]}")
        with open("tasks.txt", "w") as file_tasks:            
            for task in updated_task_list:
                file_tasks.write(task + "\n")

    elif selection == "2":
        task_id_file = 0
        with open("tasks.txt", "r") as file_tasks:
            # Read all the lines from the file and store them in a list
            tasks = file_tasks.readlines()
            for task_file in tasks:
                task_id_file += 1
                task_items = task_file.strip().split(", ")
                if task_id_file == task_id:              
                    print("Editing Due Date...")
                    print("Current Due Date: ", task_items[4])
                    update_date = input("Enter due date (Example: 10 Oct 2019): ")
                    if update_date != task_items[4]:
                        updated_task_list.append(f"{task_items[0]}, {task_items[1]}, {task_items[2]}, {task_items[3]}, {update_date}, {task_items[5]}")
                else:
                    updated_task_list.append(f"{task_items[0]}, {task_items[1]}, {task_items[2]}, {task_items[3]}, {task_items[4]}, {task_items[5]}")
        with open("tasks.txt", "w") as file_tasks:
            for task in updated_task_list:
                file_tasks.write(task + "\n")

    elif selection == "3":
        task_id_file = 0
        with open("tasks.txt", "r") as file_tasks:
            # Read all the lines from the file and store them in a list
            tasks = file_tasks.readlines()
            for task_file in tasks:
                task_id_file += 1
                task_items = task_file.strip().split(", ")
                if task_id_file == task_id:
                    if task_items[5].lower() != "yes":
                        update_complete = "Yes"
                        if update_complete != task_items[5]:
                            updated_task_list.append(f"{task_items[0]}, {task_items[1]}, {task_items[2]}, {task_items[3]}, {task_items[4]}, {update_complete}")
                            print("Marked Task as Completed!\n Enter any key to continue...")
                            input()
                    else:
                        print("Task is Already Marked Complete!\n Enter any key to continue...")
                        input()
                else:
                    updated_task_list.append(f"{task_items[0]}, {task_items[1]}, {task_items[2]}, {task_items[3]}, {task_items[4]}, {task_items[5]}")
        with open("tasks.txt", "w") as file_tasks:
            for task in updated_task_list:
                file_tasks.write(task + "\n")


# function to generate user report
def generate_user_report():
    # Ensure text file is not going to be appended duplicate data
    with open("user_overview.txt", "w") as default_user_report:
        default_user_report.write("")
    # Retrieve a list of tasks by calling the view_all() function
    load_tasks()
    # Open the "user.txt" file in read mode
    with open("user.txt", "r") as user:
        # Read the contents of the file and split it into a list of users
        users = user.read().split("\n")
        # Iterate through each user in the list
        for user in users:
            # Split the user entry into username and additional info
            username = user.split(", ")
            # Counters for task statistics
            total_tasks = 0
            total_completed = 0
            total_incomplete = 0
            total_overdue = 0
            # Iterate through each task
            for task in loaded_tasks_all:
                # Split the task into individual values
                task_values = task.split(", ")
                # Check if the task is assigned to the current user
                if task_values[0].lower() == username[0].lower():
                    # Increment the total task count
                    total_tasks += 1
                    # Check if the task is completed
                    if task_values[5].lower() == "yes":
                        # Increment the completed task count
                        total_completed += 1
                    elif task_values[5].lower() == "no":
                        # Increment the incomplete task count
                        total_incomplete += 1
                    # Get the current date
                    current_date = datetime.today()
                    # Get the task's due date
                    due_date = task_values[4]
                    # Check if the task is overdue
                    if current_date > datetime.strptime(due_date, date_format):
                        # Increment the overdue task count
                        total_overdue += 1
            # Calculate the percentages for each task category
            percentage_total = round((total_tasks / len(loaded_tasks_all))*100, 2)
            percentage_completed = round((total_completed / len(loaded_tasks_all))*100, 2)
            percentage_incomplete = round((total_incomplete / len(loaded_tasks_all))*100, 2)
            percentage_overdue = round((total_overdue / len(loaded_tasks_all))*100, 2)
            # Create the output string for the user report
            output = f'''
User: {username[0]}
    Total Assigned Tasks: {total_tasks} | {percentage_total}%
    Completed Tasks: {total_completed} | {percentage_completed}%
    Incomplete Tasks: {total_incomplete} | {percentage_incomplete}%
    Overdue Tasks: {total_overdue} | {percentage_overdue}%
'''
            with open("user_overview.txt", "a") as file_task_overview_write:
                file_task_overview_write.write(output)


# function to generate task report
def generate_task_report():
    # counter for tasks statistics
    load_tasks()
    generate = len(loaded_tasks_all)
    count = 0
    tasks_incomplete = 0
    tasks_complete = 0
    task_overdue = 0
    # Iterate through each tasks
    for task in loaded_tasks_all:
        # Split task details
        task_items = task.strip().split(", ")
        count += 1
        # Check if task is incomplete
        if task_items[5].lower() == "no":
            tasks_incomplete += 1
        else:
            # Increment completed task count
            tasks_complete += 1
        # Get current date
        current_date = datetime.today()
        # Get task due date
        due_date = task_items[4]
        # Check if task is overdue
        if current_date > datetime.strptime(due_date, date_format):
            task_overdue += 1
    # Calculate percentages
    percentage_incomplete = round((tasks_incomplete / generate)*100, 2)
    percentage_complete = round((tasks_complete / generate)*100, 2)
    percentage_overdue = round((task_overdue / generate)*100, 2)
    # 
    output = f'''TASK OVERVIEW:
Total Tasks: {generate},
Incomplete Tasks(%): {percentage_incomplete} %,
Complete Tasks(%): {percentage_complete} %,
Overdue Tasks(%): {percentage_overdue} %    
'''
    # Write task report to file
    with open("task_overview.txt", "w") as file_task_overview:
        file_task_overview.write(output)


# Function to display reports
def display_report():
    try:
        # Read and display task report
        with open("task_overview.txt", "r") as file_task_overview:
            print(file_task_overview.read())
        # Read and display user report
        with open("user_overview.txt", "r") as read_overview:
            print(read_overview.read())

    except:
        print("File Does Not Exist:", FileNotFoundError)
        # Generate user report if file doesn't exist
        generate_user_report()
        # Generate task report if file doesn't exist
        generate_task_report()

# login section


while True:
    user_attempt = input("Please enter username: ")
    password_attempt = input("Please enter password: ")
 
    user_found = False
    # Read user credentials
    with open("user.txt", "r") as file_users:
        users_credentials = file_users.read().split('\n')
        # Iterate over each username and password in user credentials
        for users_username_password in users_credentials:
            tmp = users_username_password.split(', ')
            credentials.append(tmp)

        for username_password in credentials:
            # Check if username and password match
            if user_attempt == username_password[0] and password_attempt == username_password[1]:
                user_found = True
                current_username = user_attempt.strip()
                break

        if user_found:
            print("Welcome")
            print("Logged in as:", username_password[0])
            while True:
                if username_password[0] == "admin":
                    menu = input('''Select one of the following options:
                                a - Add a task
                                r - Register User
                                va - View all tasks
                                vm - View my tasks
                                gr - Generate reports
                                ds - Display statistics
                                e - Exit
                                : ''').lower()
                else:
                    menu = input('''Select one of the following options:
                                  a - Add a task
                                  va - View all
                                  vm - View my tasks                             
                                  e - Exit
                                  : ''').lower()
                if menu == "r":
                    # Call register_user() function
                    if str(username_password[0]).lower() != "admin":
                        print("You do not have the necessary permissions!")
                    else:
                        register_user()
                elif menu == "a":
                    # Call add_task() function
                    add_task()
                elif menu == "va":
                    view_all()
                elif menu == "vm":
                    load_tasks()
                    view_mine()
                elif menu == "gr":
                    if str(username_password[0]).lower() == "admin":
                        # Call generate_user_report() function
                        generate_user_report()
                        # Call generate_task_report() function
                        generate_task_report()
                    else:
                        print("You do not have the necessary permissions!")
                elif menu == "ds":
                    if username_password[0] != "admin":
                        print("You do not have the necessary permissions!")
                    else:
                        display_report()
                    # Call display_report() function
                elif menu == "e":
                    print("Goodbye")
                    # Exit the program
                    exit()
                else:
                    print("Incorrect username or password. Try Again.")
                    # End
                    continue
