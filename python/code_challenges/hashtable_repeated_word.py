from data_structures.hashtable import Hashtable
import re

def first_repeated_word(string):

    lower_cased = string.lower()
    words = re.findall(r'\b[a-z]+\b', lower_cased)
    
    words_seen = set()
    for word in words:
        if word in words_seen:
            return word
        words_seen.add(word)
    return None
