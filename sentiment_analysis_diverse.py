from textblob import TextBlob
from collections import Counter
import spacy

class EmotionDetector:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def detect_emotions(self, text):
        """
        Detects emotions in the input text using spaCy for context and TextBlob for sentiment.

        Parameters:
        - text (str): The input text for emotion detection.

        Returns:
        - emotion_percentages (dict): A dictionary containing emotion labels and their respective percentages.
        """
        # Use spaCy for sentence-level context-based analysis
        doc = self.nlp(text)

        # Initialize emotion labels
        emotion_labels = []

        # Analyze sentiment using TextBlob for the entire text
        textblob_polarity = TextBlob(text).sentiment.polarity

        # Map polarity score to emotions
        emotion_labels += self.map_score_to_emotions(textblob_polarity)

        # Analyze each sentence in the document
        for sentence in doc.sents:
            # Use TextBlob for sentence-level sentiment analysis
            sentence_polarity = TextBlob(sentence.text).sentiment.polarity

            # Map sentence-level polarity score to emotions
            emotion_labels += self.map_score_to_emotions(sentence_polarity)

            # Extract additional emotions from spaCy analysis
            emotion_labels += self.extract_spacy_emotions(sentence)

        # Count the emotion frequencies
        emotion_frequencies = Counter(emotion_labels)

        # Calculate the total number of emotions
        total_emotions = sum(emotion_frequencies.values())

        # Normalize frequencies to values between 0 and 1
        emotion_percentages = {label: (frequency / total_emotions) * 100 for label, frequency in emotion_frequencies.items()}

        return emotion_percentages

    def map_score_to_emotions(self, score):
        # Map polarity score to emotions based on thresholds
        emotion_labels = []

        if score >= 0.4:
            emotion_labels.append('joy')
        elif 0.2 <= score < 0.4:
            emotion_labels.append('happy')
        elif 0 <= score < 0.2:
            emotion_labels.append('neutral')
        elif -0.2 <= score < 0:
            emotion_labels.append('sad')
        elif -0.4 <= score < -0.2:
            emotion_labels.append('sadness')
        else:
            emotion_labels.append('anger')

        # Additional labels based on individual scores
        if score > 0.4:
            emotion_labels.append('positive')
        elif score < -0.4:
            emotion_labels.append('negative')

        # Additional emotion classes
        if score > 0.2:
            emotion_labels.append('surprise')
        elif score < -0.6:
            emotion_labels.append('fear')
        elif score < -0.4:
            emotion_labels.append('disgust')

        return emotion_labels

    def extract_spacy_emotions(self, sentence):
        # Extract additional emotions based on spaCy analysis at the sentence level
        # You can customize this based on the specific emotions you want to detect
        emotion_labels = []
        for token in sentence:
            if "anger" in token.text.lower():
                emotion_labels.append("anger")
            # Add more conditions for other emotions
            
        return emotion_labels

# Example usage:
# text_to_analyze = input("Enter your text: ")
# emotion_detector = EmotionDetector()
# result_emotion_percentages = emotion_detector.detect_emotions(text_to_analyze)

# print(f"Emotion Percentages: {result_emotion_percentages}")
