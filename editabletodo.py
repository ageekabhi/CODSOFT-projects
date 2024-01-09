import json

def load_data():
    try:
        with open("todos.json", "r") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {"tasks": []}
    return data

def save_data(data):
    with open("todos.json", "w") as file:
        json.dump(data, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {'[X]' if task['completed'] else '[ ]'} {task['description']}")

def add_task(data, description):
    task = {"description": description, "completed": False}
    data["tasks"].append(task)
    save_data(data)
    print("Task added successfully.")

def update_task(data, task_index, new_description):
    if 1 <= task_index <= len(data["tasks"]):
        data["tasks"][task_index - 1]["description"] = new_description
        save_data(data)
        print("Task updated successfully.")
    else:
        print("Invalid task index.")

def mark_completed(data, task_index):
    if 1 <= task_index <= len(data["tasks"]):
        data["tasks"][task_index - 1]["completed"] = not data["tasks"][task_index - 1]["completed"]
        save_data(data)
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def delete_task(data, task_index):
    if 1 <= task_index <= len(data["tasks"]):
        del data["tasks"][task_index - 1]
        save_data(data)
        print("Task deleted successfully.")
    else:
        print("Invalid task index.")

def main():
    data = load_data()

    while True:
        print("\n=== To-Do List ===")
        display_tasks(data["tasks"])

        print("\n1. Add Task")
        print("2. Update Task")
        print("3. Mark as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            description = input("Enter the task description: ")
            add_task(data, description)
        elif choice == "2":
            task_index = int(input("Enter the task index to update: "))
            new_description = input("Enter the new task description: ")
            update_task(data, task_index, new_description)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            mark_completed(data, task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to delete: "))
            delete_task(data, task_index)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
