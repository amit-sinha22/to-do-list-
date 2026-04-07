tasks = []


def show_menu():
    print("\nTo-Do App")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")


def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
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
        print(f"Removed: {removed_task}")
    else:
        print("Task number not found.")


def main():
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
