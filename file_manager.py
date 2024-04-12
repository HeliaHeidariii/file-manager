import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


class FileManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Management")
        self.master.geometry("368x545")
        self.master.configure(bg="#2C3E50")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="What would you like to do?", bg="#2C3E50",
                 fg="white", font=("Helvetica", 14, "bold")).pack(pady=10)

        buttons = [
            ("Open File", self.open_file),
            ("Copy File", self.copy_file),
            ("Delete File", self.delete_file),
            ("Rename File", self.rename_file),
            ("Move File", self.move_file),
            ("Create Folder", self.make_directory),
            ("Delete Folder", self.remove_directory),
            ("List All Files", self.list_files)
        ]

        for text, command in buttons:
            tk.Button(self.master, text=text, fg="white", bg="#3498DB", font=(
                "Helvetica", 12, "bold"), width=20, height=2, command=command).pack(pady=5)

    def file_open_box(self):
        return filedialog.askopenfilename()

    def directory_open_box(self):
        return filedialog.askdirectory()

    def open_file(self):
        path = self.file_open_box()
        if path:
            try:
                os.startfile(path)
            except TypeError:
                messagebox.showinfo("!Error", "File not found!")

    def copy_file(self):
        source = self.file_open_box()
        destination = self.directory_open_box()
        if source and destination:
            try:
                shutil.copy(source, destination)
                messagebox.showinfo("!Success", "File copied successfully!")
            except:
                messagebox.showinfo("!Error", "Copy failed!")

    def delete_file(self):
        path = self.file_open_box()
        if path:
            try:
                os.remove(path)
                messagebox.showinfo("!Success", "File deleted successfully!")
            except:
                messagebox.showinfo("!Error", "File deletion failed!")

    def rename_file(self):
        file = self.file_open_box()
        if file:
            try:
                path1 = os.path.dirname(file)
                extension = os.path.splitext(file)[1]
                new_name = input("new name: ")
                path2 = os.path.join(path1, new_name + extension)
                os.rename(file, path2)
            except:
                messagebox.showinfo("!Error", "Failed to rename!")

    def move_file(self):
        source = self.file_open_box()
        destination = self.directory_open_box()
        if source and destination:
            if source == destination:
                messagebox.showinfo("!Error", "Destination path unchanged!")
            else:
                try:
                    shutil.move(source, destination)
                    messagebox.showinfo("!Success", "File moved successfully!")
                except:
                    messagebox.showinfo("!Error", "File move failed!")

    def make_directory(self):
        path = self.directory_open_box()
        if path:
            name = input("name: ")
            path = os.path.join(path, name)
            try:
                os.mkdir(path)
            except:
                messagebox.showinfo("!Error", "Directory creation failed!")

    def remove_directory(self):
        path = self.directory_open_box()
        if path:
            try:
                os.rmdir(path)
            except:
                messagebox.showinfo("!Error", "Directory deletion failed!")

    def list_files(self):
        path = self.directory_open_box()
        if path:
            file_list = sorted(os.listdir(path))
            for i in file_list:
                print(i)


def main():
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
