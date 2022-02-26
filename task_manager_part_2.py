# The program is for a small business.
# It will manage tasks and assign task to each member of the team.

# Date today import
from datetime import date
import datetime

# Empty list variables
task_output = []
user_output = []

# Empty variables
user_setlist = ""
pass_input = ""
message = ""
user_input = ""


# User defined function for main menu for admin
def display_menu_admin():
    global message
    # option choices that are displayed in the main menu
    option_sentence = input("Please select one of the following: \n"
                            "r - register task\n"
                            "a - add task\n"
                            "va - view all tasks\n"
                            "vm - view my tasks\n"
                            "gr - generate reports\n"
                            "ds - view statistics\n"
                            "e - exit\n"
                            "Enter your choice: \t")

    # List that checks for right input
    keyword_list = ["r", "a", "va", "vm", "gr", "ds", "e"]

    # Used to check if the right input is given
    for x in keyword_list:
        if x == option_sentence:
            message = option_sentence

    # Loops code until we receive the right input
    while option_sentence != message:
        option_sentence = input("Please select one of the following: \n"
                                "r - register task\n"
                                "a - add task\n"
                                "va - view all tasks\n"
                                "vm - view my tasks\n"
                                "gr - generate reports\n"
                                "ds - view statistics\n"
                                "e - exit\n"
                                "Enter your choice: \t")

        # Used to check if the right input is given
        for x in keyword_list:
            if x == option_sentence:
                message = option_sentence


# User defined function for main menu for user
def display_menu_user():
    global message
    # option choices that are displayed in the main menu
    option_sentence = input("Please select one of the following: \n"
                            "a - add task\n"
                            "va - view all tasks\n"
                            "vm - view my tasks\n"
                            "gr - generate reports\n"
                            "e - exit\n"
                            "Enter your choice: \t")

    # List that checks for right input
    keyword_list = ["a", "va", "vm", "gr", "e"]
    # Used to check if the right input is given
    for x in keyword_list:
        if x == option_sentence:
            message = option_sentence

    # Loops code until we receive the right input
    while option_sentence != message:
        option_sentence = input("Please select one of the following: \n"
                                "a - add task\n"
                                "va - view all tasks\n"
                                "vm - view my tasks\n"
                                "e - exit\n"
                                "Enter your choice: \t")

        # Used to check if the right input is given
        for x in keyword_list:
            if x == option_sentence:
                message = option_sentence


# User defined function to register new users to user.txt
def reg_user():
    # Added new users and passwords depending on the number of new users
    int(input("What is the number of input users? "))

    # We append the following details into tasks.txt and format it.
    with open("user.txt", "a") as f:
        new_user_input = input("Please enter new username: ")

        # We read the data we want from user.txt
        with open("user.txt", "r") as file:
            for i in file:

                # Looks for line that begins with new user_input
                # If true, we will need to enter a different username
                if i.startswith(f"{new_user_input}"):
                    print("Username is taken. "
                          "Please enter a different username.")
                    while i.startswith(f"{new_user_input}"):
                        new_user_input = input("Please enter new username: ")

                # If false, the new user_input name is registered
                if not i.startswith(f"{new_user_input}"):
                    user_name = new_user_input

        # Printed instruction messages to enter new password twice to confirm
        new_pass_input = input("Please enter new password: ")
        new_pass_input2 = input("Please enter new password again: ")

        # If passwords are mismatched, retry again
        if new_pass_input != new_pass_input2:
            print("Passwords do not match")
            while new_pass_input != new_pass_input2:
                new_pass_input = input("Please enter new password: ")
                new_pass_input2 = input("Enter new password again: ")

        # If passwords match, user and password are registered in user.txt
        if new_pass_input == new_pass_input2:
            password = new_pass_input
        user_password = f"{user_name}, {password}"
        f.write(f"\n{user_password}\n")
        return user_password


# User defined function to add new tasks to tasks.txt
def add_task():
    # We append the following details into tasks.txt and format it.
    with open("tasks.txt", "a") as task_add:
        user_task = input("Who is the task assigned to? ")
        title_task = input("Title of the task? ")
        description_task = input("Description of the task? ")
        date_assign_task = date.today()
        date_year = int(input("What year is the task for?\n"))
        date_month = int(input("What month is the task for?\n"
                               "Use number representation of month:\n"))
        date_day = int(input("What day is the task for?\n"))
        date_format = datetime.datetime(date_year, date_month, date_day)
        date_due_task = date_format.strftime("%Y-%m-%d")
        completed_task = "No"
        task_assignment = f"{user_task}, {title_task}, " \
                          f"{description_task}, {date_assign_task}, " \
                          f"{date_due_task}, {completed_task}"
        task_add.write(f"\n{task_assignment}")
        return task_assignment


