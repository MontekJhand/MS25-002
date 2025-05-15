#Python automatically allocates memory
#convert python objects into strings, can write and read json data to a file
import pandas as pd
import csv

"""
Linked List: Create a linked list to manage tasks. Implement methods for adding, deleting, and traversing tasks.
Stack: Implement a stack for the undo feature, allowing users to revert the last action.
Hash Table: Use a hash table to manage and search tasks by tags or keywords.
"""
#intilizing node for adding method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#linked list
class ListedList:
    def __init__(self):
        self.head = None

    def inserAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node

task_list = ListedList()    #meant to tie a method to linkedlist


def Add():
    while True:
        task = input("Enter a new task, type 'finish' to stop: ")
        if task == "finish":
            break
            
    task_list.insertAtEnd(task)

    # Saved to CSV
    tasks = task_list.traverse()
    df = pd.DataFrame(tasks, columns=["Task"])

def file_exists():
    try:
        with open("TasksV2.csv", "r"):
            return True
    except:
            return False

def Delete():
    open("TasksV2.csv", "w").close()
    print("All tasks deleted.")

def Edit():
    print("Havent implemented it yet")

def View():
    df = pd.read_csv("TasksV2.csv")
    if df.empty:
        print("No tasks to show.")
    else:
        print(df.to_string(index=False))


def main():
    print("1. To add tasks")
    print("2. To view tasks")
    print("3. To edit tasks")
    print("4. To delete all tasks\n")

    choice = int(input("Enter a choice to do each of the 5 options: "))
    if choice == 1:
        Add()
    elif choice == 2:
        View()
    elif choice == 3:
        Edit()
    elif choice == 4:
        Delete()
    else:
        print("Invalid choice.")

main()
