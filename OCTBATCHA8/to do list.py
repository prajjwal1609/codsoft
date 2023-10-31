tasks = []
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    show_tasks()
    task_number = int(input("Enter the task number to remove: "))
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Removed: {removed_task}")
    else:
        print("Invalid task number.")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
