# Capstone-Project-III---LV1
This is my third project that demonstates my skills as a software engineer.

## Description of the project
1. What is the project
2. How does it work

### What is the project
This project is a software program that is designed to help a small business assign and manage tasks for each member of the business.
This project consists of 3 main files.
1. The main program python file
2. The user text file that has a list of the registered users and their individual passwords
3. The tasks text file that has all the neccessary details of each assigned task.

### How does it work

The program has a login menu. The program will request the user for their username and password. <br/>
If the username or password is wrong, the username and password will be requested until both are correct.

Once the login is correct, the program will have a menu with the following options:
1. **r - register user**
2. **a - add task**
3. **va - view all tasks**
4. **vm - view my tasks**
5. **gr - generate reports**
6. **ds - display statistics**
7. **e - exit**

The **_register user_** option allows any member to register a new user, along with password, to use the software program.<br/>
The details of the user login crdentials are _stored_ in _user.txt_. This option does not allow a user to register a username that is already in the 
_user.txt file_.

The **_add task_** option allows one to assign a new task to a member of the team along with _when_ the task is assigned and the _deadline_ for task to be completed.
The _details_ of the tasks are stored in _tasks.txt_.

The **_view all tasks_** option allows anyone to see **all** the tasks assigned to which member of the team along with tasks details.
This option has add functionalites which:
 * Allows the user to select either a specific task by entering a number
or input ‘-1’ to return to the main menu.
 *  If the user selects a specific task, they should be able to choose to
either mark the task as complete or edit the task. The task can be edited only if the task is incomplete.

The **_view my tasks_** option allows the user logged in to see **all** their assigned tasks along with tasks details.

The **_generate reports_** option is chosen, 2 text files named _task_overview.txt_ and _user_overview.txt_ will be generated.
#### task_overview.txt should contain the following:
  * The total number of tasks that have been generated and
tracked using the task_manager.py.
  * The total number of completed tasks.
  * The total number of uncompleted tasks.
  * The total number of tasks that haven’t been completed and
that are overdue.
  * The percentage of tasks that are incomplete.
  * The percentage of tasks that are overdue.

#### user_overview.txt should contain the following:
  * The total number of users registered with task_manager.py.
  * The total number of tasks that have been generated and
tracked using the task_manager.py.
##### For each user describe the following:
  * The total number of tasks assigned to that user.
  * The percentage of the total number of tasks have
been assigned to that user that is logged in.
  * The percentage of the tasks assigned to the logged in user 
that have been completed.
  * The percentage of the tasks assigned to the logged in user 
that must still be completed.
  * The percentage of the tasks assigned to the logged in user
that have not yet been completed and are overdue.

The **_display statistics_** option allows the user to read the statistics of both the _task_overview.txt_ and _user_overview.txt_ in a friendly manner.

The **_exit_** option let's the user log off the software program.


