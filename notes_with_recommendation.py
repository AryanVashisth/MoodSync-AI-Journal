import tkinter as tk
from tkinter import ttk, filedialog
from sentiment_analysis import MoodDetector, MoodRecommendation

class MoodSyncGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MoodSync - Your Mood Journal")

        self.style = ttk.Style()
        self.style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'), foreground='#3498db')
        self.style.configure('Result.TLabel', font=('Helvetica', 10, 'italic'), foreground='#2ecc71')

        self.create_widgets()

    def create_widgets(self):
        # Button to open file dialog
        self.open_file_button = ttk.Button(self.root, text="Open File", command=self.open_file)
        self.open_file_button.grid(row=0, column=0, pady=10)

        # Save history button
        self.save_history_button = ttk.Button(self.root, text="Save History", command=self.save_history)
        self.save_history_button.grid(row=0, column=1, pady=10)

        # Result label
        self.result_label = ttk.Label(self.root, text="", style='Result.TLabel')
        self.result_label.grid(row=1, column=0, pady=10, columnspan=2)

        # Separator
        separator = ttk.Separator(self.root, orient='horizontal')
        separator.grid(row=2, columnspan=2, sticky="ew", pady=10)

        # Mood history label
        self.mood_history_label = ttk.Label(self.root, text="Mood History:", style='Title.TLabel')
        self.mood_history_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        # Mood history text
        self.mood_history_text = tk.Text(self.root, height=10, width=50, wrap=tk.WORD)
        self.mood_history_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, 'r') as file:
                user_input = file.read()

                # Perform sentiment analysis using MoodDetector
                mood_detector = MoodDetector()
                result_mood_percentages = mood_detector.detect_mood(user_input)

                # Display the result
                result_text = "Mood Breakdown:\n"

                for mood, percentage in result_mood_percentages.items():
                    result_text += f"{mood}: {percentage:.2f}%\n"

                # Display mood breakdown
                self.result_label.config(text=result_text)

                # Get recommendation based on mood breakdown
                recommendation = MoodRecommendation.get_recommendation(result_mood_percentages)

                # Display recommendation in the mood history text
                self.mood_history_text.insert(tk.END, f"{result_text}\n{recommendation}\n{'-'*30}\n")

    def save_history(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, 'w') as file:
                history_content = self.mood_history_text.get("1.0", tk.END)
                file.write(history_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = MoodSyncGUI(root)
    root.mainloop()