# User defined function to view all tasks in tasks.txt
def view_all():
    # We read from the tasks.txt
    with open("tasks.txt", "r") as user_task_list:
        for task_line in user_task_list:
            task_line_strip = task_line.strip()
            task_output.append(task_line_strip)

    # FOR loop to put into task stringed list
    for i in task_output:
        # Turns i into a list format
        all_list_split = i.split(", ")

        # Prints all task details of the tasks.txt
        print("\n")
        print(f"Task: {all_list_split[1]}")
        print(f"Assigned to: {all_list_split[0]}")
        print(f"Date assigned: {all_list_split[3]}")
        print(f"Due date: {all_list_split[4]}")
        print(f"Task complete: {all_list_split[5]}")
        print(f"Task Description: {all_list_split[2]}")


# User defined function to view users' own tasks in tasks.txt
def view_mine():
    # We read from the tasks.txt
    with open("tasks.txt", "r") as user_task_list:
        for task_line in user_task_list:
            task_line_strip = task_line.strip()
            task_output.append(task_line_strip)

    # FOR loop to put into task stringed list
    for i in task_output:
        # Looks for line that begins with user_input
        if i.startswith(f"{user_input}"):
            # Turns i into a list format
            my_list_split = i.split(", ")

            # Prints all task details of the user
            print("\n")
            print(f"Task: {my_list_split[1]}")
            print(f"Assigned to: {my_list_split[0]}")
            print(f"Date assigned: {my_list_split[3]}")
            print(f"Due date: {my_list_split[4]}")
            print(f"Task complete: {my_list_split[5]}")
            print(f"Task Description: {my_list_split[2]}")

    # We read from the tasks.txt
    with open("tasks.txt", "r") as user_task_list:
        view_more = user_task_list.read()
        num_task = 0
        for task_line in user_task_list:
            task_line.strip().split(",")
            num_task += 1

    # Prints out instruction message and input commands
    ask_input = input("Do you want to edit a specific task "
                      "or do you want to exit to main menu? \n"
                      "Specific Task - (1)\n"
                      "Exit to main menu - (-1):\n")

    # Inner user defined function to edit certain tasks in tasks.txt
    def edit_file():
        # We format the task of our choice
        # and manipulate the task data inside file
        user_Task = taskFile[taskNum].strip().split(", ")
        new_state_assigned = taskFile[taskNum].strip() \
            .replace(user_Task[0], task_assigned).strip() \
            .replace(user_Task[4], task_due_date)
        final_string = view_more.replace(taskFile[taskNum].strip(),
                                         new_state_assigned)

        # We write our new task in place of the old task
        with open('tasks.txt', 'w') as edit_tasks:
            edit_tasks.write(f"{final_string}")

    # If statement that edits tasks in tasks.txt or exits to main menu
    if ask_input == "1":
        taskNum = int(input("Please enter the Task number?\n"))
        taskNum = taskNum - 1

        # We read tasks from tasks.txt
        with open('tasks.txt', 'r') as file:
            taskFile = file.readlines()
        for _ in taskFile:
            print(taskFile[taskNum] + "\n")
            break

        # Printed input message
        taskComplete = input("Has this task been completed?\n")

        # If choice is Yes, the chosen tasks are now marked complete
        if taskComplete == "Yes":
            userTask = taskFile[taskNum].strip().split(", ")
            new_state = taskFile[taskNum].strip() \
                .replace(userTask[5], taskComplete)
            updated_string = view_more.replace(taskFile[taskNum]
                                               .strip(), new_state)
            with open('tasks.txt', 'w') as f:
                f.write(updated_string)

        # If choice is No,
        # the chosen tasks assigned person and due date is changed
        elif taskComplete == "No":
            task_assigned = input("Enter new assigned name for task:\n")
            # New deadline for assignment completion
            print("Enter new due date:")
            date_year = int(input("What year is the task for?\n"))
            date_month = int(input("What month is the task for?\n"
                                   "Use number representation of month:\n"))
            date_day = int(input("What day is the task for?\n"))
            date_format = datetime.datetime(date_year, date_month, date_day)
            task_due_date = date_format.strftime("%Y-%m-%d")

            edit_file()

    # Returns to main menu
    elif ask_input == "-1":
        if user_input == "admin":
            display_menu_admin()
        if user_input != "admin":
            display_menu_user()


