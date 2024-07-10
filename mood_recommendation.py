import os
import openai

class MoodRecommendation:
    @staticmethod
    def get_recommendation(mood_breakdown):
        # You can customize the recommendations based on the mood breakdown
        highest_mood = max(mood_breakdown, key=mood_breakdown.get)
        recommendation = f"Recommendation for {highest_mood}:"

        if highest_mood == "Happy":
            recommendation += MoodRecommendation.get_happy_recommendation()
        elif highest_mood == "Sad":
            recommendation += MoodRecommendation.get_sad_recommendation()
        elif highest_mood == "Angry":
            recommendation += MoodRecommendation.get_angry_recommendation()
        # Add more conditions for other emotions

        return recommendation

    @staticmethod
    def get_happy_recommendation():
        return " Do something that brings you joy and happiness."

    @staticmethod
    def get_sad_recommendation():
        return " Consider talking to a friend or engaging in activities that uplift your mood."

    @staticmethod
    def get_angry_recommendation():
        return " Take a break, practice deep breathing, or engage in physical activity to release tension."

    # Add more methods for other emotions

    @staticmethod
    def get_chatgpt_recommendation():
        # Use environment variable to get the API key
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OpenAI API key not found. Set the OPENAI_API_KEY environment variable.")

        openai.api_key = api_key

        prompt = "I'm feeling "
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7
        )

        return response.choices[0].text.strip()
