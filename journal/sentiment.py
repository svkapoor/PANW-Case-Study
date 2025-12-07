from transformers import pipeline

import os

# Get the absolute path to the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct path to the model relative to this script
model_path = os.path.join(current_dir, "..", "training", "emotion_model")

emotion_analyzer = pipeline("text-classification",
                    model=model_path,
                    return_all_scores=False)

def analyze_sentiment(text):
    result = emotion_analyzer(text)
    return result[0]['label']

if __name__ == "__main__":
    print(analyze_sentiment(""))
