# mood_sync_api.py

from flask import Flask, request, jsonify
from sentiment_analysis import MoodDetector

app = Flask(__name__)
mood_detector = MoodDetector()

@app.route('/api/analyze_mood', methods=['POST'])
def analyze_mood():
    data = request.json
    user_input = data.get('text', '')
    
    result_mood_breakdown = mood_detector.detect_mood(user_input)

    result_text = "Mood Breakdown:\n"
    for mood, count in result_mood_breakdown.items():
        result_text += f"{mood}: {count}\n"

    response_data = {
        'result': result_text
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
