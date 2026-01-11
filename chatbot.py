

positive_words = ["happy", "good", "great", "excellent", "love", "awesome", "amazing"]
negative_words = ["sad", "bad", "terrible", "hate", "awful", "worst", "angry"]

history = []
sentiment_count = {
    "Positive": 0,
    "Negative": 0,
    "Neutral": 0
}

def analyze_sentiment(text):
    text = text.lower()
    pos_count = sum(word in text for word in positive_words)
    neg_count = sum(word in text for word in negative_words)

    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

def show_stats():
    print("\nSentiment Statistics")
    for key, value in sentiment_count.items():
        print(f"{key}: {value}")

def show_history():
    print("\nConversation History")
    if not history:
        print("No conversations yet")
    for i, item in enumerate(history, 1):
        print(f"{i}. \"{item['text']}\" → {item['sentiment']}")

def reset_data():
    history.clear()
    for key in sentiment_count:
        sentiment_count[key] = 0
    print("\nAll data has been reset.")

def final_report():
    print("\nsentiment Report")
    total = sum(sentiment_count.values())
    print(f"total messages {total}")
    for key, value in sentiment_count.items():
        print(f"{key}: {value}")

print("Sentiment analysis chatbot")
print("type your message/ use commands: stats, history, reset, exit")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        final_report()
        print("Goodbye!")
        break

    elif user_input.lower() == "stats":
        show_stats()

    elif user_input.lower() == "history":
        show_history()

    elif user_input.lower() == "reset":
        reset_data()

    else:
        sentiment = analyze_sentiment(user_input)
        sentiment_count[sentiment] += 1
        history.append({"text": user_input, "sentiment": sentiment})
        print(f" bot: sentiment detected {sentiment}")

