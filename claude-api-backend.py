from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

CLAUDE_API_KEY = os.environ.get('CLAUDE_API_KEY')
CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"

@app.route('/api/chat', methods=['POST'])
def chat_with_claude():
    user_message = request.json['message']
    
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": CLAUDE_API_KEY,
    }
    
    data = {
        "model": "claude-3-opus-20240229",
        "messages": [{"role": "user", "content": user_message}],
        "max_tokens": 1000
    }
    
    response = requests.post(CLAUDE_API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        claude_response = response.json()['content'][0]['text']
        return jsonify({"response": claude_response})
    else:
        return jsonify({"error": "Failed to get response from Claude API"}), 500

if __name__ == '__main__':
    app.run(debug=True)
