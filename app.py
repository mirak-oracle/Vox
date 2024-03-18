import tkinter as tk
from tkinter import messagebox

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Create the main window
root = tk.Tk()
root.title("Task Manager")

# Create GUI elements
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=10)

delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task)
delete_button.grid(row=0, column=2, padx=5, pady=10)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
