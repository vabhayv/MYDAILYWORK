import json

FILE_NAME = "tasks.json"


def load_tasks():

    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = [] 
    return tasks


def save_tasks(tasks):
    
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    
    if not tasks:
        print("\nNo tasks available!\n")
        return

    print("\nYour To-Do List:")
    print("------------------")
    for index, task in enumerate(tasks):
        status = "✔ Completed" if task["completed"] else "✘ Not Completed"
        print(f"{index + 1}. {task['title']} [{status}]")
    print()


def add_task(tasks):
    """
    This function adds a new task to the list.
    """
    title = input("Enter task title: ")
    task = {
        "title": title,
        "completed": False 
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


def update_task(tasks):
    """
    This function updates the title of an existing task.
    """
    display_tasks(tasks)

    try:
        task_number = int(input("Enter task number to update: "))
        if 1 <= task_number <= len(tasks):
            new_title = input("Enter new task title: ")
            tasks[task_number - 1]["title"] = new_title
            save_tasks(tasks)
            print("Task updated successfully!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def mark_completed(tasks):
    """
    This function marks a task as completed.
    """
    display_tasks(tasks)

    try:
        task_number = int(input("Enter task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def delete_task(tasks):
    
    display_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['title']}' deleted successfully!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def main():
    

    tasks = load_tasks()

    while True:
        print("====== TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Saving tasks and exiting...")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
