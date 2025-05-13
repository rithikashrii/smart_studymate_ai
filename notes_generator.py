def generate_detailed_notes(text):
    # Simplified logic – replace with AI model or NLP rules if needed
    sentences = text.split('.')
    notes = [f"• {s.strip()}" for s in sentences if len(s.strip()) > 30]
    return "\n".join(notes)
