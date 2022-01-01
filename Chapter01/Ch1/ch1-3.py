import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        self.label_text = tk.StringVar()
        self.label_text.set("My Name is:")

        self.name_text=tk.StringVar()

        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)

        self.name_Entry= tk.Entry(self,textvar=self.name_text)
        self.name_Entry.pack(fill=tk.BOTH,expand=1,padx=20,pady=20)

        hello_button = tk.Button(self, text="Say Hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))

        goodbye_button = tk.Button(self, text="Say Goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def say_hello(self):
        msgbox.showinfo("Hello","Hello " + self.name_Entry.get())

    def say_goodbye(self):
        if  msgbox.askyesno("Close Window?","Do you want to close this window?"):
            self.label_text.set("Window will close in 2 seconds! \n Goodbye "+ self.name_Entry.get())
            self.after(2000, self.destroy)
        else:
            msgbox.showinfo("Not Closing","Great! This Window will stay open. ")


if __name__ == "__main__":
    window = Window()
    window.mainloop()

