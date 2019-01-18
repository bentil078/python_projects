from tkinter import *
#from fetchit import fetch

class ChatGui:
    def __init__(self):
        window = Tk()
        window.title("LAN CHAT")
        

        frame1 = Frame(window)
        frame1.pack()
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.txt = Text(frame1, width = 40, height = 10,
                   yscrollcommand = scrollbar.set)
        self.txt.config(font=("times", 16, "italic"))
        self.txt.pack()
        scrollbar.config(command = self.txt.yview)

        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "Type Here")
        label.grid(row=1, column=1, padx=5)
        

        self.var = StringVar()
        self.ent = Entry(frame2, textvariable = self.var)
        self.ent.grid(row=1, column=2, padx=5)
        
        
        self.ent.focus()
        self.ent.bind('<Return>', (lambda event: self.fetch()))
        btn = Button(frame2, text = 'Send', command = self.fetch)
        btn.grid(row=1, column=3, padx=5)

        btclear = Button(frame2, text="Clear", command=self.clear)
        btclear.grid(row=1, column=4)
        #btclear.config(relief=RAISED)

        window.mainloop()

    def fetch(self):
        #print("%s" % self.ent.get())
        self.txt.insert(END,'%s\n' % self.var.get())
        self.ent.delete(0, END)

    def clear(self):
        pass
ChatGui()

