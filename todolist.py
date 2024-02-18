import tkinter as tk
from tkinter import messagebox

tasks=[]

def add_task():
    task_text=entry.get()
    if task_text:
        tasks.append(task_text)
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
        
def mark_completed():
    selected_index=listbox.curselection()
    if selected_index:
        index=selected_index[0]
        task=tasks[index]
        tasks[index]=f"[Completed]{task}"
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task.")
        
def delete_task():
    selected_index=listbox.curselection()
    if selected_index:
        index=selected_index[0]
        del tasks[index]
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")
        
def update_listbox():
    listbox.delete(0,tk.END)
    for task in tasks:
        listbox.insert(tk.END,task)
        
root=tk.Tk()
root.title("To-Do List")

entry= tk.Entry(root, width=60, font=('Helvetica', 12))
entry.grid(row=0,column=0,padx=10,pady=10)

add_button= tk.Button(root, text="Add Task", background="bisque", width=10, command=add_task, font=('Helvetica', 12))
add_button.grid(row=0,column=1,padx=10,pady=10)

listbox= tk.Listbox(root, selectmode= tk.SINGLE, width=70, height=20, font=('Helvetica', 12))
listbox.grid(row=1,column=0,columnspan=2,padx=5,pady=10)

complete_button=tk.Button(root, text="Mark as Completed", background="light blue", command=mark_completed, font=('Helvetica', 12))
complete_button.grid(row=2,column=0,padx=10,pady=10)


delete_button= tk.Button(root, text="Delete Task", background="pink", width=10, command=delete_task, font=('Helvetica', 12))
delete_button.grid(row=2,column=1,padx=10,pady=10)

root.mainloop()
