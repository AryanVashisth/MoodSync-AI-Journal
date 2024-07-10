import streamlit as st
from sentiment_analysis_multi import EmotionDetector
from recommendations import EmotionRecommendation

class MoodSyncStreamlit:
    def __init__(self):
        st.title("MoodSync - Your Mood Journal")

    def analyze_mood(self, user_input):
        # Perform sentiment analysis using EmotionDetector
        emotion_detector = EmotionDetector()
        result_emotion_percentages = emotion_detector.detect_emotions(user_input)

        # Display the result
        result_text = "Emotion Breakdown:\n"

        for emotion, percentage in result_emotion_percentages.items():
            result_text += f"{emotion}: {percentage:.2f}%\n"

        # Display emotion breakdown
        st.write(result_text)

        # Get recommendation based on emotion breakdown
        recommendation = EmotionRecommendation.get_recommendation(result_emotion_percentages)

        # Display recommendation
        st.write(f"Recommendation: {recommendation}")

        # Update mood history
        new_entry = f"Entry: {user_input}\n{result_text}\nRecommendation: {recommendation}\n{'-'*30}\n"
        st.text_area("Mood History:", new_entry, height=200)

    def run(self):
        # Text entry
        user_input = st.text_area("Express your mood:", height=100)

        # Button to analyze mood
        if st.button("Analyze Mood"):
            self.analyze_mood(user_input)

if __name__ == "__main__":
    app = MoodSyncStreamlit()
    app.run()
