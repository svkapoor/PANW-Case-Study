from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import google.generativeai as genai
import socket
from journal.config import GEMINI_API_KEY


def is_online():
    try:
        # attempts DNS resolution for google.com
        socket.gethostbyname("google.com")
        return True
    except:
        return False




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
    online = is_online()
    key = GEMINI_API_KEY
    if online and key:
        # Use gemini for online
        gemini_tag = call_gemini_sentiment(text)
        if gemini_tag:
            return gemini_tag
    
    # Use vader for offline
    return run_vader(text)

def run_vader(text):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

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


def call_gemini_sentiment(text):
    if not GEMINI_API_KEY:
        return None

    genai.configure(api_key=GEMINI_API_KEY)

    prompt = f"""
Classify the sentiment of this text into negative, slightly negative, neutral, slightly positive, and positive.

Text:
{text}

Only return the category name.
    """

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        result = response.text.strip()
        return result
    except Exception:
        return None



# Testing
if __name__ == "__main__":
    # Cleaning Test
    statement = "Its raining crazy"
    print(clean_text("Cleaned statement " + statement))
    print("Sentiment: " + analyze_sentiment(statement))
