from transformers import pipeline

summarizer = pipeline("text2text-generation", model="google/flan-t5-small")

def summarize_text(text):
    prompt = f"Summarize the following text in simple 1 line:\\n{text}"

    result = summarizer(prompt, max_new_tokens=100)

    return result[0]['generated_text']




# Example usage
sample_text = input("Enter text to summarize: ")
print(summarize_text(sample_text))