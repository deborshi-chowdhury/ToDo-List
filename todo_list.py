tasks = []

while True:
    print("\nTO DO LIST")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No task yet!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No task to delete!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_num = int(input("Enter the task number which you want to delete: "))

            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num - 1)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")        