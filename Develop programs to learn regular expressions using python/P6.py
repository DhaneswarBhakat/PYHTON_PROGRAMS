import re

# Example 1: Matching a pattern
text = "Hello, my name is John. I live in New York."
pattern = r"John"
matches = re.findall(pattern, text)
print("Matches:", matches)

# Example 2: Searching and replacing
text = "Hello, my name is John. I live in New York."
pattern = r"John"
replacement = "Peter"
new_text = re.sub(pattern, replacement, text)
print("New Text:", new_text)

# Example 3: Splitting a string
text = "Hello, my name is John. I live in New York."
pattern = r"\W+"  # Splitting based on non-word characters
words = re.split(pattern, text)
print("Words:", words)

# Example 4: Matching email addresses
text = "Contact us at info@example.com or support@example.com"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(pattern, text)
print("Emails:", emails)
