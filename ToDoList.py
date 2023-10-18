import os
import json

filename = "todo_list.txt"

class Task:
    def __init__(self, description, completed=False, priority=3):
        self.description = description
        self.completed = completed
        self.priority = priority

    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.description} (Priority: {self.priority})"

def load_todo_list():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read().strip()
            if content:  # check if the file is not empty
                try:
                    tasks_json = json.loads(content)
                    return [Task(task['description'], task['completed'], task['priority']) for task in tasks_json]
                except json.JSONDecodeError:
                    print("Error: The file is not in a valid JSON format.")
                    return []  # return an empty list or handle this appropriately
            else:
                print("Notice: The file is empty, starting with an empty to-do list.")
                return []  # file is empty
    else:
        print("Notice: No existing file found, starting with an empty to-do list.")
        return []  # file does not exist


def save_todo_list(todo_list):
    with open(filename, "w") as file:
        json.dump([task.__dict__ for task in todo_list], file)

def print_todo_list(todo_list):
    if todo_list:
        print("Things to do:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty!")

def remove_task(todo_list):
    print("List of tasks:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    
    task_num = input("Enter the number of the task you want to remove: ")
    
    # Error handling for non-integer inputs
    if task_num.isdigit() and 0 < int(task_num) <= len(todo_list):
        del todo_list[int(task_num) - 1]
        print("Task removed.")
    else:
        print("Invalid task number!")

def edit_task(todo_list):
    print("List of tasks:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    
    task_num = input("Enter the number of the task you want to edit: ")

    # Error handling for invalid input
    if task_num.isdigit() and 0 < int(task_num) <= len(todo_list):
        new_description = input("Enter new task description: ")
        todo_list[int(task_num) - 1].description = new_description
    else:
        print("Invalid task number!")

def mark_task_complete(todo_list):
    print("List of tasks:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    
    task_num = input("Enter the number of the task you want to mark as complete: ")

    # Error handling for invalid input
    if task_num.isdigit() and 0 < int(task_num) <= len(todo_list):
        todo_list[int(task_num) - 1].completed = True
        print("Task marked as complete.")
    else:
        print("Invalid task number!")

todo_list = load_todo_list()
print_todo_list(todo_list)

# Main loop with choices handling
while True:
    print("\nChoose an option:")
    print("1: Add task\n2: Remove task\n3: Edit task\n4: Mark task as complete\n0: Exit")
    choice = input("Your choice: ")

    if choice == '1':
        description = input("Enter task description: ")
        priority = input("Set priority (1- High, 2 - Medium, 3 - Low): ")
        if priority.isdigit() and 1 <= int(priority) <= 3:
            todo_list.append(Task(description=description, priority=int(priority)))
            save_todo_list(todo_list)
        else:
            print("Invalid priority!")
    elif choice == '2':
        remove_task(todo_list)
        save_todo_list(todo_list)
    elif choice == '3':
        edit_task(todo_list)
        save_todo_list(todo_list)
    elif choice == '4':
        mark_task_complete(todo_list)
        save_todo_list(todo_list)
    elif choice == '0':
        break
    else:
        print("Invalid option, please choose again.")

    print("\nCurrent List:")
    print_todo_list(todo_list)
