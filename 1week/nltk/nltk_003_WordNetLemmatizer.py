from nltk.stem import WordNetLemmatizer

words = ['lives', 'crying', 'flies', 'dying']

# WordNetLemmatizer:원형복원
lm = WordNetLemmatizer()

word = [lm.lemmatize(w) for w in words]

print(word)
# ['life', 'cry', 'fly', 'dying']

print(lm.lemmatize("dying", pos="v"))
# die