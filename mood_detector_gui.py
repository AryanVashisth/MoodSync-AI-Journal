import tkinter as tk
from tkinter import ttk
from sentiment_analysis_diverse import EmotionDetector
from recommendations import EmotionRecommendation
from datetime import datetime

class MoodSyncGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MoodSync - Your Mood Journal")

        self.create_widgets()

    def create_widgets(self):
        # Text entry
        self.text_label = ttk.Label(self.root, text="Express your mood:")
        self.text_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.text_entry = ttk.Entry(self.root, width=70)  # Expanded width
        self.text_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Button to analyze mood
        self.analyze_button = ttk.Button(self.root, text="Analyze Mood", command=self.analyze_mood)
        self.analyze_button.grid(row=1, column=1, pady=10)

        # Result label
        self.result_label = ttk.Label(self.root, text="", font=('Helvetica', 10, 'italic'))
        self.result_label.grid(row=2, column=1, pady=10)

        # Save button
        self.save_button = ttk.Button(self.root, text="Save Entry", command=self.save_entry)
        self.save_button.grid(row=3, column=1, pady=10)

        # Separator
        separator = ttk.Separator(self.root, orient='horizontal')
        separator.grid(row=4, columnspan=2, sticky="ew", pady=10)

        # Mood history label
        self.mood_history_label = ttk.Label(self.root, text="Mood History:")
        self.mood_history_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

        # Mood history text
        self.mood_history_text = tk.Text(self.root, height=10, width=70, wrap=tk.WORD)  # Expanded width
        self.mood_history_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def analyze_mood(self):
        # Get user input from the entry
        user_input = self.text_entry.get()

        # Perform sentiment analysis using EmotionDetector
        emotion_detector = EmotionDetector()
        result_emotion_percentages = emotion_detector.detect_emotions(user_input)

        # Display the result
        result_text = "Emotion Breakdown:\n"

        for emotion, percentage in result_emotion_percentages.items():
            result_text += f"{emotion}: {percentage:.2f}%\n"

        # Display emotion breakdown
        self.result_label.config(text=result_text)

        # Get recommendation based on emotion breakdown
        recommendation = EmotionRecommendation.get_recommendation(result_emotion_percentages)

        # Display recommendation
        self.mood_history_text.insert(tk.END, recommendation + "\n")

        # Update mood history
        current_mood_history = self.mood_history_text.get("1.0", tk.END)
        new_entry = f"Entry: {user_input}\n{result_text}\n{recommendation}\n{'-'*30}\n"
        self.mood_history_text.delete("1.0", tk.END)
        self.mood_history_text.insert(tk.END, new_entry + current_mood_history)

        # Open a new window to display emotion breakdown and recommendation
        self.display_result_window(result_emotion_percentages, recommendation)

    def display_result_window(self, result_emotion_percentages, recommendation):
        result_window = tk.Toplevel(self.root)
        result_window.title("Emotion Analysis Result")

        result_label = ttk.Label(result_window, text="Emotion Breakdown:", font=('Helvetica', 12, 'bold'))
        result_label.pack(pady=10)

        for emotion, percentage in result_emotion_percentages.items():
            label = ttk.Label(result_window, text=f"{emotion}: {percentage:.2f}%")
            label.pack()

        recommendation_label = ttk.Label(result_window, text=f"\nRecommendation:\n{recommendation}", font=('Helvetica', 10, 'italic'))
        recommendation_label.pack(pady=10)

    def save_entry(self):
        # Get current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get user input and recommendation
        user_input = self.text_entry.get()
        recommendation = self.mood_history_text.get("1.0", tk.END)

        # Format the entry
        entry_to_save = f"Date and Time: {current_datetime}\nEntry: {user_input}\nRecommendation: {recommendation}\n{'-'*30}\n"

        # Save to a file (you can customize the file path)
        with open("mood_journal_entries.txt", "a") as file:
            file.write(entry_to_save)
        # Optional: Show a message that the entry is saved
        tk.messagebox.showinfo("Entry Saved", "Your mood entry has been saved.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MoodSyncGUI(root)
    root.mainloop()
