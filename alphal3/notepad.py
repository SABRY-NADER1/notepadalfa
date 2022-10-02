import tkinter as tk
from tkinter.filedialog import *
def savefile():
    Filelocation = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text files","*.txt"),("All files","*.*")]
    )
    if not Filelocation:
        return
    with open(Filelocation,"w") as file_output:
        text=Entry.get(1.0,tk.END)
        file_output.write(text)
    s.title(f"alfa notepad-{Filelocation}")
    
    
def openfile():
    Filelocation=askopenfilename(
        filetypes=[("Text files","*.txt"),("All files","*.*")]
    )  
    if not Filelocation:
        return
    Entry.delete(1.0,tk.END)
    with open(Filelocation,"r") as fileinput:
        text=fileinput.read()
        Entry.insert(tk.END,text)
        s.title(f"alfa notepad -{Filelocation}")
def clearfile():
    Entry.delete(1.0,tk.END)
s=tk.Tk()
top=tk.Frame(s)
top.pack( anchor='nw')
s.config (bg="White")
b1=tk.Button(s , text='Open', bg ="White",command=openfile)
b1.pack(in_=top,side="left")
b2=tk.Button(s , text='Save', bg ="White",command=savefile) 
b2.pack(in_=top,side="left")
b3=tk.Button(s , text='Clear', bg ="White",command=clearfile)
b3.pack(in_=top,side="left")
b4=tk.Button(s , text='Exit', bg ="White",command=exit)
b4.pack(in_=top,side="left")
s.title("alfa notepad")
Entry=tk.Text(s ,wrap="word", bg = "#F9DDA4",font=("poppins", 15))
Entry.pack(padx=10,pady=5,expand="True",fill='both')
s.mainloop()
