import tkinter as tk
from tkinter import messagebox
def addtask():
    task=entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delet(0,tk.END)
    else:
        messagebox.showwarning("Warning!")
def deletetask():
    selectedtask=listbox.curselection()
    if selectedtask:
        deletedtask=listbox.get(selectedtask)
        listbox.delet(selectedtask)
        deletedtask.insert(0,deletedtask)
    else:
        messagebox.showwarning("Warning! Please select a task")
def showhistory():
    history="\n".join(deletedtasks.get(0,tk.END))
    if history:
        messagebox.showinfo("Deleted task history",history)
    else:
        messagebox.showinfo("Deleted tasks history","No deleted tasks")
root=tk.Tk()
root.title("To-Do-List")
root.geometry("300x300")
listbox=tk.Listbox(root,selectmode=tk.SINGLE)
listbox.pack(fill=tk.BOTH,expand=True)
entry=tk.Entry(root)
entry.pack(fill=tk.X)
addbutton=tk.Button(root,text="Add",command=addtask)
deletebutton=tk.Button(root,text="Delete",command=deletetask)
showhistorybutton=tk.Button(root,text="Show history",command=showhistory)
addbutton.pack(fill=tk.X)
deletebutton.pack(fill=tk.X)
showhistorybutton.pack(fill=tk.X)
deletedtasks=tk.Listbox(root,selectmode=tk.SINGLE)
root.mainloop()