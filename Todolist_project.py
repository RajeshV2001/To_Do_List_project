from tkinter import *
from tkinter import messagebox

c=0
def add():
    global c
    if task.get() == "Enter Here":
        messagebox.showinfo("Enter Again","Enter Valid Task...")
        
    elif len(task.get())==0:
        messagebox.showinfo("Enter Again","Task Field Should not be Empty !")
        
    else:
        c+=1
        a=var.get()   
        lb.insert(END,"*  "+a)
        scrolly.config(command=lb.yview)
        task.delete(0,END)
        lbl2.config(text=f"Total Tasks added : {c}",fg='blue')
        
        


def delete():
    global c
    
    data=lb.get(0,END)
    selected=lb.curselection()
    
    c-=len(selected)
    
    if len(data)==0:
        messagebox.showinfo("All Cleared","No Tasks Remaining !")
        
    elif len(selected)==0:
        messagebox.showinfo("No Selection","Please Select Task To Delete !")
    
    else:
        for i in selected[::-1]:
            lb.delete(i)
            
    lbl2.config(text=f"Total Tasks added : {c}",fg='blue')

def erase(event):
    task.delete(0,END)


def save():
    a=lb.get(0,END)
    if len(a)==0:
        messagebox.showinfo("Cannot save","Please add task to save !")
        
    else:
        with open("list.txt",'w') as f:
            f.write("Added Tasks are : ")
            f.write('\n')
            for i in a:
                f.write(i)
                f.write('\n')
            f.close()
            messagebox.showinfo("Success","Task List saved Successfully !")
            


if __name__=="__main__":
    
    root=Tk()
    root.iconbitmap('todo.ico')
    root.configure(background='lightgreen')
    root.title("To Do List")
    root.geometry("500x600")
    root.maxsize(500,650)
    root.minsize(500,650)
    
   
    
    f1=Frame(root,width=500,height=100,relief=SOLID,border=3,background='lightcyan')
    f1.grid(row=0,column=0,pady=50,padx=7)
    
    f2=Frame(root,width=300,height=300,background='lightblue',border=5)
    f2.grid(row=1,column=0)

    
    
    lbl1=Label(f2,text="Click on the Tasks to Select and Delete",fg="red",font=10,relief=SOLID,borderwidth=2)
    lbl1.pack(side='top',pady=10)
    
    lbl2=Label(f2,text="Total Tasks added : 0",font=10,relief=SOLID,borderwidth=2,fg='blue')
    lbl2.pack(side='top')
    
    lbl=Label(f1,text="ENTER THE TASK : ",foreground='black',background='lightcyan')
    lbl.pack(side='left')
    
    var=StringVar()
    task=Entry(f1,width=50,textvariable=var,bd=3,background='white',highlightcolor='blue',highlightthickness=3,highlightbackground='red',insertwidth=2)
    task.insert(0,"Enter Here")
    task.pack(side='left')
    task.bind("<FocusIn>",erase)
    
    scrolly=Scrollbar(f2)
    scrolly.pack(side='right',fill=Y)
    
    
    lb=Listbox(f2,yscrollcommand=scrolly.set,width=40,height=18,background='lightcyan',selectmode=MULTIPLE,font={'style':'bold'},fg='blue')
    lb.pack(side='left',fill=BOTH)
    
    add_btn=Button(f1,text='ADD',background='yellow',foreground='blue',borderwidth=3,command=add,width=7)
    add_btn.pack(padx=2)
    
    del_btn=Button(root,text='Delete Task',background='yellow',foreground='blue',borderwidth=5,command=delete)
    del_btn.grid(row=2,column=0,pady=10)
    
    save_btn=Button(root,text="Save List",background='yellow',fg='blue',borderwidth=5,command=save)
    save_btn.grid(row=3,column=0)
    
    root.mainloop()