from transformers import pipeline

emotion_analyzer = pipeline("text-classification",
                    model="SamLowe/roberta-base-go_emotions",
                    return_all_scores=False)

def analyze_sentiment(text):
    result = emotion_analyzer(text)
    return result[0]['label']

if __name__ == "__main__":
    print(analyze_sentiment(""))
