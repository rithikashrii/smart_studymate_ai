def generate_detailed_notes(text):
    # Simplified logic – replace with AI model or NLP rules if needed
    sentences = text.split('.')
    notes = [f"• {s.strip()}" for s in sentences if len(s.strip()) > 30]
    return "\n".join(notes)
import openai  # or any LLM-based library you're using

def generate_notes(text):
    prompt = f"Summarize the following educational content into concise study notes:\n\n{text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or whichever model you’re using
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )

    return response["choices"][0]["message"]["content"]
