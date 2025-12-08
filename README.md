
# PANW Case Study: AI-Powered Journal CLI

This project acts as a smart journaling assistant that automatically tags your entries with emotions using a custom fine-tuned AI model. It features a CLI for easy interaction and a robust backend powered by Hugging Face Transformers.

## Features

- **Sentiment Analysis**: Automatically tags journal entries with specific emotional states (e.g., `positive_high_energy`,`positive_low_energy`, `negative_high_stress`, `negative_low_energy`, and `neutral`.).
- **Fine-Tuned Model**: Uses a custom RoBERTa model which was finetuned on a curated dataset of metaphors, idioms, and other edge case statements.
- **CLI Interface**: Simple command-line tools to add, view, and clear journal entries.
- **Persistent Storage**: Entries are saved locally in a JSON file named entries.json.

## Approach & Model Selection

I evaluated multiple sentiment engines before settling on the current solution:

- **VADER**: extremely fast but produced shallow labels that missed nuance, so accuracy was not acceptable.
- **Gemini**: highly accurate, but pricing and rate limits result in low scalibility inside a journaling CLI.
- **DistilBERT**: a distilled version of the BERT model (a pretrained language understanding module) resulting in a faster inference than the final model but accuracy lagged with idioms and emoji-heavy text.

The winning approach fine-tunes **RoBERTa**, a more accurate and better version of BERT. I then used LLMs to create 4000+ edge case and idiomatic statements filled with slang to finetune the RoBERTa model to produce better accuracy with difficult statements.

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

On first run, the model must load from HuggingFace so that may take a minute or two. Subsequent runs will be much faster.

### 1. Add a Journal Entry
Type your thoughts, and the model will analyze and tag them.
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

The intelligence comes from `svkapoor/5EmoteModelRoBERTa`, the model fine-tuned specifically for this project.

-   **Base Model**: `SamLowe/roberta-base-go_emotions`
-   **Training Script**: `training/main.ipynb`
-   **Methodology**: The model underwent a rigorous two-stage fine-tuning process to maximize adaptability and nuance:
    1.  **Stage 1 - Slang & Emoji Adaptation**: The base model (`SamLowe/roberta-base-go_emotions`) was first fine-tuned on `train.jsonl` and `train_v2.jsonl`. This stage focused on teaching the model modern internet slang, emoji context, and general sentiment patterns.
    2.  **Stage 2 - Idiomatic Refinement**: The resulting model was then fine-tuned *again* using `idioms.jsonl` and `train_updated.jsonl`. This critical step refined the model's ability to understand idiomatic expressions (e.g., distinguishing "I'm on thin ice" from "I'm cool as ice") and corrected varied labels (e.g. shifting `anxious` to `negative_low_energy`).

-   **Data Sources**: located in `training/data/`
    -   `train.jsonl` / `train_v2.jsonl`: Synthetic slang and emoji-rich data.
    -   `idioms.jsonl`: specialized dataset for idioms.
    -   `train_updated.jsonl`: Correction dataset to refine specific labels.

## Testing

We use `pytest` to ensure model accuracy and system reliability.

To run the tests:
```bash
python -m pytest
```

The tests cover:
-   **Sentiment Analysis**: Verifies that specific phrases (including emojis and idioms) return the expected emotional tags.
-   **End-to-End**: Ensures the full application flow works as expected.
