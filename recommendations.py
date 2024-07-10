import webbrowser

class EmotionRecommendation:
    JOY_VIDEOS = [
        "https://www.youtube.com/watch?v=ztMOLWAqL6E",  # Guided Meditation for Positive Energy
        "https://www.youtube.com/watch?v=3tmd-ClpJxA",  # Pharrell Williams - Happy (Official Music Video)
    ]

    SADNESS_VIDEOS = [
        "https://www.youtube.com/watch?v=hvOgpzRJ1qg",  # Guided Meditation for Healing Sadness
        "https://www.youtube.com/watch?v=UxUw2NMzc3U",  # 3 Hours of Relaxing Healing Music | Meditation & Sleep
    ]

    NEUTRAL_VIDEOS = [
        "https://www.youtube.com/watch?v=W0mGXL16ygI",  # Guided Mindfulness Meditation on Breath
        "https://www.youtube.com/watch?v=3GwjfUFyY6M",  # Relaxing Music & Soft Rain Sounds: Relaxing Piano Music, Sleep Music, Peaceful Music
    ]

    @staticmethod
    def get_recommendation(emotion_percentages):
        highest_emotions = [emotion for emotion, percentage in emotion_percentages.items() if percentage == max(emotion_percentages.values())]

        if 'Joy' in highest_emotions:
            return "You seem to be in a joyful mood. Consider doing activities that bring you happiness and share your joy with others."

        elif 'Sadness' in highest_emotions:
            return "I sense some sadness. It's okay to feel this way. Take some time for self-care and reach out to friends or family for support."

        elif 'Neutral' in highest_emotions:
            return "You're expressing a neutral mood. Take some time for self-reflection and engage in activities that bring you peace."

        else:
            return "Keep expressing yourself! Your emotions are unique, and it's essential to acknowledge and understand them."

    @staticmethod
    def get_meditation_videos(emotion_percentages):
        highest_emotion = max(emotion_percentages, key=emotion_percentages.get)

        if highest_emotion == 'Joy':
            return EmotionRecommendation.JOY_VIDEOS

        elif highest_emotion == 'Sadness':
            return EmotionRecommendation.SADNESS_VIDEOS

        elif highest_emotion == 'Neutral':
            return EmotionRecommendation.NEUTRAL_VIDEOS

        else:
            return []

    @staticmethod
    def open_youtube_videos(emotion_percentages):
        meditation_videos = EmotionRecommendation.get_meditation_videos(emotion_percentages)

        if meditation_videos:
            highest_emotion = max(emotion_percentages, key=emotion_percentages.get)
            print(f"Opening YouTube videos for {highest_emotion}...\n")

            for i, video_url in enumerate(meditation_videos, start=1):
                print(f"Video {i}: {video_url}")
                webbrowser.open_new_tab(video_url)

        else:
            print("No specific videos found for the detected emotion.")

# Example usage:
# result_emotion_percentages is the dictionary obtained from EmotionDetector
# recommendation = EmotionRecommendation.get_recommendation(result_emotion_percentages)
# meditation_videos = EmotionRecommendation.get_meditation_videos(result_emotion_percentages)
# print(f"Recommendation: {recommendation}")
# print(f"Meditation Videos: {meditation_videos}")
# EmotionRecommendation.open_youtube_videos(result_emotion_percentages)
