
# PANW Case Study: AI-Powered Journal CLI

This project acts as a smart journaling assistant that automatically tags your entries with emotions using a custom fine-tuned AI model. It features a CLI for easy interaction and a robust backend powered by Hugging Face Transformers.

## Features

- **Sentiment Analysis**: Automatically tags journal entries with specific emotional states (e.g., `positive_high_energy`, `negative_high_stress`, `negative_low_energy`, `positive_low_energy`, `neutral` etc.).
- **Fine-Tuned Model**: Uses a custom RoBERTa model trained on a curated dataset of idiomatic expressions and emotional nuances.
- **CLI Interface**: Simple command-line tools to add, view, and clear journal entries.
- **Persistent Storage**: Entries are saved locally in a JSON file.

## Setup & Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/svkapoor/PANW-Case-Study.git
    cd PANW-Case-Study
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: Requires `torch` and `transformers`.*

## Usage

Run the application using `main.py` in the root directory.

### 1. Add a Journal Entry
Type your thoughts, and the AI will analyze and tag them.
```bash
python main.py add "I am crushing this project!"
```
*Output: Saved entry with tag: positive_high_energy*

### 2. View Summary
View your last 3 journal entries and their emotional tags.
```bash
python main.py summary
```

### 3. Clear History
Delete all stored journal entries.
```bash
python main.py clear
```

## Data Storage
Journal entries are stored locally in:
```
data/entries.json
```
The file format is a list of JSON objects containing the text, tag, and timestamp.

## Model Training & Fine-Tuning

The core intelligence comes from `svkapoor/5EmoteModelRoBERTa`, a model fine-tuned specifically for this project.

-   **Base Model**: `SamLowe/roberta-base-go_emotions`
-   **Training Script**: `training/main.ipynb`
-   **Data**: The model was trained on a diverse set of examples located in `training/data/`, including:
    -   `train.jsonl` / `train_v2.jsonl`: General sentiment data.
    -   `idioms.jsonl`: Specialized dataset for understanding idiomatic expressions (e.g., "I'm on thin ice" vs "I'm on cloud nine").
-   **Method**: We used the Hugging Face `Trainer` API to fine-tune the model, focusing on distinguishing between subtle high-energy and high-stress states.

## Testing

We use `pytest` to ensure model accuracy and system reliability.

To run the tests:
```bash
python -m pytest
```

The tests cover:
-   **Sentiment Analysis**: Verifies that specific phrases (including emojis and idioms) return the expected emotional tags.
-   **End-to-End**: Ensures the full application flow works as expected.