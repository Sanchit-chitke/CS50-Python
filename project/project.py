import os
from tabulate import tabulate

# Function to display the to-do list
def display_todo_list(todo_list):
    headers = ["Task", "Priority", "Status"]
    table = tabulate(todo_list, headers, tablefmt="grid")
    print(table)

# Function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter the task: ")
    priority = input("Enter the priority (High/Medium/Low): ")
    status = "Incomplete"
    todo_list.append([task, priority, status])
    print("Task added successfully!")

# Function to mark a task as complete
def mark_complete(todo_list):
    display_todo_list(todo_list)
    task_index = int(input("Enter the index of the task to mark as complete: "))
    if 0 <= task_index < len(todo_list):
        todo_list[task_index][2] = "Complete"
        print("Task marked as complete!")
    else:
        print("Invalid index.")

# Function to save the to-do list to a file
def save_to_file(todo_list, filename="todo_list.txt"):
    with open(filename, "w") as file:
        for task in todo_list:
            file.write(",".join(task) + "\n")
    print("To-do list saved to", filename)

# Function to load the to-do list from a file
def load_from_file(filename="todo_list.txt"):
    todo_list = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                todo_list.append(task_data)
    return todo_list

# Main program
def main():
    filename = "todo_list.txt"
    todo_list = load_from_file(filename)

    while True:
        print("\n=== To-Do List ===")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Save To-Do List to File")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_complete(todo_list)
        elif choice == "4":
            save_to_file(todo_list, filename)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
