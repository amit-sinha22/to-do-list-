import json
import os

tasks = []
TASKS_FILE = "tasks.json"


def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []
    else:
        tasks = []


def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def show_menu():
    print("\nTo-Do App")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as complete")
    print("5. Quit")


def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task.get("done") else "[ ]"
        print(f"{index}. {status} {task['text']}")


def add_task():
    task_text = input("Enter a new task: ").strip()
    if task_text:
        tasks.append({"text": task_text, "done": False})
        save_tasks()
        print("Task added.")
    else:
        print("Task cannot be empty.")


def remove_task():
    view_tasks()
    if not tasks:
        return

    choice = input("Enter the task number to remove: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    task_index = int(choice) - 1

    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks()
        print(f"Removed: {removed_task['text']}")
    else:
        print("Task number not found.")


def mark_task():
    view_tasks()
    if not tasks:
        return

    choice = input("Enter the task number to mark as complete: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    task_index = int(choice) - 1

    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        save_tasks()
        print(f"Marked as complete: {tasks[task_index]['text']}")
    else:
        print("Task number not found.")


def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
