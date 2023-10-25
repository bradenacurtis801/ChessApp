import tkinter as tk
from tkinter.simpledialog import Dialog
from tkinter import simpledialog, ttk

class LargeInputDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None, prompt=None):
        self.prompt = prompt
        self.user_input = None
        super().__init__(parent, title=title)

    def body(self, master):
        if self.prompt:
            tk.Label(master, text=self.prompt).grid(row=0)

        # Create a PanedWindow to contain the Text widget
        self.paned_window = ttk.PanedWindow(master, orient=tk.VERTICAL)
        self.paned_window.grid(row=1, padx=20, pady=20, sticky="nsew")
        
        # Create a larger and adjustable text field
        self.text = tk.Text(self.paned_window, width=40, height=10)
        
        # Add the Text widget to the PanedWindow
        self.paned_window.add(self.text)

        # Bind the "Enter" key to insert a newline in the Text widget
        self.text.bind("<Return>", self.insert_newline)

        # Configure the row and column to be expandable
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)

        return self.text

    def buttonbox(self):
        # Override the buttonbox method to remove the "Enter" key binding from the ok method
        box = tk.Frame(self)
        w = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Escape>", self.cancel)
        box.pack()

    def insert_newline(self, event=None):
        # Insert a newline character at the current cursor position
        self.text.insert(tk.INSERT, "\n")
        return "break"  # Prevent further processing of the event

    def apply(self):
        self.user_input = self.text.get("1.0",'end-1c')


def asklargeinput(parent, title, prompt):
    dialog = LargeInputDialog(parent, title=title, prompt=prompt)
    return dialog.user_input

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    result = asklargeinput(root, "Description", "Please describe your test case:")
    print(result)
