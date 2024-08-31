from transformers import pipeline
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load the text generation pipeline
generator = pipeline("text-generation", model="gpt2")

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.get_json()  # Get JSON data from POST request
    prompt = data.get("prompt", "")
    
    # Generate text
    results = generator(prompt, 
                        max_length=50,  
                        num_return_sequences=1,  
                        temperature=0.7,  
                        top_k=50,  
                        top_p=0.9  
                        )
    
    return jsonify({"generated_text": results[0]['generated_text']})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
