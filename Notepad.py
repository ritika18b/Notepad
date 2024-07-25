from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os


def save(event=None):
    m= messagebox.askquestion("Message","Do you want to save file?")
    if m=="yes":
        filen=filedialog.asksaveasfile(initialdir="/",title="SaveFile",defaultextension=".txt",filetypes = (("Text files","*.txt"), ("All files","*.*")))
    #file=open(str(e.get()) + ".txt","w") #file=open("value of entry widget " + ".txt","w")
    if filen:
        filen=filen.name
        file=open(filen,"w")
        file.write(t.get(1.0,END))

def clear(event=None):
    m=messagebox.askquestion("Message","Do you want to clear file data?")
    if m=="yes":
        t.delete("1.0",END)
        
def open(event):
    m=messagebox.askquestion("Message","Do you want to open file ?")
    if m=="yes":
        filen=filedialog.asksaveasfile(initialdir="/",title="OpenFile",defaultextension=".txt",filetypes = (("Text files","*.txt"), ("All files","*.*")))
    if filen:
        filen=filen.name
        file=open(filen,"w") 
        file.write(t.get(1.0,END))    
        
def open_file():
    m = messagebox.askquestion("Message", "Do you want to open a file?")
    if m == "yes":
        filen = filedialog.askopenfilename(initialdir="/", title="Open File", defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filen:
            file = open(filen, "r")
            content = file.read()
            t.delete("1.0", END)
            t.insert("1.0", content)
            file.close()           

def delete_file():
    filen=filedialog.askopenfile(initialdir="/",title="Select File to delete",defaultextension=".txt",filetypes=(("Text files","*.txt"),("All files","*.*")))# str(e.get())+ ".txt")
    if filen:
        os.remove(filen)
    # file = str(e.get()) + ".txt"
    # t.delete("1.0", END)
    
def copy_text():
    t.event_generate("<<Copy>>")

def paste_text():
    t.event_generate("<<Paste>>")

def cut_text():
    t.event_generate("<<Cut>>")
         
     
root = Tk()
root.geometry("900x600")
root.config(background="#0e4f26")
root.title("NOTES")

F=Frame(root,bg="#064e3b",padx=10,pady=10)
F.pack(fill="x")

m=Menu(root)
f=Menu(m,tearoff=0,bg="#004043",fg="white",font=18)
m.add_cascade(label="File",menu=f)
f.add_command(label="save",command=save)
f.add_command(label="open",command=open_file)
f.add_command(label="delete",command=delete_file)

e=Menu(m,tearoff=0,bg="#004043",fg="white",font=18)
m.add_cascade(label="Edit",menu=e)
e.add_command(label="Copy", command=copy_text)
e.add_command(label="Paste", command=paste_text)
e.add_command(label="Cut", command=cut_text)


root.config(menu=m)

Label(F,text="Notepad",font=("Arial", 24),fg="white",bg="#064e3b").pack()

t=Text(root,height=15,background="#004043",fg="white",font=14)
t.pack(fill="both",expand=True)

F2=Frame(root,bg="#064e3b",padx=10,pady=10)
F2.pack(fill="x")

Button(F2,text="SAVE",command=save,bg="#20bf55",fg="white",padx=20,pady=10,font=20).pack(side=LEFT,padx=10)
Button(F2,text="CLEAR",command=clear,bg="#20bf55",fg="white",padx=20,pady=10,font=20).pack(side=LEFT)
Button(F2, text="DELETE FILE", command=delete_file, bg="#20bf55", fg="white", padx=10, pady=10, font=20).pack(side=LEFT)
root.bind("<Control-s>",save)
root.bind("<Control-x>",clear)

root.mainloop()
