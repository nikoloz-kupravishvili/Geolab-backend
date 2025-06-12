def get_vowel_starting_words(*words):
    vowels = 'aeiou'
    return [word for word in words if word and word[0].lower() in vowels]

