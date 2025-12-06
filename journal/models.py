from dataclasses import dataclass

@dataclass
class JournalEntry:
    text: str
    tag: str

    def to_dict(self) -> dict:
        """Convert entry to a dictionary for JSON storage."""
        return {
            "text": self.text,
            "tag": self.tag,
        }
