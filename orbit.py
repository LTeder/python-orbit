import Tkinter as tk


class Orbit(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.width = 500
        self.height = 500
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, background="black")
        self.options = tk.Frame(self, height=self.height)
        tk.Label(self.options, text="Press RETURN to confirm a value.").pack()

        self.options.grid(row=0, column=1, sticky="nsew")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        
        # I plan to eventually put window size configs
        self.sun = self.canvas.create_oval((self.width/2)-10, (self.height/2)+10,
            (self.width/2)+10, (self.height/2)-10, fill="yellow")
        
        self.canvas.bind("<ButtonRelease-1>", self.select)
        
        self.base_options = [
            ("Test:", 42),
            ("Test 2:", 243)]
        
        self.item_options = [
            ("Mass:", 1000000),
            ("Density:", 23)]
        
    def select(self, event):
        try:
            item = self.canvas.find_overlapping(event.x-1, event.y+1, event.x+1, event.y-1)[0]
        except IndexError:  # For when there is no item in the click zone
            item = 0  # This will eventually be integrated into overall options for the sim
        
        try:
            for frame in self.option_frames:  # Clearing option frames
                frame.pack_forget()
            for option_pair in self.option_items:
                option_pair[0].pack_forget()
                option_pair[1].pack_forget()
        except AttributeError:
            pass  # The first run won't have these variables in place
        self.option_frames = []  # Resetting variables
        self.option_items = []
        count = 0
            
        if item == 0:
            option_set = self.base_options  # Sets which set of options to use
        else:
            option_set = self.item_options
        for option in option_set:  # Parses through option data
            self.option_frames.append(tk.Frame(self.options))
            self.option_frames[count].pack()
            self.option_items.append((
                tk.Label(self.option_frames[count], text=option[0]),
                tk.Entry(self.option_frames[count])))
            self.option_items[count][0].pack(side=tk.LEFT)
            self.option_items[count][1].pack(side=tk.RIGHT)
            count += 1
            
        '''
        Currently, the option data has defined values for the second item.
        I need to create a system that gets data depending on the canvas item.
        '''
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("2D Python Orbit Sim")
    Orbit(root).pack()
    root.mainloop()
