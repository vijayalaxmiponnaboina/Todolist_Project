todolist=[]

# Function to Add a New Task
def add_task():
    task=input("Enter a Task: ")
    todolist.append({"Task":task,"Status":"Pending"})
    print("Your task added successfully.....\n")


# Function to View All Task
def view_task():
    print("Your TodoList ")
    if len(todolist)==0:
        print("No tasks Available")
    else:
        for index,task in enumerate(todolist,start=1):
            print(f"{index}.{task['Task']} - {task['Status']}")


# Function to Remove a Task
def remove_task():
    if len(todolist)==0:
        print("List is Empty...")
    else:
        try:
            search_index=int(input("Enter your Task number: "))-1
            if 0<=search_index<len(todolist):
                removed_task=todolist.pop(search_index)
                print(f"Removed Task : {removed_task['Task']}")
            else:
                print("Task Number is wrong!")
        except ValueError:
            print("Please Enter Valid Number")


# Function to Mark Task as Completed
def mark_completed():
    if len(todolist)==0:
        print("List is Empty...")
    else:
        try:
            search_index=int(input("Enter your Task number: "))-1
            if 0<=search_index<len(todolist):
                todolist[search_index]['Status']="Completed"
                print(f"Task {todolist[search_index]['Task']} has been marked as completed....")
            else:
                print("Task Number is wrong!")
        except ValueError:
            print("Please Enter Valid Number")


# Function to display menu
def menu():
    print("======*Main Menu*======")
    print("1.Add Task")
    print("2.View Task")
    print("3.Remove Task")
    print("4.Mark as Completed")
    print("5.Exit")
    choice=input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        print("Good byee..")
        exit()
    else:
        print("Invalid choice.Try again!!!")
while True:
    menu()
