tasks = []

def addTask():
    task = input("Please enter a task :")
    tasks.append(task)
    print(f" '{task}' added to the list ")
def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks :")
        for index,task in enumerate(tasks):
            print(f"Task #{index}. {task}")
def deleteTask():
    listTasks()
    try:
        task_to_delete = int(input("Enter the # to delete"))
        if task_to_delete >=0 and task_to_delete < len(tasks) :
            tasks.pop(task_to_delete)
            print(f"Task {task_to_delete} has been removed.")
        else:
            print(f"Task #{task_to_delete} was not found.")
    except:
        print("Invalid input")

if __name__ == "__main__": 
    while True:
        print("Select one of the folowing options")
        print("\n")
        print("1.Add a new task")
        print("2.Delete a task")
        print("3.List tasks")
        print("4.Quit")

        choice  = input("Enter your choice :")

        if choice == "1":
           addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            break
        else:
            print("Invalid input.Try again")

print("Goodbye.")