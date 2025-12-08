from transformers import pipeline

import os


'''

Commented code below used for testing locally 
Change model parameter in pipeline to model_path

'''
# Get the absolute path to the current script's directory
# current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct path to the model relative to this script
# model_path = os.path.join(current_dir, "..", "training", "finetuned_model")

from transformers import logging
logging.set_verbosity_error()

# Calls the model
emotion_analyzer = pipeline("text-classification",
                    model= "svkapoor/5Emote_Journal_RoBERTa",
                    top_k=1)

# Runs the model
def analyze_sentiment(text):
    result = emotion_analyzer(text)
    return result[0][0]['label']

if __name__ == "__main__":
    print(analyze_sentiment("i am destroying this assignment"))
    print(analyze_sentiment("ts is destroying me"))

