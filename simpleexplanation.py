from transformers import pipeline

# Initialize the pipeline with google/flan-t5-base
try:
    explainer = pipeline("text2text-generation", model="google/flan-t5-base")

except Exception as e:
    print(f"Error loading model: {e}")

    exit(1)




def explain_topic(topic):
    if not topic or not isinstance(topic, str):
        return "Error: Please provide a valid topic."

    prompt = f"In one clear, concise sentence, explain what '{topic}' is for a high school student."

    try:
        result = explainer(
            prompt,
            max_new_tokens=50,  # Keep output concise

            no_repeat_ngram_size=3,  # Prevent repetitive phrases

            do_sample=False,  # Greedy decoding for consistency

            num_beams=5,  # Beam search for better quality

            temperature=1.0  # Default temperature

        )

        print(f"Raw model output: {result}")  # Debug output

        return result[0]['generated_text'].strip()

    except Exception as e:

        return f"Error generating explanation: {e}"



# Example usage

user_input = input("Enter a topic to explain: ")
print(explain_topic(user_input))
