import os

# Task Manager class to handle task operations
class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return [line.strip() for line in file.readlines()]
        return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self, task):
        self.tasks.append(f"{task} [Incomplete]")
        self.save_tasks()

    def edit_task(self, task_number, new_task):
        if 0 <= task_number < len(self.tasks):
            status = self.tasks[task_number].split(" [")[1]  # Keep current status
            self.tasks[task_number] = f"{new_task} [{status}"
            self.save_tasks()

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks.pop(task_number)
            self.save_tasks()

    def mark_complete(self, task_number):
        if 0 <= task_number < len(self.tasks):
            task_name = self.tasks[task_number].split(" [")[0]  # Extract task name
            self.tasks[task_number] = f"{task_name} [Complete]"
            self.save_tasks()

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

# Console application logic
def console_app():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task_manager.display_tasks()
        elif choice == "2":
            task = input("Enter the new task: ")
            task_manager.add_task(task)
            print("Task added.")
        elif choice == "3":
            task_manager.display_tasks()
            task_num = int(input("Enter the task number to edit: ")) - 1
            new_task = input("Enter the new task description: ")
            task_manager.edit_task(task_num, new_task)
            print("Task edited.")
        elif choice == "4":
            task_manager.display_tasks()
            task_num = int(input("Enter the task number to delete: ")) - 1
            task_manager.delete_task(task_num)
            print("Task deleted.")
        elif choice == "5":
            task_manager.display_tasks()
            task_num = int(input("Enter the task number to mark as complete: ")) - 1
            task_manager.mark_complete(task_num)
            print("Task marked as complete.")
        elif choice == "6":
            break
        else:
            print("Invalid option, please try again.")

# Run the console application
if __name__ == "__main__":
    console_app()
