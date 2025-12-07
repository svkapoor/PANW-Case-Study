from journal.sentiment import analyze_sentiment

def test_analyze_sentiment_neutral_steadying():
    result = analyze_sentiment("This situation is steadying my senses")
    assert result in ["neutral", "positive_low_energy"]

def test_analyze_sentiment_negative_high_stress_collapsing():
    result = analyze_sentiment("I feel like I am collapsing under pressure")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_analyze_sentiment_positive_high_energy_climbing():
    result = analyze_sentiment("I feel like I am climbing under pressure")
    assert result in ["positive_high_energy", "optimism"]

def test_analyze_sentiment_intense_too_much():
    result = analyze_sentiment("Everything feels too intense")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_analyze_sentiment_neutral_intense_appropriate():
    result = analyze_sentiment("Everything feels appropriately intense")
    assert result in ["neutral", "positive_high_energy"]

def test_analyze_sentiment_fears_louder():
    result = analyze_sentiment("My fears keep getting louder")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_analyze_sentiment_positive_low_energy_fears_quieter():
    result = analyze_sentiment("My fears keep getting quieter")
    assert result in ["positive_low_energy", "neutral"]

def test_analyze_sentiment_world_closing():
    result = analyze_sentiment("I feel like the world is closing in on me")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_analyze_sentiment_positive_low_energy_world_opening():
    result = analyze_sentiment("I feel like the world is opening up for me")
    assert result in ["positive_low_energy", "optimism"]

def test_analyze_sentiment_negative_high_stress_stress_worse():
    result = analyze_sentiment("My stress is getting worse")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_analyze_sentiment_neutral_stress_easing():
    result = analyze_sentiment("My stress is easing off")
    assert result in ["neutral", "positive_low_energy"]

def test_analyze_sentiment_uneasy_cannot_stop():
    result = analyze_sentiment("I cannot stop feeling uneasy")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_analyze_sentiment_neutral_no_longer_uneasy():
    result = analyze_sentiment("I no longer feel uneasy")
    assert result in ["neutral", "positive_low_energy"]

def test_analyze_sentiment_negative_high_stress_too_much_handle():
    result = analyze_sentiment("This moment feels too much to handle")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_analyze_sentiment_neutral_simple_handle():
    result = analyze_sentiment("This moment feels simple to handle")
    assert result in ["neutral", "positive_low_energy"]

def test_analyze_sentiment_negative_low_energy_drained():
    result = analyze_sentiment("I feel drained mentally")
    assert result in ["negative_low_energy", "negative_high_stress"]