def generate_reports():

    # TASK OVERVIEW CODE LOGIC

    # count variable
    # Various (empty) variables
    new_task_count = 0
    completed_count = 0
    not_completed_count = 0
    new_line_list = []

    with open("tasks.txt", "r") as task_file:
        # Integer and list variables
        no_completed_count = 0
        task_overdue = 0
        new_count_list = []

        # prints out lines in task_file that are not empty
        for line in task_file:
            new_task_count += 1
            new_line_strip = line.strip()
            new_line_list.append(new_line_strip)
            # Creates list for lines in task_file4
            new_count_strip = line.strip()
            new_count_list.append(new_count_strip)

        # FOR loop to put into task stringed list
        for q in new_line_list:
            all_q_split = q.split(", ")
            # The total number of completed tasks.
            if "Yes" in all_q_split:
                completed_count += 1

            # The total number of uncompleted tasks.
            if "No" in all_q_split:
                not_completed_count += 1

        # FOR loop to put into task stringed list
        for d in new_count_list:
            all_d_split = d.split(", ")
            due_date = all_d_split[4]
            new_due_date = str(due_date)
            new_date_today = str(date.today())

            # Compares due date and today date using operators
            result = new_due_date < new_date_today

            # Total count of tasks not complete
            if "No" in all_d_split:
                no_completed_count += 1

                # Total number of tasks that aren’t completed and are overdue
                if "No" in all_d_split and result:
                    task_overdue += 1

    # The percentage of tasks that are incomplete.
    incomplete_tasks_percent = (no_completed_count / new_task_count) * 100

    # The percentage of tasks that are overdue.
    overdue_tasks_percent = (task_overdue / new_task_count) * 100

    # Writes total number of completed and uncompleted tasks
    with open("task_overview.txt", "w") as task:
        task.write(f"Total number of task is {new_task_count}\n")
        task.write(f"Total number of completed task is {completed_count}\n")
        task.write(f"Total number of uncompleted "
                   f"task is {not_completed_count}\n")
        task.write(f"Total number of overdue "
                   f"and uncompleted task are {task_overdue}\n")
        task.write(f"Total number of uncompleted tasks "
                   f"are {incomplete_tasks_percent}%\n")
        task.write(f"Total number of overdue tasks are "
                   f"{overdue_tasks_percent}%\n")

    # USER OVERVIEW CODE LOGIC

    # The total number of users registered
    with open("user.txt", "r") as user_file1:
        # count variable
        count_user = 0
        # Counts number of lines that aren't empty lines
        for a in user_file1:
            if a != "\n":
                count_user += 1

    # The total number of tasks
    with open("tasks.txt", "r") as user_file2:
        # count variable and list variables
        count_task = 0
        count_name = 0
        is_completed_count = 0
        to_be_completed_count = 0
        overdue_user_count = 0
        new_task_list = []

        # Counts number of lines that aren't empty lines
        for line in user_file2:
            if line != "\n":
                count_task += 1

            # Total number of tasks for that user
            if line.startswith(f"{user_input}"):
                count_name += 1

            # Percentage of tasks for that user from all tasks
            task_user_percentage = (count_name / count_task) * 100

            # Lines from user_file in a list format
            new_user_strip = line.strip()
            new_task_list.append(new_user_strip)

        # Objects in list
        for q in new_task_list:
            all_q_split = q.split(", ")
            due_date = all_q_split[4]
            new_due_date = str(due_date)
            new_date_today = str(date.today())

            # Compares due date and today date using operators
            result = new_due_date < new_date_today
            if q.startswith(f"{user_input}"):

                # User tasks that are complete
                if "Yes" in all_q_split:
                    is_completed_count += 1

                # User tasks that are incomplete
                if "No" in all_q_split:
                    to_be_completed_count += 1

                # User tasks that are overdue and incomplete
                if "No" in all_q_split and result:
                    overdue_user_count += 1

        if count_name != 0:

            # percentage of tasks assigned to user are completed
            completed_tasks_user = (is_completed_count / count_name) * 100

            # percentage of tasks assigned to user aren't completed
            not_completed_tasks_user = (to_be_completed_count /
                                        count_name) * 100

            # percentage of tasks assigned to user are overdue and incomplete
            overdue_tasks_user = (overdue_user_count / count_name) * 100
        elif count_name == 0:

            # percentage of tasks assigned to user are completed
            completed_tasks_user = 0

            # percentage of tasks assigned to user aren't completed
            not_completed_tasks_user = 0

            # percentage of tasks assigned to user are overdue and incomplete
            overdue_tasks_user = 0

    # Writes all of user_overview.txt information
    with open("user_overview.txt", "w") as user1:

        # Total number of registered users in user.txt
        user1.write(f"Total number of registered users are {count_user}\n")

        # Total number of task in tasks.txt
        user1.write(f"Total number of task are {count_task}\n")

        # Total number of tasks assigned to user
        user1.write(f"Total number of tasks for "
                    f"{user_input} are {count_name}\n")

        # Percentage of tasks for that user from all tasks
        user1.write(f"Total percentage of tasks for "
                    f"{user_input} is {task_user_percentage}%\n")

        # percentage of tasks assigned to user are complete
        user1.write(f"Total percentage of tasks completed "
                    f"by {user_input} is {completed_tasks_user}%\n")

        # percentage of tasks assigned to user are incomplete
        user1.write(f"Total percentage of tasks not completed "
                    f"by {user_input} is {not_completed_tasks_user}%\n")

        # percentage of tasks assigned to user are overdue and incomplete
        user1.write(f"Total percentage of tasks that are "
                    f"overdue and not completed by {user_input} "
                    f"is {overdue_tasks_user}%\n")

    return


