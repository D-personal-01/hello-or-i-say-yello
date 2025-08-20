import random

# Updated mapping of letters to possible replacements
letters = {
    "H": ["H", "h", "Y", "y", "b","B", "]-[", "#"], 
    "E": ["E", "e", "3", "i", "I", "€","£","ê","ë"],
    "L": ["L", "l", "1", "|", "!", "¬"], 
    "O": ["O", "o", "0", "()", "°", "Ω", "ø", "¤"]
}

def random_hello():
    """Generate one random variation of HELLO"""
    return "".join(random.choice(letters[ch]) for ch in "HELLO")

# Store unique results
results = set()

# Keep generating until we have exactly 1000 unique variations
while len(results) < 1000:
    results.add(random_hello())

# Print them
for word in results:
    print(word)

print(f"\nTotal generated: {len(results)}")
