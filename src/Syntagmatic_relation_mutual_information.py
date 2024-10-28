import math

class Syntagmatic_relation_mutual_information():

    def __init__(self, target_word, individual_words_probabilities, target_word_probabilities_with_others, vocabulary):

        self.target_word = target_word

        self.individual_words_probabilities = individual_words_probabilities

        self.target_word_and_word_frequency = target_word_probabilities_with_others[0]

        self.vocabulary = vocabulary

        self.word_syntagmatic_relations = self.compute_syntagmatic_relations()

    
    def compute_syntagmatic_relations(self):

        syntagmatic_relations = {}

        for word in self.vocabulary:

            syntagmatic_relations[word] = self.I(word)

        return syntagmatic_relations

    
    def I(self, w2):

        pw1 = self.individual_words_probabilities[self.target_word]
        pw2 = self.individual_words_probabilities[w2]
        pw1w2 = self.target_word_and_word_frequency[w2]

        try:

            Iw1w2 = pw1w2 * math.log(pw1w2 / (pw1 * pw2))

        except:

            Iw1w2 = 0

        return Iw1w2