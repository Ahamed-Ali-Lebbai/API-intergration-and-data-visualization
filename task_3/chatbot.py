import spacy

# Load English tokenizer, POS tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Predefined Q&A pairs
qa_pairs = {
    "what is your name": "I am a chatbot created using spaCy!",
    "how are you": "I'm just code, but thanks for asking!",
    "what is nlp": "NLP stands for Natural Language Processing.",
    "bye": "Goodbye! Have a great day!"
}

def get_response(user_input):
    doc = nlp(user_input.lower())
    for question in qa_pairs:
        if question in user_input.lower():
            return qa_pairs[question]
    return "I'm sorry, I don't understand that."

def main():
    print("🤖 Chatbot: Hello! Ask me anything. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("🤖 Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("🤖 Chatbot:", response)

if __name__ == "__main__":
    main()
