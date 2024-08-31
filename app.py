from transformers import pipeline

# Load the text generation pipeline
generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt):
    # Adjust parameters for better control
    results = generator(prompt, 
                        max_length=50,  # Maximum length of the generated text
                        num_return_sequences=1,  # Number of sequences to generate
                        temperature=0.7,  # Controls randomness; lower is more focused
                        top_k=50,  # Limits sampling pool to top k tokens
                        top_p=0.9  # Nucleus sampling; considers top p cumulative probability
                        )
    return results[0]['generated_text']

if __name__ == "__main__":
    prompt = input("Enter a prompt: ")
    print(generate_text(prompt))
