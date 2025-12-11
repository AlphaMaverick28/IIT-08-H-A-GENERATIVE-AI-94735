
sentence = input("Enter a sentence: ").strip()


num_chars = len(sentence.replace(" ", ""))


words = sentence.split()
num_words = len(words)


vowels = set("aeiouAEIOU")
num_vowels = sum(1 for ch in sentence if ch in vowels)

print(f"Number of characters (no spaces): {num_chars}")
print(f"Number of words: {num_words}")
print(f"Number of vowels: {num_vowels}")
