from tkinter import *

master = Tk()
master.title("Notice")


def show():
    add.grid(row=0, column=0)


def forget():
    add.grid_forget()



def Add():
    forget()
    master.title("Untitled")

    t1 = Text(master)
    t1.grid(row=0, columnspan=2)


    def cancelcmd():
        forget_new()
        show()

    def forget_new():
        t1.grid_forget()
        cancel.grid_forget()
        save.grid_forget()

    def savecmd():
        forget_new()
        l1 = Label(master, text = "Name ")
        l1.grid(row = 0, column = 0)

        e1 = Entry(master)
        e1.grid(row = 0, column = 1)

        namefinish = Buton(master, text = "fiish")

    cancel = Button(master, text="Cancel", fg="red", command=cancelcmd)
    cancel.grid(row=1, column=0)

    save = Button(master, text="Save", command = savecmd)
    save.grid(row=1, column=1)


add = Button(master, text="Add", command=Add)
add.grid(row=0, column="0")

master.mainloop()
