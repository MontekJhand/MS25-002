#Python automatically allocates memory
#convert python objects into strings, can write and read json data to a file
import pandas as pd
import json
"""
Linked List: Create a linked list to manage tasks. Implement methods for adding, deleting, and traversing tasks.
Stack: Implement a stack for the undo feature, allowing users to revert the last action.
Hash Table: Use a hash table to manage and search tasks by tags or keywords.
"""
#store data in local json file
import json

def Add():
    task = []
    count = len(task) + 1  #  keep track of the next task number to assign when the user adds a new task

    
    while True:
        user = input("Enter tasks, when finished enter 'done': ")
        if user == 'done':
            break
        task.append(f"{count}. {user}")
        count += 1      #while True count increases by one in order to be incremented per user input for element

    tasks = {
        "tasks": task
    }
    
    with open("Tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)    #stores data within json file

    
def Delete():
    with open("Tasks.json", 'w') as file:
        json.dump({"tasks": []}, file)
    print("Task list has been deleted.")

def View():
    
    #load file to read and print contents within a particular format
    with open("Tasks.json", 'r') as file:
        tasks = json.load(file)     #reads file via storage to then be printed
        print(json.dumps(tasks, indent=4))

def Edit():
    with open("Tasks.json", "r") as file:   
        data = json.load(file)
        tasks = data.get("tasks", [])



    alter = int(input("Enter the task number you want to edit: ")) - 1
    if 0 <= alter < len(tasks):
        new = input("Enter the new task: ")
        prefix = f"{alter + 1}. "

        tasks[alter] = prefix + new

        with open("Tasks.json", "w") as file:

            #access and stores task alteration by writing into task file
            json.dump({"tasks": tasks}, file, indent=4)
        print("Task updated")




def main():
    print("1. To add to tasks")
    print("2. To view tasks")
    print("3. To edit tasks")
    print("4. To delete tasks\n")
    choice = int(input("Choose: "))
    
    if choice == 1:
        Add()   #error

    elif choice == 2:
        View()
    
    elif choice == 3:
        Edit()

    elif choice == 4:
        Delete()

main()
