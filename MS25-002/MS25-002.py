#Python automatically allocates memory
#convert python objects into strings, can write and read json data to a file
import pandas as pd
import json
"""
Linked List: Create a linked list to manage tasks. Implement methods for adding, deleting, and traversing tasks.
Stack: Implement a stack for the undo feature, allowing users to revert the last action.
Hash Table: Use a hash table to manage and search tasks by tags or keywords.    -> do so as an seperrate task
"""
#store data in local json file
import json
task = []

def Add():
    count = len(task) + 1  #  keep track of the next task number to assign when the user adds a new task

    
    while True:
        user = input("Enter tasks, when finished enter 'done': ")
        if user == 'done':
            break
        task.append(f"{count}. {user}")     #count is key
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
            json.dump({"tasks": tasks}, file, indent=4)
        print("Task updated")

def Undo():
    #utilize pop to undo latest 
    with open("Tasks.json", "r") as file:
        data = json.load(file)      #access data within json file
        tasks = data.get("tasks", [])   #returns value in dictionary within json file


    if tasks:
        removed = tasks.pop()   #access task to remove last element within dict-list
        with open("Tasks.json", "w") as file:

            #write into file to remove a key from a hash table
            json.dump({"tasks": tasks}, file, indent=4)     #serilizes into a properly formated JSON string and writes into file to be written into
    print(f"Latest entry has been undone.")

def Search():
    search = int(input("Enter a number for the task list you want: ")) - 1
    with open("Tasks.json", "r") as file:
        data = json.load(file)
    my_dict = data["tasks"]     #access arrays that are stored within dict

    if 0 <= search < len(my_dict):
        task = my_dict[search]
        print("Task found:")
        print(task)

def main():
    print("1. To add to tasks")
    print("2. To view tasks")
    print("3. To edit tasks")
    print("4. To delete tasks")
    print("5. To undo last action")
    print("6. Search for a task\n")
    choice = int(input("Choose: "))
    
    if choice == 1:
        Add()   #error

    elif choice == 2:
        View()
    
    elif choice == 3:
        Edit()

    elif choice == 4:
        Delete()
    
    elif choice == 5:
        Undo()
    
    elif choice == 6:
        Search()

main()