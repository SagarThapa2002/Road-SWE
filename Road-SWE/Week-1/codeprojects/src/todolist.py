## ToDo list application using Python

def manage():
    todo_list = []

    def display_menu():
        print("\nToDo List Application")
        print("1. View ToDo List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            if not todo_list:
                print("Your ToDo list is empty.")
            else:
                print("Your ToDo List:")
                for idx, task in enumerate(todo_list, start=1):
                    print(f"{idx}. {task}")

        elif choice == "2":
            task = input("Enter the task to add: ")
            todo_list.append(task)
            print(f'Task "{task}" added to the list.')

        elif choice == "3":
            if not todo_list:
                print("Your ToDo list is empty. No tasks to remove.")
            else:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    print(f'Task "{removed_task}" removed from the list.')
                else:
                    print("Invalid task number.")

        elif choice == "4":
            print("Exiting ToDo List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")