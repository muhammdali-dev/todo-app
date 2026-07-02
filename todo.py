import json
import os
File_Name="task.json"
def load_tasks():
    if os.path.exists(File_Name):
        with open(File_Name,"r") as f:
            return json.load(f)
    return []
def save_tasks(tasks):
    with open(File_Name,"w") as f:
        json.dump(tasks,f)
def add_tasks(tasks):
    task_name=input("Enter Task: ")
    tasks.append({"task":task_name,"done":False})
    save_tasks(tasks)
    print("Task Added")
def show_tasks(tasks):
        if not tasks:
            print("No tasks yet!")
            return
        for i, t in enumerate(tasks):
            status = "✓" if t["done"] else "✗"
            print(f"{i+1}. [{status}] {t['task']}")
def complete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to complete: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked complete!")
    else:
        print("Invalid task number")
def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice")
main()

