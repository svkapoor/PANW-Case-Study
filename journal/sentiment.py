def clean_text(text: str) -> str:
    """
    Basic cleaning for journaling text.
    - Do not lowercase as all caps can show emotion
    - remove surrounding whitespace
    - collapse multiple spaces into one
    """
    text = text.strip()
    text = " ".join(text.split())
    return text

# Testing
if __name__ == "__main__":
    print(clean_text("Butterflys are    awesome.  "))