from journal.sentiment import analyze_sentiment

def test_analyze_sentiment_content_optimism():
    result = analyze_sentiment("I am so happy")
    assert result == "optimism"

def test_analyze_sentiment_content_sadness():
    result = analyze_sentiment("my mom died")
    assert result == "sadness"

def test_analyze_sentiment_content_anger():
    result = analyze_sentiment("i am pissed")
    assert result == "anger"