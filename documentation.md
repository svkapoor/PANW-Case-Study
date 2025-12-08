# PANW Case Study Documentation

## Submission Checklist
- **Working Prototype/Demo 💻**: This repository (`PANW-Case-Study/`) contains the fully functional CLI, training artifacts, datasets, and tests required to run the journaling assistant locally.
- **Design Documentation 📝**: This `documentation.md` summarizes the system design, technical decisions, and instructions for running and validating the solution.

## 1. Solution Overview
The PANW Case Study project is a CLI-based smart journaling assistant. Users create entries from the terminal (`python main.py add "..."`), and the application automatically classifies each entry into one of five emotion buckets using a fine-tuned RoBERTa transformer served via Hugging Face. Entries persist locally inside `data/entries.json` so the CLI can summarize or clear past reflections.

### Goals
1. Fast, offline-friendly journaling workflow.
2. Emotion labels that capture nuanced, idiomatic language rather than generic positive/negative sentiment.
3. Simple local persistence requiring no external database.

## 2. System Architecture
```
+-----------+        +----------------+        +-----------------+
| CLI User  | -----> | main.py        | -----> | journal.sentiment|
+-----------+        | (command parser)|        | (HF pipeline)    |
       ^             +----------------+        +-----------------+
       |                     |                           |
       |                     v                           v
       |             +----------------+        +------------------+
       |             | journal.storage| -----> | data/entries.json|
       |             +----------------+        +------------------+
       |                     |
       +----- summary/clear -+
```
- `main.py`: Parses CLI arguments (`add`, `summary`, `clear`).
- `journal/sentiment.py`: Wraps a Hugging Face `pipeline` bound to `svkapoor/5Emote_Journal_RoBERTa` and returns the top predicted label.
- `journal/storage.py`: Provides load/save/clear helpers that read/write JSON on disk.
- `journal/models.py`: Defines the `JournalEntry` dataclass used within the CLI.
- `data/entries.json`: Acts as the persistent store for user entries.
- `training/`: Contains notebooks and datasets used to fine-tune the model.
- `tests/`: Pytest suites validating sentiment predictions and end-to-end flow.

## 3. Technical Stack
| Layer | Technology | Rationale |
| --- | --- | --- |
| Language & Runtime | Python 3.10+, standard library | Rapid prototyping, rich ecosystem. |
| CLI Framework | Native `argparse`-style parsing via `sys.argv` | Keeps CLI footprint minimal. |
| NLP Model | Hugging Face Transformers `pipeline` w/ `svkapoor/5Emote_Journal_RoBERTa` | Accurate emotion detection on slang/idioms after fine-tuning. |
| Storage | Local JSON file (`data/entries.json`) | Human-readable, no external dependencies. |
| Virtual Env | `python -m venv` | Ensures reproducible Python dependencies. |
| Testing | `pytest` | Lightweight automated verification. |

### External Dependencies (`requirements.txt`)
- `transformers`
- `torch`
- `datasets`
- `pytest`

## 4. Model & Data Design
- **Base Model**: `SamLowe/roberta-base-go_emotions` for broad emotional understanding.
- **Fine-tuned Model**: Hosted at `svkapoor/5Emote_Journal_RoBERTa` (HF). Fine-tuning stages:
  1. **Slang & Emoji Adaptation** (`train.jsonl`, `train_v2.jsonl`): teaches social-media tone + emoji semantics.
  2. **Idiomatic Refinement** (`idioms.jsonl`, `train_updated.jsonl`): handles metaphors and idioms ("on thin ice").
  3. **Neutral Greetings Calibration** (`greetings_train.jsonl`, `greetings_validation.jsonl`): prevents false positives on greetings like "hey man".
- **Labels**: `positive_high_energy`, `positive_low_energy`, `negative_high_stress`, `negative_low_energy`, `neutral`.
- **Storage Schema** (`data/entries.json`): array of objects
  ```json
  {
    "text": "I am crushing this project!",
    "tag": "positive_high_energy",
    "date": "2024-06-15 15:22:03"
  }
  ```

## 5. Runtime Flow
1. User invokes CLI with `add`, `summary`, or `clear`.
2. `main.py` routes command:
   - `add`: builds `JournalEntry`, calls `analyze_sentiment(text)` to obtain top label, then persists entry.
   - `summary`: loads entries, prints the three most recent entries + tags.
   - `clear`: truncates `entries.json` via `clear_entries()`.
3. Sentiment predictions rely on the embedded HF pipeline which downloads model weights on first run and caches them locally.

## 6. Setup & Execution
Refer to `README.md` for the full quick-start guide. Key steps:
1. Clone repository.
2. `cd PANW-Case-Study`.
3. Create venv (`python3 -m venv .venv`).
4. Activate venv (`source .venv/bin/activate` or `.venv\Scripts\activate`).
5. Install dependencies (`pip install -r requirements.txt`).
6. Seed data file if empty (`echo "[]" > data/entries.json`).
7. Run CLI:
   ```bash
   python main.py add "I am crushing this project!"
   python main.py summary
   python main.py clear
   ```

## 7. Testing Strategy
- **Command**: `python -m pytest`
- **Unit Coverage**: Validates sentiment analyzer wiring, storage helpers, and CLI input handling.
- **Integration Coverage**: Ensures full add/summary loop writes and reads entries, matching expected JSON structure.
- **Manual QA**: Run `python main.py add` with idiom/slang-heavy sentences to confirm nuanced labels.

## 8. Deployment & Distribution
- Designed for local execution; no cloud services required after first HF model download.
- Model weights pulled dynamically from Hugging Face; caching managed by Transformers.
- For packaging, the CLI can be wrapped with `pipx` entry points or Dockerized (future work).

## 9. Future Enhancements
1. **Encryption**: Protect local journal data with symmetric encryption.
2. **UI Wrapper**: Build a lightweight TUI or web dashboard around the CLI for richer browsing.
3. **Scheduling**: Add reminders or Cron-compatible prompts to encourage consistent journaling.
4. **Export/Import**: Provide CSV/Markdown export of entries for backup.
5. **Model Drift Monitoring**: Periodically re-evaluate predictions against new slang datasets.

---
For any demo instructions or reviewer notes, reference `README.md` for command syntax and `tests/` for validation scripts.
