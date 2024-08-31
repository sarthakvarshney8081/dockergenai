from transformers import pipeline

# Load the text generation pipeline
generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt):
    results = generator(prompt, max_length=50)
    return results[0]['generated_text']

if __name__ == "__main__":
    prompt = input("Enter a prompt: ")
    print(generate_text(prompt))
