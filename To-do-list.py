# todo.py

tasks: list[str] = []

def show_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    global tasks
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def remove_task():
    global tasks
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Task '{removed}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
