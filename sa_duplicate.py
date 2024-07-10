import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from sentiment_analysis_diverse import EmotionDetector
from recommendations import EmotionRecommendation

class MoodSyncTkinter:
    def __init__(self, master):
        self.master = master
        master.title("MoodSync - Your AI Journal")
        master.geometry("800x600")

        self.set_styles()

        self.text_entry = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=5)
        self.text_entry.pack(pady=10)

        self.analyze_button = tk.Button(master, text="Analyze Mood", command=self.analyze_mood)
        self.analyze_button.pack(pady=10)

        self.notes_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=80, height=15)
        self.notes_text.pack(pady=10)

        self.show_notes_button = tk.Button(master, text="Show Mood Notes", command=self.display_notes)
        self.show_notes_button.pack(pady=10)

        self.youtube_frame = tk.Frame(master)
        self.youtube_frame.pack(pady=10)

    def set_styles(self):
        style = ttk.Style()
        style.configure("TButton", foreground="white", background="#4caf50", font=("Consolas", 18))
        style.map("TButton", background=[("active", "#45a049")])

        self.master.configure(bg="#303030")
        self.text_entry.configure(bg="#404040", fg="white", font=("Consolas", 18))
        self.notes_text.configure(bg="#404040", fg="white", font=("Consolas", 18))

    def analyze_mood(self):
        user_input = self.text_entry.get("1.0", tk.END)
        try:
            emotion_detector = EmotionDetector()
            result_emotion_percentages = emotion_detector.detect_emotions(user_input)

            result_text = "Emotion Breakdown:\n"
            for emotion, percentage in result_emotion_percentages.items():
                result_text += f"{emotion}: {percentage:.2f}%\n"

            recommendation = EmotionRecommendation.get_recommendation(result_emotion_percentages)

            mood_practices = self.get_mood_practices(result_emotion_percentages)

            new_entry = (
                f"Entry: {user_input}\n{result_text}\nRecommendation: {recommendation}\n{'-'*30}\n"
            )
            self.save_note(new_entry)

            self.display_youtube_links(recommendation)

        except Exception as e:
            self.display_error(f"An error occurred: {e}")

    def display_youtube_links(self, mood):
        # Customize YouTube links based on the user's mood
        joy_videos = [
            "https://www.youtube.com/watch?v=3tmd-ClpJxA",  # Pharrell Williams - Happy (Official Music Video)
            "https://www.youtube.com/watch?v=KQ6zr6kCPj8",  # Try Not To Laugh Challenge - Funny Kids Fails Compilation 2021
        ]

        sadness_videos = [
            "https://www.youtube.com/watch?v=UxUw2NMzc3U",  # 3 Hours of Relaxing Healing Music | Meditation & Sleep
        ]

        neutral_videos = [
            "https://www.youtube.com/watch?v=3GwjfUFyY6M",  # Relaxing Music & Soft Rain Sounds: Relaxing Piano Music, Sleep Music, Peaceful Music
        ]

        youtube_links = []
        if mood == 'Joy':
            youtube_links = joy_videos
        elif mood == 'Sadness':
            youtube_links = sadness_videos
        elif mood == 'Neutral':
            youtube_links = neutral_videos

        for i, link in enumerate(youtube_links, start=1):
            youtube_label = tk.Label(self.youtube_frame, text=f"Video {i}", fg="white", bg="#303030")
            youtube_label.pack()
            link_label = tk.Label(self.youtube_frame, text=link, fg="blue", cursor="hand2", bg="#303030")
            link_label.pack()
            link_label.bind("<Button-1>", lambda event, url=link: self.open_link(url))

    def open_link(self, url):
        import webbrowser
        webbrowser.open_new_tab(url)

    def get_mood_practices(self, emotion_percentages):
        # Customize mood-enhancing practices based on emotion
        joy_practices = [
            "Practice gratitude by writing down three things you're grateful for today.",
            "Engage in physical activity like a short walk or quick workout.",
        ]

        sadness_practices = [
            "Listen to uplifting music or watch a funny video to lighten your mood.",
            "Try deep-breathing exercises to help calm your mind and body.",
        ]

        neutral_practices = [
            "Take a few moments for mindfulness meditation to center yourself.",
            "Read a motivational quote or book to boost your spirits.",
        ]

        highest_emotion = max(emotion_percentages, key=emotion_percentages.get)

        if highest_emotion == 'Joy':
            return joy_practices
        elif highest_emotion == 'Sadness':
            return sadness_practices
        elif highest_emotion == 'Neutral':
            return neutral_practices
        else:
            return []

    def display_error(self, message):
        tk.messagebox.showerror("Error", message)

    def display_notes(self):
        try:
            with open("mood_notes.txt", "r") as file:
                notes_content = file.read()
                self.notes_text.delete(1.0, tk.END)
                self.notes_text.insert(tk.END, notes_content)
        except FileNotFoundError:
            self.display_error("No mood notes found.")

    def save_note(self, note):
        with open("mood_notes.txt", "a") as file:
            file.write(note + "\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = MoodSyncTkinter(root)
    root.mainloop()
