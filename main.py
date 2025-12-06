import sys

from journal.models import JournalEntry
from journal.storage import load_entries, save_entry
from journal.sentiment import analyze_sentiment


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [add <text> | summary]")
        return

    command = sys.argv[1]

    # Adding another statement
    if command == "add":
        # The user must provide some text
        if len(sys.argv) < 3:
            print("Error: No text provided for 'add' command.")
            return

        # Combine everything after 'add' into one string
        text = " ".join(sys.argv[2:])

        # Analyze sentiment
        tag = analyze_sentiment(text)

        # Create entry object
        entry = JournalEntry(text=text, tag=tag)

        # Save entry
        save_entry(entry.to_dict())

        print(f"Saved entry with tag: {tag}")
        return
    
    # Checking last three statements
    if command == "summary":
        entries = load_entries()

        if not entries:
            print("No entries yet.")
            return

        # Get last 3 entries
        if len(entries) < 3:
            arr = entries
        else:
            arr = entries[-3:]
        
        for entry in reversed(arr):
            print(f"Text: {entry['text']}")
            print(f"Tag: {entry['tag']}")
            print("")
        

        return

if __name__ == "__main__":
    main()
