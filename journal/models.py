from dataclasses import dataclass

# Data class for storage of entries
@dataclass
class JournalEntry:
    text: str
    tag: str
    date: str

    def to_dict(self) -> dict:
        """Convert entry to a dictionary for JSON storage."""
        return {
            "text": self.text,
            "tag": self.tag,
            "date": self.date,
        }

