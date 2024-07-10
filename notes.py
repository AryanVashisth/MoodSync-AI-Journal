import tkinter as tk
from tkinter import scrolledtext
import datetime

class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes App")
        self.create_widgets()

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(pady=10)

        save_button = tk.Button(self.root, text="Save Note", command=self.save_note)
        save_button.pack()

    def save_note(self):
        new_note = self.text_area.get("1.0", tk.END).strip()
        if new_note:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note_text = f"{timestamp}:\n{new_note}\n{'='*30}\n"

            with open("notes.txt", "a") as file:
                file.write(note_text)

            self.text_area.delete("1.0", tk.END)
            print("Note added successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
