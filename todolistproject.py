print("Welcome!!")
print("If you need to make and organize a list, you've come to the right place!")

tasks = []  # Initialize an empty list to store tasks

while True:
    choice = input("Enter 'a' to add a task, 'd' to delete a task, 's' to show all tasks, or 'q' to quit: ").lower()

    if choice == 'a':
        new_task = input("Enter a new task: ")
        tasks.append(new_task)  # Add the new task to the list

    elif choice == 'd':
        if not tasks:  # Check if the list is empty
            print("The task list is empty.")
        else:
            print("Current tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            task_number = int(input("Enter the task number to delete: ")) - 1

            if 0 <= task_number < len(tasks):
                del tasks[task_number]
                print("Task deleted successfully.")
            else:
                print("Invalid task number. No task deleted.")

    elif choice == 's':
        if not tasks:  # Check if the list is empty
            print("The task list is empty.")
        else:
            print("Current tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == 'q':
        break  # Exit the loop and end the program

    else:
        print("Invalid choice. Please try again.")

print("Goodbye! Thanks for using the to-do list application.")
