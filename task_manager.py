import os
import json

#File to store tasks
FILE_NAME = "tasks.txt"

#Load tasks from file
def load_tasks():
 tasks= {}
 if os.path.exists(FILE_NAME):
     with open(FILE_NAME,"r") as file:
         for line in file:
             task_id, title, status, priority = line.strip(). split("|")
             tasks[int(task_id)] = {"title": title.strip(), "status": status.strip(), "priority": priority.strip()}
 return tasks
             
#Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']} |{task.get('priority', 'Not Set')}\n")
           
#Export tasks to JSON file           
def json_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent = 4 )
        print("Tasks exported to tasks.json successfully!")

#Add a new task
def add_tasks(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added.")
    
#View all task
def view_tasks(tasks):
    if  not tasks:
        print("No task available")
        
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']} - Priority: {task.get('priority', 'Not Set')}")
            
#Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete:"))  
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as completed")
    else:
        print("Task ID not found")
        
#To add priority       
def priority_task(tasks):
    task_id = int(input("EnterTask ID: "))
    if task_id in tasks:
        priority = input("Enter Priority Task(High/Medium/Low): ")
        tasks[task_id]["priority"] = priority
        print("Priority updated successfully")
    else:
            print("Task ID not found")
                  
#Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to Delete: "))

    if task_id in tasks:
        deleted_task = tasks.pop(task_id)

        new_tasks = {}
        for new_id, (_, task) in enumerate(tasks.items(), start=1):
         new_tasks[new_id] = task

        tasks.clear()
        tasks.update(new_tasks)

        print(f"Task '{deleted_task['title']}' deleted")

    else:
        print("Task ID not found")
        
#Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu")
        print("1. Add task")
        print("2. View task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Set Priority")
        print("6. Export to JSON")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_tasks(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            mark_task_complete(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            priority_task(tasks)
        elif choice ==6:
            json_tasks(tasks)    
        elif choice == 7:
            save_tasks(tasks)
            print("Goodbye")
            break
        else:
            print("Invalid Choice. Please try again")
            
if __name__== "__main__":
    main()
    
