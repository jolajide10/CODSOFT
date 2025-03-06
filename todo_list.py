import json

# File to store tasks
todo_file = "todo_list.json"

# Load existing tasks
def load_tasks():
    try:
        with open(todo_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(todo_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "[✓]" if task["completed"] else "[ ]"
            print(f"{idx}. {status} {task['description']}")

def update_task(tasks, task_index, new_description):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["description"] = new_description
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task index.")

def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

def mark_completed(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            index = int(input("Enter task number to update: ")) - 1
            new_desc = input("Enter new task description: ")
            update_task(tasks, index, new_desc)
        elif choice == "4":
            view_tasks(tasks)
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == "5":
            view_tasks(tasks)
            index = int(input("Enter task number to mark as completed: ")) - 1
            mark_completed(tasks, index)
        elif choice == "6":
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
