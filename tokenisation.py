import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = input("Enter a sentence: ")
words = word_tokenize(text)

print("\nWord Tokens:")
print(words)

print("\nCharacter Tokens (word by word):")

for word in words:
    char_list = [c for c in word]   # ✔ working method
    print(f"{word} -> {char_list}")