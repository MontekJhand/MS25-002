import json

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def insert(self, task):
        new_node = Node(task)

        #head works is that because it connects to first node
        if not self.head:       
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def traverse(self):
        current = self.head
        count = 1
        while current:
            print(f"{count}. {current.task}")   #during first node re counter as its traersing it increments
            current = current.next
            count += 1

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.task)
            current = current.next
        return result

    def from_list(self, tasks):
        self.head = None
        for task in tasks:
            self.insert(task)

    def edit(self, index, new_task):
        current = self.head
        count = 1
        while current:
            if count == index:
                old_task = current.task
                current.task = new_task
                return old_task
            current = current.next
            count += 1
        return None

    def delete(self, index):
        if not self.head:
            return None
        if index == 1:
            deleted = self.head.task
            self.head = self.head.next
            return deleted
        current = self.head
        count = 1
        while current.next:
            if count + 1 == index:
                deleted = current.next.task
                current.next = current.next.next
                return deleted
            current = current.next
            count += 1
        return None

class Stack:
    def __init__(self):
        self.items = []

    def push(self, action):
        self.items.append(action)

    def pop(self):
        return self.items.pop() if self.items else None

class TaskHashTable:
    def __init__(self):
        self.table = {}

    def build(self, tasks):
        self.table.clear()
        for i, task in enumerate(tasks):
            self.table[task.lower()] = i + 1

    def search(self, keyword):
        return self.table.get(keyword.lower(), -1)

task_list = TaskList()  #call fcn
undo_stack = Stack()
hash_table = TaskHashTable()


def save_to_file():
    with open("Tasks.json", "w") as file:
        json.dump({"tasks": task_list.to_list()}, file, indent=4)


def load_from_file():
    try:
        with open("Tasks.json", "r") as file:
            content = file.read().strip()
            if not content:
                return  # Empty file, nothing to load
            data = json.loads(content)
            task_list.from_list(data.get("tasks", []))
    except (FileNotFoundError, json.JSONDecodeError):
        pass  # Either the file doesn't exist or it's invalid JSON


def main():
    load_from_file()

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Undo Last Action")
        print("6. Search Task")
        print("7. Exit")

        choice = input("Choose (1–7): ")

        if choice == "1":
            task = input("Enter task: ")
            task_list.insert(task)
            undo_stack.push(("add",))
            save_to_file()

        elif choice == "2":
            task_list.traverse()

        elif choice == "3":
            task_list.traverse()
            index = int(input("Enter task number to edit: "))
            new_task = input("Enter new task: ")
            old_task = task_list.edit(index, new_task)
            if old_task:
                undo_stack.push(("edit", index, old_task))
                save_to_file()
            else:
                print("Invalid task number.")

        elif choice == "4":
            task_list.traverse()
            index = int(input("Enter task number to delete: "))
            deleted = task_list.delete(index)
            if deleted:
                undo_stack.push(("delete", index, deleted))
                save_to_file()
                print("Task deleted.")
            else:
                print("Invalid task number.")

        elif choice == "5":
            action = undo_stack.pop()
            if not action:
                print("Nothing to undo.")
                continue

            if action[0] == "add":
                task_list.delete(len(task_list.to_list()))

            elif action[0] == "edit":
                _, index, old_task = action
                task_list.edit(index, old_task)

            elif action[0] == "delete":
                _, index, deleted_task = action
                current = task_list.head
                new_list = []
                count = 1
                while current:
                    if count == index:
                        new_list.append(deleted_task)
                    new_list.append(current.task)
                    current = current.next
                    count += 1
                task_list.from_list(new_list[:len(task_list.to_list())+1])

            save_to_file()
            print("Last action undone.")

        elif choice == "6":
            hash_table.build(task_list.to_list())
            keyword = input("Enter keyword to search: ")
            pos = hash_table.search(keyword)
            if pos == -1:
                print("Task not found.")
            else:
                print(f"Found at position {pos}: {task_list.to_list()[pos-1]}")

        elif choice == "7":
            break


if __name__ == "__main__":
    main()
