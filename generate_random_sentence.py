import random
import string
import nltk
from nltk.corpus import words

# Download the word corpus if it's not already downloaded
nltk.download('words')

# List of words to use in the random sentences
words = words.words()

# List of words or phrases to use in the random sentences
# words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
punctuation = [".", "!", "?"]

def generate_random_sentence(min_length, max_length):
    # Generate a random sentence length between min_length and max_length words
    sentence_length = random.randint(min_length, max_length)
    
    # Select random words to form the sentence
    sentence = ' '.join(random.choices(words, k=sentence_length))
    
    # Capitalize the first letter of the sentence
    sentence = sentence.capitalize()
    
    # Add random punctuation at the end of the sentence
    sentence += random.choice(punctuation)
    
    return sentence