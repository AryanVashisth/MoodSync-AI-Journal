import streamlit as st
from sentiment_analysis_diverse import EmotionDetector

# Create an instance of the EmotionDetector
emotion_detector = EmotionDetector()

# Streamlit app
def main():
    st.title("Emotion Detector Web App")
    
    # Text input
    user_input = st.text_area("Enter your text:", "")

    # Detect emotions when the user clicks the button
    if st.button("Detect Emotions"):
        result_emotion_percentages = emotion_detector.detect_emotions(user_input)

        # Display emotion percentages
        st.subheader("Emotion Percentages:")
        for emotion, percentage in result_emotion_percentages.items():
            st.write(f"{emotion.capitalize()}: {percentage:.2f}%")

if __name__ == "__main__":
    main()
