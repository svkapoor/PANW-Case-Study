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

For all further instructions and information, reference `README.md`.
