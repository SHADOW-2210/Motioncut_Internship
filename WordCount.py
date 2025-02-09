import re

# Counting words
def word_count(string):
    words = re.findall(r'\b\w+\b', s)
    return len(words)

s=input("Enter your Sentence or Paragraph")
if len(s)==0:
    print("Invalid input")
else:
    print(word_count(s))