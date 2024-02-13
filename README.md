import os
import json
from datetime import datetime

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        return tasks
    return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks,file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']} - {task['date']}")

def add_task(title):
    tasks = load_tasks()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task = {'title': title, 'date': date}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {title}")

def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task removed: {removed_task['title']}")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            tasks = load_tasks()
            display_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '3':
            index = int(input("Enter task index to remove: "))
            remove_task(index)
        elif choice == '4':
            print("Exiting To-Do List Application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main ()