# User defined function to view all stats of tasks and users
def all_stats():
    # Reads from task.overview.txt
    with open("task_overview.txt", "r") as f1:
        content_task = ""
        print("The below are the statistics from the task_overview: \n")
        # Prints out contents of task_overview.txt
        for x in f1:
            content_task += x
        print(content_task)

    # Reads from user_overview.txt
    with open("user_overview.txt", "r") as f2:
        content_user = ""
        print("The below are the statistics from the user_overview: \n")
        # Prints out contents of user_overview.txt
        for y in f2:
            content_user += y
        print(content_user)


# User List
# Read the user.txt file
with open("user.txt", "r") as user_pass_list:
    for user_line in user_pass_list:
        user_line_strip = user_line.strip()
        user_output.append(user_line_strip)
        user_setlist = user_output

    # LOGIN CODE
    # We read username and password from file
    # Enter username.
    # If wrong username is given, and error message will print
    user_input = input("Please enter username: ")

    # We set the False value to Login variable
    login = False

    # FOR loop to read list items
    for j in user_setlist:
        split_j = j.split(", ")
        if user_input == split_j[0]:
            login = True
            break

    # While loop conditions for login
    while not login:
        print("Wrong username. Try again.")
        user_input = input("Please enter username: ")
        for j in user_setlist:
            split_j = j.split(", ")
            if user_input == split_j[0]:
                login = True
                break

    # Enter password.
    # If wrong password is given, and error message will print
    if user_input == split_j[0]:
        pass_input = input("Please enter password: ")
        while pass_input != split_j[1]:
            print("Wrong password. Try again.")
            pass_input = input("Please enter password: ")

# If the username and password is right, the menu will display.
if user_input == split_j[0] and pass_input == split_j[1]:
    if user_input == "admin":
        display_menu_admin()

# We add new users and their passwords
if message == "r":
    reg_user()

# Add Tasks to tasks.txt
elif message == "a":
    func_task_add = add_task()

# View all tasks in tasks.txt
elif message == "va":
    view_all()

# View my tasks option
elif message == "vm":
    view_mine()

# View generated reports
elif message == "gr":
    generate_reports()

# View statistics for both user_overview.txt and task_overview.txt
elif message == "ds":
    all_stats()

# Exits the program
elif message == "e":
    print("You have exited the program.")

# Admin 2nd User Login Menu
if user_input != "admin":
    display_menu_user()

# NEW MENU
# 2nd Menu for every other user except Admin
if user_input != "admin":
    # Add Tasks to tasks.txt
    if message == "a":
        func_task_add = add_task()

    # View all tasks in tasks.txt
    elif message == "va":
        view_all()

    # View my tasks option
    elif message == "vm":
        view_mine()
    # View generated reports
    elif message == "gr":
        generate_reports()

    # Exits the program
    elif message == "e":
        print("You have exited the program.")

# Reference
# https://www.kite.com/python/answers \
# /how-to-get-a-line-count-of-a-file-in-python
# https://betterprogramming.pub
# /10-ways-to-convert-lists-to-dictionaries-in-python-d2c728d2aeb8
# https://blog.finxter.com/list-to-dict-convert-a-list-into-a-dictionary-in-python/
# https://stackoverflow.com/questions/60294481/checking-if-date-is-overdue-from-text-file
# https://www.machinelearningplus.com/python/datetime-python-examples/
# https://stackabuse.com/how-to-format-dates-in-python/
# https://www.geeksforgeeks.org/python-replace-multiple-characters-at-once/
