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
                    font-size: 18px.
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
        try:
            emotion_detector = EmotionDetector()
            result_emotion_percentages = emotion_detector.detect_emotions(user_input)

            self.display_result(user_input, result_emotion_percentages)

        except Exception as e:
            st.error(f"An error occurred: {e}")

        finally:
            st.empty()  # Clear any loading indicators

    def display_result(self, user_input, emotion_percentages):
        self.display_emotion_result(emotion_percentages)

        recommendation = EmotionRecommendation.get_recommendation(emotion_percentages)
        st.markdown(f"Recommendation: {recommendation}")

        meditation_videos = EmotionRecommendation.get_meditation_videos(emotion_percentages)
        self.display_youtube_links(meditation_videos)

        mood_practices = self.get_mood_practices(emotion_percentages)
        self.display_mood_practices(mood_practices)

        new_entry = self.get_entry_text(user_input, emotion_percentages, recommendation)
        st.text_area("Mood History:", new_entry, height=200)
        self.save_note(new_entry)

    def display_emotion_result(self, emotion_percentages):
        result_text = "Emotion Breakdown:\n"
        for emotion, percentage in emotion_percentages.items():
            result_text += f"{emotion}: {percentage:.2f}%\n"
        st.markdown(result_text)

    def display_youtube_links(self, youtube_links):
        st.markdown("## YouTube Video Recommendations:")
        for link in youtube_links:
            st.markdown(f"[Video Link]({link})", unsafe_allow_html=True)

    def display_mood_practices(self, mood_practices):
        st.markdown("## Mood-Enhancing Practices:")
        for practice in mood_practices:
            st.markdown(f"- {practice}")

    def get_mood_practices(self, emotion_percentages):
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

    def get_entry_text(self, user_input, emotion_percentages, recommendation):
        result_text = self.get_emotion_result_text(emotion_percentages)
        entry_text = f"Entry: {user_input}\n{result_text}\nRecommendation: {recommendation}\n{'-'*30}\n"
        return entry_text

    def get_emotion_result_text(self, emotion_percentages):
        result_text = "Emotion Breakdown:\n"
        for emotion, percentage in emotion_percentages.items():
            result_text += f"{emotion}: {percentage:.2f}%\n"
        return result_text

    def save_note(self, note):
        with open("mood_notes.txt", "a") as file:
            file.write(note + "\n\n")

    def display_notes(self):
        with open("mood_notes.txt", "r") as file:
            st.text_area("Saved Mood Notes:", file.read(), height=300)

    def run(self):
        st.title("MoodSync: AI Journal")
        user_input = st.text_area("Express your mood:", height=100)

        if st.button("Analyze Mood"):
            with st.spinner("Analyzing Mood..."):
                self.analyze_mood(user_input)

        if st.button("Show Mood Notes"):
            self.display_notes()

if __name__ == "__main__":
    app = MoodSyncStreamlit()
    app.run()
