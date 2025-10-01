from transformers import pipeline

quiz_generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_quiz(text):
    prompt = f"Create 3 multiple-choice questions and answers from the text: {text}"
    result = quiz_generator(prompt, max_length=300)
    return result[0]['generated_text']




# Example of dynamic input
user_input = input("Enter text for quiz generation: ")
print(generate_quiz(user_input))
