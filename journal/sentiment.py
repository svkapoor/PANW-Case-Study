from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Loads Vader's model
analyzer = SentimentIntensityAnalyzer()

def clean_text(text: str) -> str:
    """
    Basic cleaning for journaling text.
    - Do not lowercase as all caps can show emotion
    - remove surrounding whitespace
    - collapse multiple spaces into one
    """
    text = text.strip()
    text = " ".join(text.split())
    return text

def base_sentiment(text: str) -> str:
    """
    Use VADER to get basic sentiment classification.
    Returns one of: 'positive', 'negative', 'neutral'.
    """
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]  # summarizes positivity vs negativity

    if compound >= 0.6:
        return "very positive"
    elif compound >= 0.35:
        return "slightly positive"
    elif compound <= -0.6:
        return "very negative"
    elif compound <= -0.35:
        return "slightly negative"
    else:
        return "neutral"


# Call to return sentiment of statement
def analyze_sentiment(text: str) -> str:
    # Clean
    cleaned_txt = clean_text(text)
    sentiment = base_sentiment(cleaned_txt)
    return sentiment



# Testing
if __name__ == "__main__":
    # Cleaning Test
    statement = "Its raining crazy"
    print(clean_text("Cleaned statement " + statement))
    print("Sentiment: " + analyze_sentiment(statement))
