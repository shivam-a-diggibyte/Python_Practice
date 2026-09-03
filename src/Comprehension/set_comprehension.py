words = ["apple", "fig", "banana", "kiwi", "plum"]

unique_lengths = {len(w) for w in words}

print("Words:", words)

print("Unique lengths:", unique_lengths) # because set automatically removes duplicates
