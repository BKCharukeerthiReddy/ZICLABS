import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("300x400")
        self.root.configure(background="#f0f0f0")

        self.tasks = []

        self.entry = tk.Entry(root, bg="white", fg="black", font=('Arial', 14))
        self.entry.pack(pady=10, padx=10, ipadx=10, ipady=8, fill=tk.X)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=('Arial', 12))
        self.add_button.pack(pady=5, ipadx=10, ipady=6, fill=tk.X)

        self.list_button = tk.Button(root, text="List Tasks", command=self.list_tasks, bg="#008CBA", fg="white", font=('Arial', 12))
        self.list_button.pack(pady=5, ipadx=10, ipady=6, fill=tk.X)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg="#FF8C00", fg="white", font=('Arial', 12))
        self.remove_button.pack(pady=5, ipadx=10, ipady=6, fill=tk.X)

        self.tasks_label = tk.Label(root, text="Tasks will be listed here.", font=('Arial', 14), wraplength=280)
        self.tasks_label.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.entry.delete(0, tk.END)

    def list_tasks(self):
        if self.tasks:
            tasks_text = ""
            for task_info in self.tasks:
                task = task_info["task"]
                completed = task_info["completed"]
                if completed:
                    tasks_text += f"✔ {task}\n"
                else:
                    tasks_text += f"❌ {task}\n"
            self.tasks_label.config(text=tasks_text)
        else:
            self.tasks_label.config(text="No tasks in the list.")

    def remove_task(self):
        if self.tasks:
            task_index = len(self.tasks) - 1
            self.tasks.pop(task_index)
            self.list_tasks()

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
