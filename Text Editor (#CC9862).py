import tkinter as tk
from tkinter import filedialog, messagebox
import os

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.file_path = None
        
        self.create_widgets()

    def create_widgets(self):
        self.text_area = tk.Text(self.root, wrap='word', font=("Arial", 12))
        self.text_area.pack(expand=1, fill='both')
        
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)
        
        edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Word Count", command=self.word_count)

    def new_file(self):
        self.file_path = None
        self.text_area.delete(1.0, tk.END)
        self.root.title("Simple Text Editor - New File")

    def open_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            with open(self.file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())
            self.root.title(f"Simple Text Editor - {os.path.basename(self.file_path)}")

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        self.file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"Simple Text Editor - {os.path.basename(self.file_path)}")

    def exit_editor(self):
        self.root.quit()

    def word_count(self):
        text = self.text_area.get(1.0, tk.END)
        words = len(text.split())
        messagebox.showinfo("Word Count", f"Words: {words}")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
