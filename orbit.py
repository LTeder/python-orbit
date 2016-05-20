from Tkinter import *

class Orbit(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.width = 500
        self.height = 500
        self.canvas = Canvas(self, width=self.width, height=self.height, background="black")
        self.options = Frame(self, width=300, height=self.height)

        self.options.grid(row=0, column=1, sticky="nsew")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        
        self.sun = self.canvas.create_oval((self.width/2)-10, (self.height/2)+10,
            (self.width/2)+10, (self.height/2)-10, fill="yellow")
        
        self.canvas.bind("<ButtonRelease-1>", self.select)
        
    def select(self, event):
        try:
            item = event.widget.find_overlapping(event.x-1, event.y+1, event.x+1, event.y-1)[0]
        except IndexError: # For when there is no item
            item = 0 # This will eventually be integrated into overall options for the sim
        print item

if __name__ == "__main__":
    root = Tk()
    root.title("Simple Python Orbit Sim")
    Orbit(root).pack(fill="both", expand=True)
    root.mainloop()
