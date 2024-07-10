import streamlit as st
from sentiment_analysis_diverse import EmotionDetector

from recommendations import EmotionRecommendation

class MoodSyncStreamlit:
    def __init__(self):
        st.set_page_config(
            page_title="MoodSync - Your AI Journal",
            page_icon="😊",
            layout="wide"
        )
        self.set_styles()

    def set_styles(self):
        st.markdown(
            """
            <style>
                body {
                    background-color: #303030;
                    color: white;
                    font-family: 'Consolas', monospace;
                    font-size: 18px;
                }
                .stButton {
                    color: #ffffff;
                    background-color: #4caf50;
                    border: 2px solid #4caf50;
                    font-size: 18px;
                }
                .stButton:hover {
                    background-color: #45a049;
                }
                .stText {
                    color: white;
                    font-size: 18px;
                }
                .stMarkdown {
                    color: white;
                    font-size: 18px;
                }
                .stTextInput {
                    color: white;
                    background-color: #404040;
                    font-size: 18px;
                }
                .stTextArea {
                    color: white;
                    background-color: #404040;
                    font-size: 18px;
                }
                .stTitle {
                    color: #4caf50;
                    font-size: 36px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

    def analyze_mood(self, user_input):
        # Perform sentiment analysis using EmotionDetector
        emotion_detector = EmotionDetector()
        result_emotion_percentages = emotion_detector.detect_emotions(user_input)

        # Display the result
        result_text = "Emotion Breakdown:\n"
        for emotion, percentage in result_emotion_percentages.items():
            result_text += f"{emotion}: {percentage:.2f}%\n"

        # Display emotion breakdown
        st.markdown(result_text)

        # Get recommendation based on emotion breakdown
        recommendation = EmotionRecommendation.get_recommendation(result_emotion_percentages)

        # Display recommendation
        st.markdown(f"Recommendation: {recommendation}")

        # Display YouTube video recommendations
        youtube_links = self.get_youtube_links(result_emotion_percentages)
        for link in youtube_links:
            st.video(link)

        # Suggest mood-enhancing practices
        mood_practices = self.get_mood_practices(result_emotion_percentages)
        st.markdown("## Mood-Enhancing Practices:")
        for practice in mood_practices:
            st.markdown(f"- {practice}")

        # Update mood history
        new_entry = f"Entry: {user_input}\n{result_text}\nRecommendation: {recommendation}\n{'-'*30}\n"
        st.text_area("Mood History:", new_entry, height=200)

        # Save the note to a file or database for persistent storage
        self.save_note(new_entry)

    def get_youtube_links(self, emotion_percentages):
        # Customize YouTube links based on emotion
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

        highest_emotion = max(emotion_percentages, key=emotion_percentages.get)

        if highest_emotion == 'Joy':
            return joy_videos
        elif highest_emotion == 'Sadness':
            return sadness_videos
        elif highest_emotion == 'Neutral':
            return neutral_videos
        else:
            return []

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

    def save_note(self, note):
        # For demonstration purposes, this saves the note to a text file
        with open("mood_notes.txt", "a") as file:
            file.write(note + "\n\n")

    def display_notes(self):
        # Display saved mood notes
        with open("mood_notes.txt", "r") as file:
            st.text_area("Saved Mood Notes:", file.read(), height=300)

    def run(self):
        # Add a title
        st.title("MoodSync: AI Journal")

        # Text entry for mood
        user_input = st.text_area("Express your mood:", height=100)

        # Button to analyze mood
        if st.button("Analyze Mood"):
            self.analyze_mood(user_input)

        # Button to display saved notes
        if st.button("Show Mood Notes"):
            self.display_notes()

if __name__ == "__main__":
    app = MoodSyncStreamlit()
    app.run()
