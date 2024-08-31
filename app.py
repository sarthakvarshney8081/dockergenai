from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize text-generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Define the /generate endpoint to accept POST requests
@app.route('/generate', methods=['POST'])
def generate_text():
    # Ensure the request is a POST request
    if request.method == 'POST':
        # Parse the JSON request body
        data = request.get_json()
        
        # Check if 'prompt' exists in the request
        if 'prompt' in data:
            prompt = data['prompt']
            results = generator(prompt, max_length=50, num_return_sequences=1)
            return jsonify({"generated_text": results[0]['generated_text']})
        else:
            return jsonify({"error": "No prompt provided"}), 400
    else:
        return jsonify({"error": "Invalid method"}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
