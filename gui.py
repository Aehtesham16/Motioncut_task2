import tkinter as tk
from tkinter import messagebox
import os

class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.tasks = self.load_tasks()

        # Task Listbox
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)
        self.update_task_listbox()

        # Task Entry Field
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(self.root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(side=tk.LEFT, padx=5)

    def load_tasks(self):
        filename = "tasks.txt"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                return [line.strip() for line in file.readlines()]
        return []

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(f"{task} [Incomplete]")
            self.save_tasks()
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                task_status = self.tasks[selected_task_index[0]].split(" [")[1]  # Keep status
                self.tasks[selected_task_index[0]] = f"{new_task} [{task_status}"
                self.save_tasks()
                self.update_task_listbox()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.save_tasks()
            self.update_task_listbox()

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_name = self.tasks[selected_task_index[0]].split(" [")[0]  # Keep task name
            self.tasks[selected_task_index[0]] = f"{task_name} [Complete]"
            self.save_tasks()
            self.update_task_listbox()

# Run the Tkinter GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()
