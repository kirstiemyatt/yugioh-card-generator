import numpy as np

def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        yield (corpus[i], corpus[i+1])

def create_word_mapping_dictionary(corpus):
    pairs = make_pairs(corpus)

    dictionary = {}

    for word_1, word_2 in pairs:
        if word_1 in dictionary.keys():
            dictionary[word_1].append(word_2)
        else:
            dictionary[word_1] = [word_2]

    return dictionary

def generate_cardtext(corpus, dictionary, length):
    first_word = np.random.choice(corpus)
    chain = [first_word]

    for i in range(length):
        chain.append(np.random.choice(dictionary[chain[-1]]))

    return  " ".join(chain)

def generate_corpus(filename):
    text = open(filename, encoding="utf-8").read()
    return text.split()


corpus = generate_corpus("spell.txt")
dictionary = create_word_mapping_dictionary(corpus)
cardtext = generate_cardtext(corpus, dictionary, 25)
print(cardtext)

