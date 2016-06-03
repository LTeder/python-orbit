import Tkinter as tk
import orbitmath
import random


class Orbit(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.width = 500
        self.height = 500
        self.scale = 50
        self.large = self.scale * [self.width if self.width > self.height else self.height]
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, background='black')
        self.options = tk.Frame(self, height=self.height)
        tk.Label(self.options,
                 text="Confirm value: Return.\nUnits: Light Seconds.\n1 Pixel = %s Light Seconds." % self.scale).pack()

        self.options.grid(row=0, column=1, sticky='nsew')
        self.canvas.grid(row=0, column=0, sticky='nsew')

        # I plan to eventually put window size configs (hence the computations for core object size)
        self.bodies = {}
        self.sun = self.canvas.create_oval((self.width / 2) - 10, (self.height / 2) + 10,
                                           (self.width / 2) + 10, (self.height / 2) - 10, fill='yellow')

        self.canvas.bind('<ButtonRelease-1>', self.select)

        self.base_options = ["Scale:", "Test 2:"]

        self.item_options = ["Apoapsis:", "Periapsis:", "Arg. of Periapsis:"]

        self.item = 0

        self.option_frames = []
        self.option_items = []

    def spawn_item(self, apoaps=None, periaps=None,
                   argp=random.randint(0, 359)):  # Creates the canvas item, ellipse, and dictionary for each item
        if apoaps is None:
            apoaps = random.randint(2, self.large)
        if periaps is None:
            periaps = random.randint(1, apoaps)
        focus_displacement = (apoaps + periaps) / 2
        self.bodies[self.canvas.create_line(orbitmath.poly_oval())] = [apoaps, periaps, argp]
        pass

    def select(self, event):
        try:
            self.item = self.canvas.find_overlapping(event.x - 1, event.y + 1, event.x + 1, event.y - 1)[0]
        except IndexError:  # For when there is no self.item in the click zone
            pass  # Overall options for the sim (maybe save/load)
        try:
            for frame in self.option_frames:  # Clearing option frames
                frame.pack_forget()
            for option_pair in self.option_items:
                option_pair[0].pack_forget()
                option_pair[1].pack_forget()
        except AttributeError:
            pass  # The first run won't have these variables in place
        if self.item == 0:
            option_set = self.base_options  # Sets which set of options to use
        else:
            option_set = self.item_options
        count = 0
        for option in option_set:  # Parses through option data
            self.option_frames.append(tk.Frame(self.options))
            self.option_frames[count].pack()
            self.option_items.append((tk.Label(self.option_frames[count], text=option),
                                      tk.Entry(self.option_frames[count])))
            self.option_items[count][0].pack(side=tk.LEFT)
            self.option_items[count][1].bind('<Return>', self.param_update)
            self.option_items[count][1].insert(0, self.item[self.option_items[count][0].cget('text')])
            self.option_items[count][1].pack(side=tk.RIGHT)
            count += 1

    def param_update(self, event):  # Updates the option of an element
        for item in self.option_items:  # Finds the tuple containing the triggering widget
            if item[0] == event:
                option = item
        self.item[option[0].cget('text')] = float(option[1].get('1.0', 'end-1c'))


if __name__ == '__main__':
    root = tk.Tk()
    root.title("2D Python Orbit Sim")
    Orbit(root).pack()
    root.mainloop()
