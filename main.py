import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to mark a task as done
def mark_done():
    try:
        selected_task = task_listbox.curselection()
        if selected_task:
            task_listbox.itemconfig(selected_task, {'bg': 'lightgreen'})
            task_listbox.selection_clear(selected_task)
            task_listbox.selection_set(selected_task)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Function to delete a task from the list
def delete_task():
    try:
        selected_task = task_listbox.curselection()
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Setting up the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.config(bg="#f4f4f9")

# Create the task listbox with a custom background color
task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 14), selectmode=tk.SINGLE, bg="lightyellow")
task_listbox.pack(pady=20)

# Entry widget to add new tasks
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Add, Done, and Delete buttons
add_button = tk.Button(root, text="Add Task", font=("Arial", 14), bg="lightblue", command=add_task)
add_button.pack(pady=5)

done_button = tk.Button(root, text="Mark as Done", font=("Arial", 14), bg="lightgreen", command=mark_done)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Arial", 14), bg="salmon", command=delete_task)
delete_button.pack(pady=5)

# Main loop to run the application
root.mainloop()
